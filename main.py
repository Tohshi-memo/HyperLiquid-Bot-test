from __future__ import annotations

import logging
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from rich.logging import RichHandler

from core.analyzer import TechnicalAnalyzer
from core.executor import ExecutorFactory, ProposalBuilder
from core.scanner import MarketScanner
from core.stats import StatsManager
from core.tracker import OUTCOME_SL_HIT, OUTCOME_TP_HIT, SymbolTracker
from utils.display import console, print_candidates
from utils.hyperliquid_client import HyperLiquidClient
from utils.notifier import Notifier


def load_environment() -> None:
    root = Path(__file__).parent
    env_path = root / ".env"
    if env_path.exists():
        load_dotenv(env_path)
    elif (root / ".env.example").exists():
        load_dotenv(root / ".env.example")


def setup_logging() -> None:
    log_level = getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper(), logging.INFO)
    log_file = Path(os.getenv("LOG_FILE", "logs/scanner.log"))
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            RichHandler(console=console, level=logging.WARNING, show_path=False),
            logging.FileHandler(log_file, encoding="utf-8"),
        ],
        force=True,
    )
    logging.getLogger("hyperliquid").setLevel(logging.WARNING)


def run_once(
    cycle: int,
    client: HyperLiquidClient,
    scanner: MarketScanner,
    analyzer: TechnicalAnalyzer,
    builder: ProposalBuilder,
    executor,
    tracker: SymbolTracker,
    stats: StatsManager,
    notifier: Notifier,
) -> None:
    logger = logging.getLogger(__name__)
    dry_run = os.getenv("DRY_RUN", "true").lower() != "false"
    cooldown_hours = int(os.getenv("COOLDOWN_HOURS", "48"))
    cb_window = int(os.getenv("CIRCUIT_BREAKER_WINDOW", "10"))
    cb_losses = int(os.getenv("CIRCUIT_BREAKER_LOSSES", "5"))

    console.rule(f"HyperLiquid Momentum Scanner cycle {cycle} {'DRY' if dry_run else 'LIVE'}")

    newly_closed = tracker.update_prices(client)
    if newly_closed:
        stats.record_many(newly_closed)
        for item in newly_closed:
            if item.outcome == OUTCOME_TP_HIT:
                notifier.notify_tp_sl_hit(
                    item.symbol,
                    item.detection_price,
                    item.outcome_price or item.current_price,
                    item.current_change_pct,
                    item.hours_tracked,
                    hit_tp=True,
                )
            elif item.outcome == OUTCOME_SL_HIT:
                notifier.notify_tp_sl_hit(
                    item.symbol,
                    item.detection_price,
                    item.outcome_price or item.current_price,
                    item.current_change_pct,
                    item.hours_tracked,
                    hit_tp=False,
                )

    summary = stats.summary(recent_window=cb_window)
    console.print(
        f"[dim]stats total={summary.total} wins={summary.wins} losses={summary.losses} "
        f"win_rate={summary.win_rate:.1f}% avg={summary.avg_pnl_pct:+.2f}% "
        f"recent_losses={summary.recent_losses}/{cb_window}[/dim]"
    )

    circuit_open = stats.circuit_breaker_active(cb_window, cb_losses)
    if circuit_open:
        console.print("[bold red]Circuit breaker active. New entries skipped this cycle.[/bold red]")

    btc, candidates = scanner.run_scan()
    console.print(
        f"BTC {btc.price:.8g} 1h={btc.change_1h_pct:+.2f}% regime={btc.regime}"
    )
    if candidates:
        print_candidates(
            "Surge candidates",
            [(c.symbol, c.price, c.change_1h_pct, c.relative_strength_pct) for c in candidates[:15]],
        )
    else:
        console.print("[dim]No surge candidates.[/dim]")

    if not candidates or circuit_open:
        _finalize_expired(tracker, stats, notifier)
        return

    analysis = analyzer.analyze_candidates(candidates)
    confirmed = [r for r in analysis if r.is_confirmed_signal]
    if not confirmed:
        console.print("[dim]No confirmed signals after technical filters.[/dim]")
        _finalize_expired(tracker, stats, notifier)
        return

    for result in confirmed:
        if stats.had_sl_within(result.symbol, cooldown_hours):
            console.print(f"[dim]{result.symbol} skipped: cooldown after recent SL.[/dim]")
            continue

        proposal = builder.build(result)
        exec_result = executor.execute(proposal)
        status = (exec_result or {}).get("status")
        if status not in {"dry_run", "ok"}:
            logger.warning("Execution skipped for %s: %s", result.symbol, exec_result)
            continue

        added = tracker.add_if_new(
            symbol=result.symbol,
            detection_price=proposal.entry_price,
            rsi=result.rsi,
            change_1h=result.change_1h_pct,
            sl_price=proposal.stop_loss,
            tp_price=proposal.take_profit,
            conviction="MEDIUM",
            market_regime=btc.regime,
            detection_rel_strength=result.relative_strength_pct,
        )
        if added:
            console.print(
                f"[green]{result.symbol} short signal[/green] entry={proposal.entry_price:.8g} "
                f"sl={proposal.stop_loss:.8g} tp={proposal.take_profit:.8g}"
            )
            notifier.notify_new_signal(
                symbol=result.symbol,
                entry=proposal.entry_price,
                sl=proposal.stop_loss,
                tp=proposal.take_profit,
                sl_pct=proposal.sl_pct,
                tp_pct=proposal.tp_pct,
                rsi=result.rsi,
                change_1h_pct=result.change_1h_pct,
                regime=btc.regime,
                relative_strength_pct=result.relative_strength_pct,
            )

    _finalize_expired(tracker, stats, notifier)


def _finalize_expired(tracker: SymbolTracker, stats: StatsManager, notifier: Notifier) -> None:
    expired = tracker.clean_expired()
    if not expired:
        return
    stats.record_many(expired)
    for item in expired:
        if item.outcome not in {OUTCOME_TP_HIT, OUTCOME_SL_HIT}:
            notifier.notify_tracking_expired(
                item.symbol,
                item.detection_price,
                item.current_price,
                item.current_change_pct,
                item.hours_tracked,
            )


def main() -> None:
    load_environment()
    setup_logging()

    run_once_mode = os.getenv("RUN_ONCE", "false").lower() == "true"
    interval = int(os.getenv("SCAN_INTERVAL_SECONDS", "300"))

    client = HyperLiquidClient()
    scanner = MarketScanner(client)
    analyzer = TechnicalAnalyzer(client)
    builder = ProposalBuilder()
    executor = ExecutorFactory.create(client)
    tracker = SymbolTracker()
    stats = StatsManager()
    notifier = Notifier()

    cycle = 0
    while True:
        cycle += 1
        try:
            run_once(cycle, client, scanner, analyzer, builder, executor, tracker, stats, notifier)
        except KeyboardInterrupt:
            console.print("Interrupted.")
            break
        except Exception:
            logging.getLogger(__name__).exception("Unhandled scanner cycle error")
        finally:
            tracker.save()
            stats.save()

        if run_once_mode:
            break
        time.sleep(interval)


if __name__ == "__main__":
    main()

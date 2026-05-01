from __future__ import annotations

import json
import logging
import os
import urllib.request

logger = logging.getLogger(__name__)


class Notifier:
    def __init__(self) -> None:
        self._webhook_url = os.getenv("DISCORD_WEBHOOK_URL", "").strip()

    def notify_new_signal(
        self,
        symbol: str,
        entry: float,
        sl: float,
        tp: float,
        sl_pct: float,
        tp_pct: float,
        rsi: float | None,
        change_1h_pct: float,
        regime: str,
        relative_strength_pct: float,
    ) -> None:
        rsi_text = f"{rsi:.1f}" if rsi is not None else "n/a"
        self._send(
            "HyperLiquid signal",
            (
                f"{symbol} short setup\n"
                f"entry={entry:.8g} sl={sl:.8g} (+{sl_pct:.2f}%) "
                f"tp={tp:.8g} (-{tp_pct:.2f}%)\n"
                f"1h={change_1h_pct:+.2f}% relBTC={relative_strength_pct:+.2f}% "
                f"RSI={rsi_text} regime={regime}"
            ),
        )

    def notify_tp_sl_hit(
        self,
        symbol: str,
        entry: float,
        exit_price: float,
        change_pct: float,
        hours_tracked: float,
        hit_tp: bool,
    ) -> None:
        outcome = "TP hit" if hit_tp else "SL hit"
        self._send(
            f"{symbol} {outcome}",
            f"entry={entry:.8g} exit={exit_price:.8g} change={change_pct:+.2f}% hours={hours_tracked:.1f}",
        )

    def notify_tracking_expired(
        self,
        symbol: str,
        entry: float,
        final_price: float,
        final_change_pct: float,
        hours_tracked: float,
    ) -> None:
        self._send(
            f"{symbol} tracking expired",
            f"entry={entry:.8g} final={final_price:.8g} change={final_change_pct:+.2f}% hours={hours_tracked:.1f}",
        )

    def _send(self, title: str, description: str) -> None:
        if not self._webhook_url:
            return
        payload = json.dumps({"embeds": [{"title": title, "description": description}]}).encode("utf-8")
        request = urllib.request.Request(
            self._webhook_url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=10) as response:
                if response.status >= 300:
                    logger.warning("Discord webhook returned HTTP %s", response.status)
        except Exception as e:
            logger.warning("Discord notification failed: %s", e)

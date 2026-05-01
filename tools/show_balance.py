"""Print HyperLiquid account balance and open perp positions."""
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

_root = Path(__file__).parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from utils.hyperliquid_client import HyperLiquidClient


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value) if value is not None else default
    except (TypeError, ValueError):
        return default


def fetch_account_overview() -> dict[str, Any]:
    if not (os.getenv("HYPERLIQUID_ACCOUNT_ADDRESS") or os.getenv("HYPERLIQUID_PRIVATE_KEY")):
        raise RuntimeError(
            "Set HYPERLIQUID_ACCOUNT_ADDRESS or HYPERLIQUID_PRIVATE_KEY before reading the account."
        )

    client = HyperLiquidClient()
    balance = client.fetch_balance()
    usdc_info = balance.get("USDC", {}) or {}
    positions = client.exchange.fetch_positions()

    return {
        "total_usdc": _safe_float(usdc_info.get("total")),
        "free_usdc": _safe_float(usdc_info.get("free")),
        "used_usdc": _safe_float(usdc_info.get("used")),
        "unrealized_pnl": sum(_safe_float(p.get("unrealizedPnl")) for p in positions),
        "positions": positions,
    }


def print_overview(overview: dict[str, Any]) -> None:
    sep = "=" * 72
    print(sep)
    print("  HyperLiquid Perp Account")
    print(sep)
    print(f"  Account value : ${overview['total_usdc']:>12,.2f} USDC")
    print(f"  Withdrawable  : ${overview['free_usdc']:>12,.2f} USDC")
    print(f"  Margin used   : ${overview['used_usdc']:>12,.2f} USDC")
    pnl = overview["unrealized_pnl"]
    sign = "+" if pnl >= 0 else ""
    print(f"  Unrealized PnL: {sign}${pnl:>11,.2f} USDC")
    print()

    positions = overview["positions"]
    if not positions:
        print("  Open positions: none")
        print(sep)
        return

    print(f"  Open positions: {len(positions)}")
    print(f"  {'COIN':<12} {'SIDE':<6} {'SIZE':>12} {'ENTRY':>13} {'MARK':>13} {'uPnL':>12}")
    print("  " + "-" * 66)
    for pos in positions:
        upnl = _safe_float(pos.get("unrealizedPnl"))
        print(
            f"  {str(pos.get('symbol')):<12} "
            f"{str(pos.get('side')):<6} "
            f"{_safe_float(pos.get('contracts')):>12.4f} "
            f"${_safe_float(pos.get('entryPrice')):>12.6g} "
            f"${_safe_float(pos.get('markPrice')):>12.6g} "
            f"{'+' if upnl >= 0 else ''}${upnl:>10.2f}"
        )
    print(sep)


def main() -> int:
    try:
        from dotenv import load_dotenv

        env_path = _root / ".env"
        if env_path.exists():
            load_dotenv(env_path)
    except ImportError:
        pass

    try:
        overview = fetch_account_overview()
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 1

    print_overview(overview)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

from rich.console import Console
from rich.table import Table

console = Console()


def print_candidates(title: str, rows: list[tuple[str, float, float, float]]) -> None:
    table = Table(title=title)
    table.add_column("Coin")
    table.add_column("Price", justify="right")
    table.add_column("1h", justify="right")
    table.add_column("Rel BTC", justify="right")
    for symbol, price, change, rel in rows:
        table.add_row(symbol, f"{price:.8g}", f"{change:+.2f}%", f"{rel:+.2f}%")
    console.print(table)

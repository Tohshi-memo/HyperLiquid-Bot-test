# HyperLiquid Momentum Scanner

HyperLiquid perpetual markets for short-side momentum exhaustion signals.

This is a HyperLiquid rewrite of the original MEXC momentum scanner.  The core
flow is unchanged:

1. Read BTC regime and scan active perp coins.
2. Find coins with strong 1h moves and relative strength versus BTC.
3. Run RSI, Bollinger Band, ATR, volume, funding, OI, and multi-timeframe checks.
4. Track dry-run/shadow outcomes in `data/`.
5. Optionally place live HyperLiquid short entries with reduce-only SL/TP trigger orders.

## Quick Start

```bash
pip install -r requirements.txt
copy .env.example .env
python main.py
```

`DRY_RUN=true` is the default and is strongly recommended until the account,
API wallet, and GitHub secrets are tested.

## HyperLiquid Settings

Public scanning works without keys.  Private reads and live orders use:

```ini
HYPERLIQUID_PRIVATE_KEY=
HYPERLIQUID_ACCOUNT_ADDRESS=
HYPERLIQUID_VAULT_ADDRESS=
HYPERLIQUID_TESTNET=false
DRY_RUN=true
```

For an API wallet, put the API wallet private key in
`HYPERLIQUID_PRIVATE_KEY` and the main account address in
`HYPERLIQUID_ACCOUNT_ADDRESS`.

## Live Trading

When `DRY_RUN=false`, the executor:

- checks account balance and open positions
- skips duplicate symbols and max-position overflow
- sizes by risk percentage and SL distance
- opens a market short through the official HyperLiquid SDK
- places reduce-only trigger orders for stop loss and take profit

Live mode can lose real funds.  Test on HyperLiquid testnet first by setting
`HYPERLIQUID_TESTNET=true`.

## GitHub Actions

`.github/workflows/scanner.yml` runs one scan every five minutes and commits
updated `data/` files back to the repository.  Add these secrets before using
live or private account features:

- `HYPERLIQUID_PRIVATE_KEY`
- `HYPERLIQUID_ACCOUNT_ADDRESS`
- `HYPERLIQUID_VAULT_ADDRESS` (optional)
- `DISCORD_WEBHOOK_URL` (optional)

`tools/show_balance.py` and the `Show HyperLiquid Balance` workflow print the
HyperLiquid account summary and open perp positions.

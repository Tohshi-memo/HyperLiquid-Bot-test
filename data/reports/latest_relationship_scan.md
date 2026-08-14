# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T23:07:28.782405+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_24h` score `136.4097` n `128` status `ready` deltaP `-30.6424` edge `11.863` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.9452` n `32` status `ready` deltaP `-43.9236` edge `4.5916` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.9452` n `32` status `ready` deltaP `-43.9236` edge `4.5916` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.9996` n `36` status `ready` deltaP `15.9722` edge `0.8481` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6765` n `36` status `ready` deltaP `40.3963` edge `0.3704` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9238` n `128` status `ready` deltaP `27.8645` edge `0.2303` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.4999` n `32` status `ready` deltaP `30.2083` edge `0.1736` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.4999` n `32` status `ready` deltaP `30.2083` edge `0.1736` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.3185` n `32` status `ready` deltaP `22.2222` edge `0.3929` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.3185` n `32` status `ready` deltaP `22.2222` edge `0.3929` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.6778` n `32` status `ready` deltaP `18.6738` edge `0.1169` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6778` n `32` status `ready` deltaP `18.6738` edge `0.1169` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.6297` n `36` status `ready` deltaP `19.7917` edge `0.0872` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7841` n `36` status `ready` deltaP `20.5284` edge `0.025` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7406` n `36` status `ready` deltaP `8.5829` edge `0.1197` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.73` n `128` status `ready` deltaP `17.1113` edge `0.0772` maxDD `-0.7687`
- `risk_on_high->commodity_1h` score `1.2479` n `32` status `ready` deltaP `13.3608` edge `0.0382` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2479` n `32` status `ready` deltaP `13.3608` edge `0.0382` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `0.9886` n `32` status `ready` deltaP `12.1528` edge `0.0198` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `0.9886` n `32` status `ready` deltaP `12.1528` edge `0.0198` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T05:52:25.826273+00:00`
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

- `market_context_high->unknown_24h` score `136.7174` n `128` status `ready` deltaP `-28.3855` edge `11.8736` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.1453` n `32` status `ready` deltaP `-41.6667` edge `4.6022` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.1453` n `32` status `ready` deltaP `-41.6667` edge `4.6022` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.7704` n `36` status `ready` deltaP `20.3125` edge `0.8834` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.4286` n `36` status `ready` deltaP `37.9573` edge `0.366` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.937` n `128` status `ready` deltaP `27.8645` edge `0.2314` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.5131` n `32` status `ready` deltaP `30.2083` edge `0.1747` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5131` n `32` status `ready` deltaP `30.2083` edge `0.1747` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0544` n `32` status `ready` deltaP `26.9097` edge `0.456` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.0544` n `32` status `ready` deltaP `26.9097` edge `0.456` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.0587` n `36` status `ready` deltaP `24.4792` edge `0.0917` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.7474` n `32` status `ready` deltaP `19.5884` edge `0.1166` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.7474` n `32` status `ready` deltaP `19.5884` edge `0.1166` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.7996` n `128` status `ready` deltaP `18.0259` edge `0.0769` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7147` n `36` status `ready` deltaP `19.7662` edge `0.0243` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6663` n `36` status `ready` deltaP `7.6847` edge `0.1195` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2096` n `32` status `ready` deltaP `12.9117` edge `0.038` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2096` n `32` status `ready` deltaP `12.9117` edge `0.038` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `0.6503` n `32` status `ready` deltaP `8.8542` edge `0.0136` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `0.6503` n `32` status `ready` deltaP `8.8542` edge `0.0136` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

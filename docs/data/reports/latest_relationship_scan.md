# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T20:52:25.235165+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `87.6535` n `152` status `ready` deltaP `-26.6996` edge `7.7737` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7233` n `32` status `ready` deltaP `-41.6667` edge `4.6763` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7233` n `32` status `ready` deltaP `-41.6667` edge `4.6763` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.6202` n `36` status `ready` deltaP `10.0694` edge `0.7725` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.6263` n `36` status `ready` deltaP `35.5183` edge `0.3154` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.5565` n `32` status `ready` deltaP `31.7708` edge `0.1679` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5565` n `32` status `ready` deltaP `31.7708` edge `0.1679` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.8924` n `32` status `ready` deltaP `20.3506` edge `0.1236` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8924` n `32` status `ready` deltaP `20.3506` edge `0.1236` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.5596` n `152` status `ready` deltaP `21.2445` edge `0.152` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.4275` n `36` status `ready` deltaP `15.1042` edge `0.1016` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.6761` n `32` status `ready` deltaP `19.0972` edge `0.0308` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6761` n `32` status `ready` deltaP `19.0972` edge `0.0308` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6129` n `36` status `ready` deltaP `19.004` edge `0.0209` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.5731` n `152` status `ready` deltaP `17.2256` edge `0.0801` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.5212` n `36` status `ready` deltaP `7.2356` edge `0.1104` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.3471` n `32` status `ready` deltaP `13.0208` edge `0.2015` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.3471` n `32` status `ready` deltaP `13.0208` edge `0.2015` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.3054` n `32` status `ready` deltaP `13.9596` edge `0.039` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3054` n `32` status `ready` deltaP `13.9596` edge `0.039` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

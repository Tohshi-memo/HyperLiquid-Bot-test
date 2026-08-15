# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T03:50:21.254163+00:00`
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

- `market_context_high->unknown_24h` score `136.7416` n `128` status `ready` deltaP `-28.0382` edge `11.8733` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.161` n `32` status `ready` deltaP `-41.3194` edge `4.6019` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.161` n `32` status `ready` deltaP `-41.3194` edge `4.6019` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.5923` n `36` status `ready` deltaP `19.2708` edge `0.8755` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.4918` n `36` status `ready` deltaP `38.5671` edge `0.3672` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9214` n `128` status `ready` deltaP `27.8645` edge `0.2301` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.4975` n `32` status `ready` deltaP `30.2083` edge `0.1734` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.4975` n `32` status `ready` deltaP `30.2083` edge `0.1734` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.9019` n `32` status `ready` deltaP `25.5208` edge `0.4457` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.9019` n `32` status `ready` deltaP `25.5208` edge `0.4457` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.9344` n `36` status `ready` deltaP `23.0903` edge `0.0906` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6986` n `32` status `ready` deltaP `18.9787` edge `0.1166` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6986` n `32` status `ready` deltaP `18.9787` edge `0.1166` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.7508` n `128` status `ready` deltaP `17.4162` edge `0.0769` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7293` n `36` status `ready` deltaP `19.9187` edge `0.0245` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6951` n `36` status `ready` deltaP `7.9841` edge `0.1199` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2491` n `32` status `ready` deltaP `13.3608` edge `0.0383` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2491` n `32` status `ready` deltaP `13.3608` edge `0.0383` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `0.731` n `32` status `ready` deltaP `9.5486` edge `0.0157` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `0.731` n `32` status `ready` deltaP `9.5486` edge `0.0157` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

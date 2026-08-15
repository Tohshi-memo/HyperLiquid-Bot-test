# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T05:36:56.644073+00:00`
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

- `market_context_high->unknown_24h` score `136.7138` n `128` status `ready` deltaP `-28.3855` edge `11.8733` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.1429` n `32` status `ready` deltaP `-41.6667` edge `4.6019` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.1429` n `32` status `ready` deltaP `-41.6667` edge `4.6019` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.7421` n `36` status `ready` deltaP `20.1389` edge `0.8822` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.4164` n `36` status `ready` deltaP `37.8049` edge `0.366` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9334` n `128` status `ready` deltaP `27.8645` edge `0.2311` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.5095` n `32` status `ready` deltaP `30.2083` edge `0.1744` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5095` n `32` status `ready` deltaP `30.2083` edge `0.1744` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0345` n `32` status `ready` deltaP `26.7361` edge `0.4546` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.0345` n `32` status `ready` deltaP `26.7361` edge `0.4546` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.0424` n `36` status `ready` deltaP `24.3056` edge `0.0915` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.7474` n `32` status `ready` deltaP `19.5884` edge `0.1166` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.7474` n `32` status `ready` deltaP `19.5884` edge `0.1166` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.7996` n `128` status `ready` deltaP `18.0259` edge `0.0769` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7013` n `36` status `ready` deltaP `19.6138` edge `0.0242` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6675` n `36` status `ready` deltaP `7.6847` edge `0.1196` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.1964` n `32` status `ready` deltaP `12.762` edge `0.0379` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1964` n `32` status `ready` deltaP `12.762` edge `0.0379` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `0.6678` n `32` status `ready` deltaP `9.0278` edge `0.0139` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `0.6678` n `32` status `ready` deltaP `9.0278` edge `0.0139` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

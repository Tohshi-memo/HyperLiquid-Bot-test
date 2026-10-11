# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T22:07:28.131038+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9132`

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

- `market_context_high->unknown_24h` score `1381.1409` n `40` status `ready` deltaP `-22.5694` edge `115.2819` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `47.6866` n `97` status `ready` deltaP `-2.7392` edge `4.0502` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.8008` n `40` status `ready` deltaP `27.6736` edge `0.5918` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.412` n `40` status `ready` deltaP `52.4306` edge `0.1848` maxDD `0.0`
- `market_context_high->unknown_1h` score `4.2724` n `109` status `ready` deltaP `-2.7069` edge `0.4077` maxDD `-1.0231`
- `market_context_high->fx_24h` score `3.0526` n `40` status `ready` deltaP `34.6875` edge `0.0361` maxDD `-0.0374`
- `risk_on_high->commodity_1h` score `1.7751` n `30` status `ready` deltaP `22.026` edge `0.0148` maxDD `-0.0975`
- `risk_on_and_context->commodity_1h` score `1.7751` n `30` status `ready` deltaP `22.026` edge `0.0148` maxDD `-0.0975`
- `market_context_high->crypto_major_24h` score `1.3888` n `40` status `ready` deltaP `-21.1111` edge `0.5713` maxDD `-17.8526`
- `risk_on_high->metal_1h` score `1.0052` n `30` status `ready` deltaP `17.7545` edge `0.0238` maxDD `-0.0637`
- `risk_on_and_context->metal_1h` score `1.0052` n `30` status `ready` deltaP `17.7545` edge `0.0238` maxDD `-0.0637`
- `risk_on_high->crypto_alt_1h` score `0.7794` n `30` status `ready` deltaP `8.992` edge `0.0955` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.7794` n `30` status `ready` deltaP `8.992` edge `0.0955` maxDD `-2.4421`
- `market_context_high->fx_4h` score `0.6293` n `97` status `ready` deltaP `11.1014` edge `0.0068` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.626` n `97` status `ready` deltaP `13.171` edge `0.0177` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.2826` n `109` status `ready` deltaP `6.8272` edge `0.0064` maxDD `-0.6025`
- `risk_on_high->fx_1h` score `0.2422` n `30` status `ready` deltaP `8.2435` edge `-0.0012` maxDD `-0.1501`
- `risk_on_and_context->fx_1h` score `0.2422` n `30` status `ready` deltaP `8.2435` edge `-0.0012` maxDD `-0.1501`
- `market_context_high->metal_4h` score `0.1043` n `97` status `ready` deltaP `8.9954` edge `0.021` maxDD `-1.1153`
- `market_context_high->crypto_alt_1h` score `0.0401` n `109` status `ready` deltaP `4.3743` edge `0.0794` maxDD `-4.9401`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

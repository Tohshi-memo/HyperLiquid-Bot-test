# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T08:51:50.422201+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.1411` n `81` status `ready` deltaP `6.1814` edge `0.258` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.4076` n `81` status `ready` deltaP `15.6279` edge `0.2596` maxDD `-4.666`
- `market_context_high->equity_1h` score `0.9632` n `97` status `ready` deltaP `8.5762` edge `0.0535` maxDD `-0.4329`
- `market_context_high->crypto_major_4h` score `0.7586` n `97` status `ready` deltaP `9.7216` edge `0.1005` maxDD `-3.1677`
- `market_context_high->metal_4h` score `0.701` n `97` status `ready` deltaP `14.0699` edge `0.0222` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6003` n `97` status `ready` deltaP `12.2029` edge `0.0074` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5267` n `97` status `ready` deltaP `9.4605` edge `0.0035` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.458` n `97` status `ready` deltaP `11.8557` edge `0.1114` maxDD `-5.5373`
- `market_context_high->metal_1h` score `-0.0366` n `97` status `ready` deltaP `4.0573` edge `0.0086` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.043` n `81` status `ready` deltaP `13.76` edge `-0.0765` maxDD `-0.1719`
- `market_context_high->fx_4h` score `-0.2557` n `97` status `ready` deltaP `2.6575` edge `0.0` maxDD `-0.3734`
- `market_context_high->crypto_alt_1h` score `-0.2878` n `97` status `ready` deltaP `3.1591` edge `0.0222` maxDD `-2.413`
- `market_context_high->equity_4h` score `-0.3614` n `97` status `ready` deltaP `0.8156` edge `0.0549` maxDD `-2.5696`
- `market_context_high->commodity_4h` score `-0.3946` n `97` status `ready` deltaP `3.6522` edge `0.0101` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.4476` n `97` status `ready` deltaP `1.6791` edge `0.0159` maxDD `-2.7581`
- `market_context_high->fx_1h` score `-0.4697` n `97` status `ready` deltaP `-3.741` edge `0.0009` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.6903` n `97` status `ready` deltaP `-0.0345` edge `0.0082` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.9019` n `97` status `ready` deltaP `-7.1332` edge `-0.0068` maxDD `-1.5684`
- `market_context_high->metal_24h` score `-1.5902` n `81` status `ready` deltaP `-5.1908` edge `0.0264` maxDD `-5.9871`
- `market_context_high->index_24h` score `-3.8735` n `81` status `ready` deltaP `-12.9469` edge `-0.1656` maxDD `-9.9083`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T09:37:35.164362+00:00`
- Price records: `672`
- Market context records: `4711`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7424`

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

- `market_context_high->unknown_1h` score `76.9412` n `144` status `ready` deltaP `14.0137` edge `6.3601` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.0993` n `142` status `ready` deltaP `13.2429` edge `0.4577` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.8353` n `135` status `ready` deltaP `14.7917` edge `0.23` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3061` n `144` status `ready` deltaP `2.4077` edge `0.0243` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6859` n `142` status `ready` deltaP `4.7772` edge `-0.0075` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9744` n `142` status `ready` deltaP `-2.1277` edge `-0.0025` maxDD `-1.9927`
- `market_context_high->commodity_4h` score `-0.9892` n `142` status `ready` deltaP `8.4056` edge `0.0279` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.1816` n `142` status `ready` deltaP `2.1491` edge `0.0111` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-1.1858` n `144` status `ready` deltaP `-1.5926` edge `0.0105` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.3212` n `144` status `ready` deltaP `-5.435` edge `-0.0059` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.6457` n `144` status `ready` deltaP `-3.9338` edge `-0.0105` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.2276` n `144` status `ready` deltaP `-1.2392` edge `-0.0768` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.7379` n `144` status `ready` deltaP `-1.4305` edge `-0.0944` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.3811` n `135` status `ready` deltaP `17.1065` edge `0.0713` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.4569` n `144` status `ready` deltaP `-5.6263` edge `-0.0771` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.7961` n `135` status `ready` deltaP `-13.044` edge `-0.0167` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-8.0983` n `142` status `ready` deltaP `-2.1491` edge `-0.1582` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.4011` n `135` status `ready` deltaP `-10.6366` edge `-0.0917` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.6658` n `142` status `ready` deltaP `3.1711` edge `-0.2468` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.8968` n `142` status `ready` deltaP `-2.5486` edge `-0.29` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T05:22:24.566557+00:00`
- Price records: `672`
- Market context records: `2836`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `2.355` n `142` status `ready` deltaP `3.1225` edge `0.2219` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.898` n `142` status `ready` deltaP `6.4904` edge `0.1369` maxDD `-3.7602`
- `market_context_high->crypto_alt_24h` score `0.7948` n `142` status `ready` deltaP `0.2715` edge `0.4561` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `0.7159` n `142` status `ready` deltaP `11.2114` edge `0.2943` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3301` n `142` status `ready` deltaP `13.3009` edge `0.0378` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0059` n `142` status `ready` deltaP `4.1811` edge `0.0457` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1264` n `142` status `ready` deltaP `3.5992` edge `0.0092` maxDD `-1.2855`
- `market_context_high->index_24h` score `-0.3917` n `142` status `ready` deltaP `3.8146` edge `0.04` maxDD `-2.5127`
- `market_context_high->fx_1h` score `-0.5778` n `142` status `ready` deltaP `-0.9867` edge `0.0028` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.607` n `142` status `ready` deltaP `-0.2825` edge `-0.0006` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7596` n `142` status `ready` deltaP `-0.466` edge `-0.0097` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7739` n `142` status `ready` deltaP `4.4974` edge `0.0468` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-1.0036` n `142` status `ready` deltaP `3.4769` edge `0.0351` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0082` n `142` status `ready` deltaP `-3.1985` edge `0.0206` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-1.0282` n `142` status `ready` deltaP `1.9624` edge `0.0392` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1689` n `142` status `ready` deltaP `-3.9054` edge `0.0065` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.3247` n `142` status `ready` deltaP `2.1427` edge `0.0079` maxDD `-10.0279`
- `market_context_high->crypto_alt_4h` score `-1.5105` n `142` status `ready` deltaP `13.5756` edge `0.2177` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.5511` n `142` status `ready` deltaP `-3.1005` edge `-0.0214` maxDD `-0.6418`
- `market_context_high->equity_24h` score `-1.9727` n `142` status `ready` deltaP `1.6163` edge `0.0252` maxDD `-12.6963`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

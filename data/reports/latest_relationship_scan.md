# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T16:37:26.865816+00:00`
- Price records: `672`
- Market context records: `6301`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11116`

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

- `news_risk_high->crypto_alt_24h` score `15.2418` n `32` status `ready` deltaP `43.2292` edge `0.9967` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9809` n `32` status `ready` deltaP `50.5208` edge `0.1616` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1961` n `32` status `ready` deltaP `43.8262` edge `0.0621` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1594` n `32` status `ready` deltaP `16.6667` edge `0.5001` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.1365` n `32` status `ready` deltaP `28.4722` edge `0.0921` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4003` n `32` status `ready` deltaP `28.8922` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4374` n `32` status `ready` deltaP `14.2777` edge `0.1358` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.0022` n `208` status `ready` deltaP `-1.9605` edge `0.1974` maxDD `-3.7317`
- `news_risk_high->crypto_alt_1h` score `0.9151` n `32` status `ready` deltaP `11.6205` edge `0.086` maxDD `-1.6923`
- `market_context_high->metal_4h` score `-0.0202` n `196` status `ready` deltaP `8.6455` edge `0.037` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1176` n `171` status `ready` deltaP `21.0709` edge `0.1013` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.37` n `208` status `ready` deltaP `4.2492` edge `0.002` maxDD `-1.8877`
- `news_risk_high->index_24h` score `-0.3913` n `32` status `ready` deltaP `5.7292` edge `-0.0012` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4996` n `196` status `ready` deltaP `6.0354` edge `0.0468` maxDD `-7.4205`
- `market_context_high->unknown_4h` score `-0.5758` n `196` status `ready` deltaP `-6.8784` edge `0.2511` maxDD `-11.925`
- `market_context_high->commodity_1h` score `-0.6491` n `208` status `ready` deltaP `-1.7417` edge `-0.0033` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.7117` n `208` status `ready` deltaP `-0.9155` edge `-0.002` maxDD `-0.7629`
- `news_risk_high->metal_1h` score `-0.7621` n `32` status `ready` deltaP `-3.4431` edge `-0.025` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.8457` n `208` status `ready` deltaP `-3.4517` edge `0.0015` maxDD `-0.9531`
- `market_context_high->crypto_alt_1h` score `-0.9551` n `208` status `ready` deltaP `5.1301` edge `0.0186` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

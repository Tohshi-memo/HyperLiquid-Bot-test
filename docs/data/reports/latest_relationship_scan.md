# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T22:52:24.606749+00:00`
- Price records: `672`
- Market context records: `5821`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10006`

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

- `market_context_high->equity_4h` score `0.3578` n `282` status `ready` deltaP `6.45` edge `0.1326` maxDD `-6.9958`
- `market_context_high->equity_24h` score `-0.1303` n `248` status `ready` deltaP `15.3954` edge `0.3944` maxDD `-31.6316`
- `market_context_high->fx_1h` score `-0.2069` n `282` status `ready` deltaP `3.1522` edge `0.001` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.533` n `282` status `ready` deltaP `-0.8908` edge `-0.0015` maxDD `-2.2045`
- `market_context_high->index_1h` score `-0.6044` n `282` status `ready` deltaP `0.7411` edge `0.0031` maxDD `-0.8419`
- `market_context_high->metal_1h` score `-0.6279` n `282` status `ready` deltaP `2.2147` edge `0.0` maxDD `-2.0339`
- `market_context_high->equity_1h` score `-0.7203` n `282` status `ready` deltaP `2.1999` edge `0.026` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.9461` n `282` status `ready` deltaP `2.9792` edge `0.0334` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0917` n `282` status `ready` deltaP `1.4662` edge `0.0327` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1686` n `282` status `ready` deltaP `0.8422` edge `0.0133` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.4886` n `248` status `ready` deltaP `9.4422` edge `0.028` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.495` n `282` status `ready` deltaP `0.0962` edge `0.0026` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.1596` n `282` status `ready` deltaP `-4.225` edge `-0.0428` maxDD `-9.1388`
- `market_context_high->commodity_4h` score `-2.6848` n `282` status `ready` deltaP `-1.0844` edge `-0.0167` maxDD `-8.6511`
- `market_context_high->crypto_major_4h` score `-2.7758` n `282` status `ready` deltaP `7.729` edge `0.1544` maxDD `-25.6458`
- `market_context_high->index_24h` score `-4.3333` n `248` status `ready` deltaP `3.7131` edge `0.0286` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.5052` n `282` status `ready` deltaP `5.1472` edge `0.0911` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.7753` n `248` status `ready` deltaP `-12.4608` edge `-0.0614` maxDD `-30.3426`
- `market_context_high->metal_24h` score `-7.4774` n `248` status `ready` deltaP `-2.6994` edge `-0.2276` maxDD `-16.8682`
- `market_context_high->crypto_alt_24h` score `-12.424` n `248` status `ready` deltaP `-10.0246` edge `-0.4953` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

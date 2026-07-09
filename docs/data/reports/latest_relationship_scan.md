# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T11:16:23.049900+00:00`
- Price records: `672`
- Market context records: `6177`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.6194` n `32` status `ready` deltaP `42.3848` edge `0.7838` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.1527` n `32` status `ready` deltaP `62.7986` edge `0.1774` maxDD `0.0`
- `news_risk_high->fx_4h` score `3.9995` n `32` status `ready` deltaP `41.6084` edge `0.0605` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3224` n `32` status `ready` deltaP `27.994` edge `0.0208` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `1.7772` n `32` status `ready` deltaP `15.7956` edge `0.2005` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.7646` n `194` status `ready` deltaP `1.1946` edge `0.2399` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2582` n `32` status `ready` deltaP `13.2298` edge `0.1198` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6642` n `32` status `ready` deltaP `8.6265` edge `0.0738` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.369` n `194` status `ready` deltaP `-1.0676` edge `0.2911` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.156` n `194` status `ready` deltaP `20.3916` edge `0.1409` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.0555` n `194` status `ready` deltaP `2.759` edge `0.0687` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.0954` n `32` status `ready` deltaP `9.663` edge `0.0105` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.307` n `194` status `ready` deltaP `0.9321` edge `-0.001` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.4087` n `32` status `ready` deltaP `14.0678` edge `-0.1073` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6607` n `194` status `ready` deltaP `3.6052` edge `0.01` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7639` n `194` status `ready` deltaP `-2.1791` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7808` n `32` status `ready` deltaP `-3.1437` edge `-0.0294` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8648` n `194` status `ready` deltaP `2.0109` edge `-0.0056` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9395` n `194` status `ready` deltaP `3.3752` edge `0.0323` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9655` n `194` status `ready` deltaP `3.7904` edge `0.0277` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

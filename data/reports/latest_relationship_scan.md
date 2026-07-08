# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T00:37:26.271271+00:00`
- Price records: `672`
- Market context records: `6034`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11125`

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

- `news_risk_high->fx_24h` score `7.9652` n `30` status `ready` deltaP `71.875` edge `0.1846` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3051` n `30` status `ready` deltaP `44.5732` edge `0.0662` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.7417` n `30` status `ready` deltaP `26.5973` edge `0.0717` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2574` n `30` status `ready` deltaP `27.0758` edge `0.0215` maxDD `-0.1113`
- `market_context_high->equity_24h` score `1.7333` n `180` status `ready` deltaP `29.7223` edge `0.5692` maxDD `-31.6107`
- `market_context_high->equity_4h` score `1.6287` n `206` status `ready` deltaP `8.9465` edge `0.1678` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `0.8239` n `30` status `ready` deltaP `10.1896` edge `0.0844` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2286` n `30` status `ready` deltaP `5.6188` edge `0.038` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1444` n `30` status `ready` deltaP `9.2361` edge `0.0441` maxDD `-2.3058`
- `news_risk_high->crypto_alt_24h` score `-0.0191` n `30` status `ready` deltaP `23.8889` edge `-0.1461` maxDD `-0.5131`
- `market_context_high->metal_1h` score `-0.408` n `206` status `ready` deltaP `3.43` edge `0.0047` maxDD `-2.0564`
- `market_context_high->index_24h` score `-0.4351` n `180` status `ready` deltaP `5.3472` edge `0.0786` maxDD `-5.6021`
- `news_risk_high->metal_1h` score `-0.4445` n `30` status `ready` deltaP `0.9381` edge `-0.0266` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.575` n `206` status `ready` deltaP `-0.141` edge `-0.0013` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6787` n `206` status `ready` deltaP `-1.683` edge `-0.0007` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.945` n `206` status `ready` deltaP `2.2629` edge `0.0171` maxDD `-1.9335`
- `market_context_high->metal_4h` score `-0.9515` n `206` status `ready` deltaP `4.9432` edge `0.0065` maxDD `-3.4996`
- `market_context_high->crypto_alt_1h` score `-0.9779` n `206` status `ready` deltaP `3.8065` edge `0.0245` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9938` n `206` status `ready` deltaP `3.6524` edge `0.025` maxDD `-9.807`
- `market_context_high->equity_1h` score `-1.0157` n `206` status `ready` deltaP `0.7805` edge `0.023` maxDD `-4.3608`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

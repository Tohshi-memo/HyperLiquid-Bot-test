# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T22:52:27.210034+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6574`

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

- `market_context_high->unknown_1h` score `338.4481` n `50` status `ready` deltaP `9.0778` edge `28.1484` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `286.9704` n `50` status `ready` deltaP `7.4695` edge `23.8644` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.1091` n `91` status `ready` deltaP `36.6911` edge `1.4521` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.5975` n `50` status `ready` deltaP `34.7778` edge `0.7929` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.3247` n `50` status `ready` deltaP `19.2195` edge `0.5526` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `6.2096` n `50` status `ready` deltaP `12.8889` edge `0.6025` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0934` n `50` status `ready` deltaP `16.6463` edge `0.4428` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.2305` n `91` status `ready` deltaP `17.613` edge `0.5505` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.7327` n `50` status `ready` deltaP `19.0417` edge `0.5378` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.064` n `104` status `ready` deltaP `26.2547` edge `0.1499` maxDD `-2.9013`
- `market_context_high->crypto_major_1h` score `3.0407` n `50` status `ready` deltaP `14.7485` edge `0.2001` maxDD `-2.2692`
- `market_context_high->fx_4h` score `3.0174` n `50` status `ready` deltaP `33.7561` edge `0.0399` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `3.0093` n `50` status `ready` deltaP `14.0539` edge `0.2234` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.4537` n `91` status `ready` deltaP `16.9758` edge `0.4363` maxDD `-9.4579`
- `news_risk_high->metal_24h` score `1.8727` n `91` status `ready` deltaP `21.2092` edge `0.2261` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.8351` n `91` status `ready` deltaP `20.6159` edge `0.0633` maxDD `-0.4916`
- `market_context_high->fx_1h` score `1.5154` n `50` status `ready` deltaP `21.0898` edge `0.0121` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.482` n `91` status `ready` deltaP `24.6147` edge `0.1383` maxDD `-3.9922`
- `news_risk_high->crypto_alt_4h` score `0.9174` n `104` status `ready` deltaP `6.2617` edge `0.2116` maxDD `-9.4849`
- `market_context_high->index_24h` score `0.912` n `50` status `ready` deltaP `14.7917` edge `0.0754` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

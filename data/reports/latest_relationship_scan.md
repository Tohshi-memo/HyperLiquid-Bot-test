# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T23:07:29.918220+00:00`
- Price records: `672`
- Market context records: `4667`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9870`

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

- `market_context_high->unknown_1h` score `71.032` n `145` status `ready` deltaP `9.4972` edge `5.9008` maxDD `-1.916`
- `market_context_high->unknown_4h` score `4.3718` n `145` status `ready` deltaP `10.0294` edge `0.4185` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.494` n `145` status `ready` deltaP `9.1858` edge `0.1556` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4975` n `145` status `ready` deltaP `2.1361` edge `0.0239` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5592` n `145` status `ready` deltaP `-1.879` edge `-0.0037` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.7278` n `145` status `ready` deltaP `3.8804` edge `-0.0069` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.7453` n `145` status `ready` deltaP `1.7094` edge `0.0013` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.7962` n `145` status `ready` deltaP `-1.3927` edge `0.0059` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.1731` n `145` status `ready` deltaP `2.0438` edge `0.0129` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2953` n `145` status `ready` deltaP `4.1989` edge `0.0167` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6779` n `145` status `ready` deltaP `-4.0285` edge `-0.0121` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8352` n `145` status `ready` deltaP `-3.8891` edge `-0.0724` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6527` n `145` status `ready` deltaP `13.8913` edge `0.0701` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-5.1132` n `145` status `ready` deltaP `-10.4203` edge `-0.0104` maxDD `-6.0317`
- `market_context_high->crypto_alt_1h` score `-5.2897` n `145` status `ready` deltaP `-1.3927` edge `-0.1028` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.5132` n `145` status `ready` deltaP `-5.0227` edge `-0.134` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.4461` n `145` status `ready` deltaP `-6.7541` edge `-0.038` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.0466` n `145` status `ready` deltaP `-0.3448` edge `-0.1636` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.5345` n `145` status `ready` deltaP `-3.1476` edge `-0.28` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.219` n `145` status `ready` deltaP `-2.5736` edge `-0.3268` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

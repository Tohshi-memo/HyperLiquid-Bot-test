# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T20:07:36.189318+00:00`
- Price records: `672`
- Market context records: `6013`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11122`

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

- `news_risk_high->fx_24h` score `7.6398` n `30` status `ready` deltaP `69.0972` edge `0.176` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2017` n `30` status `ready` deltaP `43.5061` edge `0.0647` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.5749` n `30` status `ready` deltaP `29.7223` edge `0.1203` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2562` n `30` status `ready` deltaP `27.0758` edge `0.0214` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.0674` n `214` status `ready` deltaP `7.0193` edge `0.1516` maxDD `-4.0887`
- `market_context_high->equity_24h` score `1.0318` n `188` status `ready` deltaP `26.5071` edge `0.4544` maxDD `-31.6107`
- `news_risk_high->crypto_major_1h` score `0.8255` n `30` status `ready` deltaP `10.3393` edge `0.0836` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2029` n `30` status `ready` deltaP `5.3194` edge `0.0367` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1327` n `30` status `ready` deltaP `9.2361` edge `0.0426` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3913` n `214` status `ready` deltaP `3.6614` edge `0.0053` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4125` n `30` status `ready` deltaP `1.3872` edge `-0.0255` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.581` n `214` status `ready` deltaP `1.6425` edge `0.0274` maxDD `-4.3608`
- `market_context_high->commodity_1h` score `-0.642` n `214` status `ready` deltaP `-1.0661` edge `0.0` maxDD `-0.7117`
- `market_context_high->fx_1h` score `-0.6986` n `214` status `ready` deltaP `-0.9304` edge `-0.0015` maxDD `-0.7077`
- `news_risk_high->index_1h` score `-1.043` n `30` status `ready` deltaP `-9.5509` edge `-0.0186` maxDD `-1.1161`
- `market_context_high->crypto_alt_1h` score `-1.0835` n `214` status `ready` deltaP `2.391` edge `0.0204` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-1.0977` n `214` status `ready` deltaP `2.6135` edge `0.0186` maxDD `-9.807`
- `market_context_high->index_24h` score `-1.121` n `188` status `ready` deltaP `3.2432` edge `0.0561` maxDD `-9.715`
- `market_context_high->index_4h` score `-1.1242` n `214` status `ready` deltaP `0.822` edge `0.0153` maxDD `-2.8591`
- `market_context_high->commodity_4h` score `-1.1262` n `214` status `ready` deltaP `-2.2538` edge `-0.0083` maxDD `-3.0181`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

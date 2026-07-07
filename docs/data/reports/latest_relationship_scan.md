# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T14:22:27.892640+00:00`
- Price records: `672`
- Market context records: `5989`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11236`

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

- `news_risk_high->fx_24h` score `7.4913` n `30` status `ready` deltaP `68.5764` edge `0.1671` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.4931` n `30` status `ready` deltaP `33.7153` edge `0.1702` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1421` n `30` status `ready` deltaP `42.8963` edge `0.0638` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2286` n `30` status `ready` deltaP `26.7764` edge `0.0211` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.0579` n `232` status `ready` deltaP `7.5747` edge `0.1471` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.785` n `30` status `ready` deltaP `9.8902` edge `0.0814` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1732` n `30` status `ready` deltaP `5.1697` edge `0.0339` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0758` n `30` status `ready` deltaP `9.2361` edge `0.0353` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4126` n `30` status `ready` deltaP `1.5369` edge `-0.0265` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.433` n `232` status `ready` deltaP `-0.9756` edge `0.0021` maxDD `-1.0884`
- `market_context_high->equity_1h` score `-0.4331` n `232` status `ready` deltaP `3.7529` edge `0.0323` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.5589` n `232` status `ready` deltaP `1.6519` edge `-0.0028` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.7778` n `232` status `ready` deltaP `-1.7293` edge `-0.0016` maxDD `-0.8015`
- `market_context_high->equity_24h` score `-0.8026` n `205` status `ready` deltaP `21.7649` edge `0.3248` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0563` n `30` status `ready` deltaP `-9.7006` edge `-0.0193` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1082` n `232` status `ready` deltaP `2.5914` edge `0.0174` maxDD `-9.807`
- `market_context_high->index_1h` score `-1.1397` n `232` status `ready` deltaP `-0.9937` edge `0.003` maxDD `-1.3078`
- `market_context_high->commodity_4h` score `-1.1877` n `232` status `ready` deltaP `-0.3943` edge `-0.0013` maxDD `-4.5336`
- `market_context_high->index_4h` score `-1.1879` n `232` status `ready` deltaP `0.1997` edge `0.0151` maxDD `-3.165`
- `market_context_high->crypto_alt_1h` score `-1.2084` n `232` status `ready` deltaP `1.5202` edge `0.0102` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

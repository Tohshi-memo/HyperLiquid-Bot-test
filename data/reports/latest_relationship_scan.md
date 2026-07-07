# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T19:53:03.328180+00:00`
- Price records: `672`
- Market context records: `6012`
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

- `news_risk_high->fx_24h` score `7.635` n `30` status `ready` deltaP `69.0972` edge `0.1756` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1883` n `30` status `ready` deltaP `43.3537` edge `0.0646` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.62` n `30` status `ready` deltaP `29.8959` edge `0.1229` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2562` n `30` status `ready` deltaP `27.0758` edge `0.0214` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.0723` n `215` status `ready` deltaP `7.0646` edge `0.1517` maxDD `-4.0887`
- `market_context_high->equity_24h` score `0.8655` n `189` status `ready` deltaP `26.1244` edge `0.4431` maxDD `-31.6107`
- `news_risk_high->crypto_major_1h` score `0.8419` n `30` status `ready` deltaP `10.489` edge `0.0847` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2192` n `30` status `ready` deltaP `5.4691` edge `0.0378` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1327` n `30` status `ready` deltaP `9.2361` edge `0.0426` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4008` n `215` status `ready` deltaP `3.5524` edge `0.0048` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4016` n `30` status `ready` deltaP `1.5369` edge `-0.0251` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.5675` n `215` status `ready` deltaP `1.8577` edge `0.0277` maxDD `-4.3608`
- `market_context_high->commodity_1h` score `-0.6473` n `215` status `ready` deltaP `-1.1468` edge `0.0001` maxDD `-0.7117`
- `market_context_high->fx_1h` score `-0.7202` n `215` status `ready` deltaP `-1.1412` edge `-0.0016` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.0337` n `30` status `ready` deltaP `-9.4012` edge `-0.0184` maxDD `-1.1161`
- `market_context_high->crypto_alt_1h` score `-1.1004` n `215` status `ready` deltaP `2.2908` edge `0.0189` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-1.1151` n `215` status `ready` deltaP `2.5045` edge `0.0171` maxDD `-9.807`
- `market_context_high->index_4h` score `-1.1296` n `215` status `ready` deltaP `0.7288` edge `0.0154` maxDD `-2.8726`
- `market_context_high->commodity_4h` score `-1.1593` n `215` status `ready` deltaP `-2.3079` edge `-0.0079` maxDD `-3.027`
- `market_context_high->index_24h` score `-1.2125` n `189` status `ready` deltaP `2.9927` edge `0.0533` maxDD `-10.2964`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

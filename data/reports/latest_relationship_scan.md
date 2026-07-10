# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T06:37:33.459061+00:00`
- Price records: `672`
- Market context records: `6258`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11082`

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

- `news_risk_high->crypto_alt_24h` score `14.5575` n `32` status `ready` deltaP `42.5514` edge `0.9442` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9837` n `32` status `ready` deltaP `50.8562` edge `0.1596` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1877` n `32` status `ready` deltaP `43.8262` edge `0.0614` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.5458` n `32` status `ready` deltaP `15.9675` edge `0.4261` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.4243` n `32` status `ready` deltaP `26.1558` edge `0.0482` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.344` n `32` status `ready` deltaP `28.1437` edge `0.0216` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.3179` n `192` status `ready` deltaP `2.7102` edge `0.2759` maxDD `-3.7317`
- `market_context_high->unknown_4h` score `1.4519` n `192` status `ready` deltaP `-0.9274` edge `0.3804` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3166` n `32` status `ready` deltaP `13.6789` edge `0.1243` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7732` n `32` status `ready` deltaP `10.4229` edge `0.0758` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1629` n `32` status `ready` deltaP `9.161` edge `0.0052` maxDD `-2.3058`
- `market_context_high->metal_24h` score `-0.2559` n `192` status `ready` deltaP `18.486` edge `0.1008` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.2933` n `192` status `ready` deltaP `1.0604` edge `-0.0001` maxDD `-0.5659`
- `market_context_high->equity_4h` score `-0.3737` n `192` status `ready` deltaP `3.5823` edge `0.0367` maxDD `-2.671`
- `market_context_high->commodity_1h` score `-0.5571` n `192` status `ready` deltaP `-0.7485` edge `0.0032` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.5656` n `192` status `ready` deltaP `3.214` edge `0.0248` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.727` n `32` status `ready` deltaP `-2.8443` edge `-0.0245` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7777` n `192` status `ready` deltaP `2.364` edge `-0.0007` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8905` n `192` status `ready` deltaP `4.6937` edge `0.0298` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9831` n `192` status `ready` deltaP `3.7831` edge `0.0255` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

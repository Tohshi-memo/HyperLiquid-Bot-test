# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T18:37:29.472818+00:00`
- Price records: `672`
- Market context records: `6007`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11142`

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

- `news_risk_high->fx_24h` score `7.5947` n `30` status `ready` deltaP `68.9236` edge `0.1734` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1725` n `30` status `ready` deltaP `43.2012` edge `0.0643` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.831` n `30` status `ready` deltaP `30.7639` edge `0.1347` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.231` n `30` status `ready` deltaP `26.7764` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1323` n `219` status `ready` deltaP `7.3804` edge `0.1546` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7842` n `30` status `ready` deltaP `10.1896` edge `0.0793` maxDD `-2.0691`
- `market_context_high->equity_24h` score `0.2638` n `193` status `ready` deltaP `24.633` edge `0.4029` maxDD `-31.6107`
- `news_risk_high->crypto_alt_1h` score `0.1826` n `30` status `ready` deltaP `5.4691` edge `0.0331` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1226` n `30` status `ready` deltaP `9.2361` edge `0.0413` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4118` n `30` status `ready` deltaP `1.5369` edge `-0.0264` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4846` n `219` status `ready` deltaP `2.5415` edge `0.0008` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5863` n `219` status `ready` deltaP `-0.6849` edge `0.0021` maxDD `-0.7117`
- `market_context_high->equity_1h` score `-0.59` n `219` status `ready` deltaP `1.9502` edge `0.0242` maxDD `-4.3608`
- `market_context_high->fx_1h` score `-0.6616` n `219` status `ready` deltaP `-0.4382` edge `-0.0014` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.0399` n `30` status `ready` deltaP `-9.4012` edge `-0.0192` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.127` n `219` status `ready` deltaP `-1.4401` edge `-0.0053` maxDD `-3.0339`
- `market_context_high->index_4h` score `-1.1501` n `219` status `ready` deltaP `0.5311` edge `0.0156` maxDD `-2.9939`
- `market_context_high->crypto_major_1h` score `-1.1942` n `219` status `ready` deltaP `2.1074` edge `0.0096` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.2238` n `219` status `ready` deltaP `1.3138` edge `0.0096` maxDD `-9.3536`
- `market_context_high->index_1h` score `-1.339` n `219` status `ready` deltaP `-3.2825` edge `0.0015` maxDD `-1.2963`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

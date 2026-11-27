# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T13:37:28.108162+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3266.9749` n `31` status `ready` deltaP `1.4825` edge `272.2556` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3169.2778` n `31` status `ready` deltaP `3.7864` edge `264.0869` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.7189` n `31` status `ready` deltaP `26.7361` edge `1.215` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.6792` n `31` status `ready` deltaP `26.2153` edge `1.0485` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.2106` n `31` status `ready` deltaP `25.8681` edge `0.8451` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.9345` n `31` status `ready` deltaP `20.5104` edge `0.6115` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.0729` n `31` status `ready` deltaP `30.3649` edge `0.3517` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.9853` n `31` status `ready` deltaP `13.1196` edge `0.6934` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.631` n `31` status `ready` deltaP `38.5865` edge `0.1415` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `4.2788` n `31` status `ready` deltaP `14.1521` edge `0.2897` maxDD `-0.1986`
- `news_risk_high->index_24h` score `2.683` n `31` status `ready` deltaP `27.7778` edge `0.0384` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.5789` n `31` status `ready` deltaP `15.9455` edge `0.1273` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.5426` n `31` status `ready` deltaP `30.06` edge `0.0375` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.3607` n `31` status `ready` deltaP `28.5494` edge `0.0149` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0082` n `31` status `ready` deltaP `6.4178` edge `0.2608` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7811` n `31` status `ready` deltaP `9.2621` edge `0.2023` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1971` n `31` status `ready` deltaP `25.5408` edge `0.0111` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3256` n `31` status `ready` deltaP `11.2903` edge `0.0222` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.082` n `31` status `ready` deltaP `7.3023` edge `0.0016` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4981` n `31` status `ready` deltaP `-3.4093` edge `0.0074` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

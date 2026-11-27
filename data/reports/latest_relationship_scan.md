# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T12:37:29.877670+00:00`
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

- `news_risk_high->unknown_1h` score `3254.2465` n `31` status `ready` deltaP `1.4825` edge `271.1949` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3179.899` n `31` status `ready` deltaP `3.7864` edge `264.972` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.2304` n `31` status `ready` deltaP `27.4306` edge `1.253` maxDD `0.0`
- `news_risk_high->equity_24h` score `15.2712` n `31` status `ready` deltaP `26.9097` edge `1.0932` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.6598` n `31` status `ready` deltaP `26.5625` edge `0.8779` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.1637` n `31` status `ready` deltaP `20.5104` edge `0.6306` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.2445` n `31` status `ready` deltaP `30.3649` edge `0.366` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1382` n `31` status `ready` deltaP `13.1196` edge `0.713` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6334` n `31` status `ready` deltaP `38.5865` edge `0.1417` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `4.4315` n `31` status `ready` deltaP `14.8466` edge `0.2978` maxDD `-0.1986`
- `news_risk_high->index_24h` score `2.7902` n `31` status `ready` deltaP `28.4722` edge `0.0427` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5606` n `31` status `ready` deltaP `30.06` edge `0.039` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.5417` n `31` status `ready` deltaP `15.9455` edge `0.1242` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3559` n `31` status `ready` deltaP `28.5494` edge `0.0145` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.9685` n `31` status `ready` deltaP `6.1184` edge `0.2577` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7624` n `31` status `ready` deltaP `9.1124` edge `0.2009` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1621` n `31` status `ready` deltaP `25.0917` edge `0.0096` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3217` n `31` status `ready` deltaP `11.2903` edge `0.0217` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0592` n `31` status `ready` deltaP `7.1499` edge `-0.0003` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5317` n `31` status `ready` deltaP `-3.7087` edge `0.0066` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

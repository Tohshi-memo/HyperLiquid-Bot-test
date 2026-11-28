# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T02:07:27.934918+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3230`

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

- `news_risk_high->unknown_1h` score `3309.6013` n `31` status `ready` deltaP `1.6322` edge `275.8068` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3173.6359` n `31` status `ready` deltaP `3.4815` edge `264.4521` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.7501` n `31` status `ready` deltaP `28.0763` edge `1.292` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.3243` n `31` status `ready` deltaP `26.3432` edge `0.8514` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.3801` n `31` status `ready` deltaP `23.9168` edge `0.7889` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.2651` n `31` status `ready` deltaP `18.8336` edge `0.5669` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.1069` n `31` status `ready` deltaP `28.5356` edge `0.2834` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.7102` n `31` status `ready` deltaP `38.6762` edge `0.1475` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.5529` n `31` status `ready` deltaP `13.7293` edge `0.6339` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.3548` n `31` status `ready` deltaP `12.1877` edge `0.2258` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.2191` n `31` status `ready` deltaP `27.621` edge `0.0268` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2133` n `31` status `ready` deltaP `27.2021` edge `0.0116` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.1843` n `31` status `ready` deltaP `14.5982` edge `0.1034` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.162` n `31` status `ready` deltaP `24.6101` edge `0.0161` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.7947` n `31` status `ready` deltaP `4.7711` edge `0.2444` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6291` n `31` status `ready` deltaP `7.9148` edge `0.1918` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1084` n `31` status `ready` deltaP `24.1935` edge `0.0087` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.35` n `31` status `ready` deltaP `8.8267` edge `0.0258` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2316` n `31` status `ready` deltaP `9.9183` edge `0.0193` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3567` n `31` status `ready` deltaP `-2.3614` edge `0.0122` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T09:52:37.152091+00:00`
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

- `news_risk_high->unknown_1h` score `3225.1573` n `31` status `ready` deltaP `1.6322` edge `268.7698` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3182.9578` n `31` status `ready` deltaP `3.7864` edge `265.2269` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `19.2972` n `31` status `ready` deltaP `29.3403` edge `1.4125` maxDD `0.0`
- `news_risk_high->equity_24h` score `17.2408` n `31` status `ready` deltaP `28.8194` edge `1.2446` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.3558` n `31` status `ready` deltaP `28.4722` edge `1.0065` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.6515` n `31` status `ready` deltaP `20.9677` edge `0.6682` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.4763` n `31` status `ready` deltaP `30.5173` edge `0.3843` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.5024` n `31` status `ready` deltaP `14.0342` edge `0.7536` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `4.9551` n `31` status `ready` deltaP `16.7563` edge `0.3287` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6322` n `31` status `ready` deltaP `38.5865` edge `0.1416` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.1182` n `31` status `ready` deltaP `30.3819` edge `0.0573` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.5657` n `31` status `ready` deltaP `16.0952` edge `0.1252` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.5628` n `31` status `ready` deltaP `29.9076` edge `0.0402` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.3966` n `31` status `ready` deltaP `28.9985` edge `0.0149` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0394` n `31` status `ready` deltaP `6.4178` edge `0.2648` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8403` n `31` status `ready` deltaP `9.5615` edge `0.2079` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1426` n `31` status `ready` deltaP `24.7923` edge `0.0091` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3665` n `31` status `ready` deltaP `11.7476` edge `0.0244` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.032` n `31` status `ready` deltaP `6.2352` edge `-0.0059` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6683` n `31` status `ready` deltaP `-4.9063` edge `0.0032` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

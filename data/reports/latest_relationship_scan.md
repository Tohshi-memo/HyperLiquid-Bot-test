# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T22:07:31.439626+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2814`

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

- `news_risk_high->unknown_1h` score `3302.2057` n `31` status `ready` deltaP `1.6322` edge `275.1905` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3175.4373` n `31` status `ready` deltaP `3.3191` edge `264.6033` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.211` n `31` status `ready` deltaP `27.383` edge `1.2517` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.4392` n `31` status `ready` deltaP `27.2097` edge `0.8552` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.2045` n `31` status `ready` deltaP `23.9168` edge `0.8576` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2423` n `31` status `ready` deltaP `21.0438` edge `0.6336` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4895` n `31` status `ready` deltaP `29.8375` edge `0.3066` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1569` n `31` status `ready` deltaP `14.4105` edge `0.7068` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6718` n `31` status `ready` deltaP `38.6762` edge `0.1443` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.626` n `31` status `ready` deltaP `12.1877` edge `0.2484` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3462` n `31` status `ready` deltaP `28.9243` edge `0.0287` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2481` n `31` status `ready` deltaP `27.6512` edge `0.0115` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2274` n `31` status `ready` deltaP `15.197` edge `0.103` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.2064` n `31` status `ready` deltaP `24.6101` edge `0.0198` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.924` n `31` status `ready` deltaP `6.2681` edge `0.251` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6953` n `31` status `ready` deltaP `8.5136` edge `0.1963` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1325` n `31` status `ready` deltaP `24.6426` edge `0.0088` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4203` n `31` status `ready` deltaP `10.1193` edge `0.0262` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3617` n `31` status `ready` deltaP `11.6708` edge `0.0243` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3256` n `31` status `ready` deltaP `-1.9123` edge `0.0118` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

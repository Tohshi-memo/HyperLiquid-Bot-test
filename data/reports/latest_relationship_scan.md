# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T04:22:27.256615+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3552`

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

- `news_risk_high->unknown_1h` score `3220.0453` n `31` status `ready` deltaP `1.6322` edge `268.3438` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3191.0182` n `31` status `ready` deltaP `3.7864` edge `265.8986` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.2012` n `31` status `ready` deltaP `33.1597` edge `1.7957` maxDD `0.0`
- `news_risk_high->equity_24h` score `21.5759` n `31` status `ready` deltaP `32.6389` edge `1.5804` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.4521` n `31` status `ready` deltaP `32.2917` edge `1.3224` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.2438` n `31` status `ready` deltaP `23.4067` edge `0.7013` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.5682` n `31` status `ready` deltaP `33.2612` edge `0.457` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.0184` n `31` status `ready` deltaP `16.4732` edge `0.8035` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.8641` n `31` status `ready` deltaP `20.2285` edge `0.3813` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.8035` n `31` status `ready` deltaP `40.3226` edge `0.1443` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.8149` n `31` status `ready` deltaP `34.2014` edge `0.0899` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.7444` n `31` status `ready` deltaP `16.8437` edge `0.1351` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.7424` n `31` status `ready` deltaP `31.432` edge `0.045` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.411` n `31` status `ready` deltaP `29.1482` edge `0.0151` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0503` n `31` status `ready` deltaP `6.7172` edge `0.2642` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8379` n `31` status `ready` deltaP `9.8609` edge `0.2056` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1846` n `31` status `ready` deltaP `25.6905` edge `0.0085` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4872` n `31` status `ready` deltaP `12.5098` edge `0.0348` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.064` n `31` status `ready` deltaP `7.3023` edge `-0.0007` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.582` n `31` status `ready` deltaP `-4.1578` edge `0.0054` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

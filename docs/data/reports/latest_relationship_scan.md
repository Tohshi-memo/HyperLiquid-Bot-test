# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T14:37:31.697323+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7782`

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

- `news_risk_high->unknown_24h` score `1807.3128` n `139` status `ready` deltaP `1.2153` edge `150.6013` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.1149` n `139` status `ready` deltaP `21.8238` edge `0.8426` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `4.4479` n `139` status `ready` deltaP `17.7757` edge `0.6956` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `4.0514` n `139` status `ready` deltaP `21.248` edge `0.4516` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.7873` n `139` status `ready` deltaP `26.8798` edge `0.1226` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.9516` n `139` status `ready` deltaP `23.5151` edge `0.1668` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.6357` n `139` status `ready` deltaP `20.4749` edge `0.1853` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.6338` n `139` status `ready` deltaP `7.1673` edge `0.0961` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.4452` n `139` status `ready` deltaP `6.6689` edge `0.2586` maxDD `-15.9436`
- `news_risk_high->equity_1h` score `0.4097` n `139` status `ready` deltaP `6.6558` edge `0.0559` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.3868` n `139` status `ready` deltaP `8.0031` edge `0.0079` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.3557` n `139` status `ready` deltaP `4.8287` edge `0.0235` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.546` n `139` status `ready` deltaP `1.1911` edge `0.0095` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6558` n `139` status `ready` deltaP `-0.0022` edge `0.0442` maxDD `-7.2607`
- `news_risk_high->fx_4h` score `-1.1534` n `139` status `ready` deltaP `11.2015` edge `-0.0012` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.1555` n `139` status `ready` deltaP `-8.6687` edge `-0.0023` maxDD `-1.0436`
- `news_risk_high->metal_4h` score `-1.57` n `139` status `ready` deltaP `-11.1379` edge `0.0224` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0287` n `139` status `ready` deltaP `-11.7165` edge `-0.0145` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1404` n `139` status `ready` deltaP `-6.7677` edge `0.0422` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0343` n `139` status `ready` deltaP `-12.6941` edge `-0.0097` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

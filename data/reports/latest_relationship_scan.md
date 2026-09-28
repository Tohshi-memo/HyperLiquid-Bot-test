# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T15:07:32.803457+00:00`
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

- `news_risk_high->unknown_24h` score `2167.8384` n `139` status `ready` deltaP `1.2153` edge `180.6451` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.286` n `139` status `ready` deltaP `21.9974` edge `0.8557` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `4.6017` n `139` status `ready` deltaP `18.123` edge `0.7061` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `4.2699` n `139` status `ready` deltaP `21.5952` edge `0.4675` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.8391` n `139` status `ready` deltaP `27.227` edge `0.1246` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `2.0408` n `139` status `ready` deltaP `23.82` edge `0.1722` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.6825` n `139` status `ready` deltaP `20.4749` edge `0.1892` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.6854` n `139` status `ready` deltaP `7.1673` edge `0.1004` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.4781` n `139` status `ready` deltaP `6.9552` edge `0.0596` maxDD `-1.957`
- `news_risk_high->crypto_alt_4h` score `0.4536` n `139` status `ready` deltaP `6.6689` edge `0.2593` maxDD `-15.9436`
- `news_risk_high->index_1h` score `0.4192` n `139` status `ready` deltaP `8.3025` edge `0.0086` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.3193` n `139` status `ready` deltaP `5.1336` edge `0.0245` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5136` n `139` status `ready` deltaP `1.4905` edge `0.0102` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6191` n `139` status `ready` deltaP `0.1475` edge `0.0479` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.164` n `139` status `ready` deltaP `-8.8184` edge `-0.0024` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1701` n `139` status `ready` deltaP `10.8966` edge `-0.0013` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5559` n `139` status `ready` deltaP `-10.9854` edge `0.0232` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.042` n `139` status `ready` deltaP `-11.8662` edge `-0.0152` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1122` n `139` status `ready` deltaP `-6.6152` edge `0.0448` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0185` n `139` status `ready` deltaP `-12.5417` edge `-0.0094` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

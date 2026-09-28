# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T09:37:31.859430+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7886`

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

- `news_risk_high->unknown_24h` score `879.1596` n `139` status `ready` deltaP `1.2153` edge `73.2552` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.29` n `139` status `ready` deltaP `18.8724` edge `0.7102` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `2.5537` n `139` status `ready` deltaP `14.3035` edge `0.5609` maxDD `-26.1424`
- `news_risk_high->index_24h` score `2.2983` n `139` status `ready` deltaP `23.4075` edge `0.105` maxDD `-2.2287`
- `news_risk_high->equity_24h` score `2.2124` n `139` status `ready` deltaP `17.7757` edge `0.3215` maxDD `-11.1179`
- `news_risk_high->equity_4h` score `1.4679` n `139` status `ready` deltaP `21.5334` edge `0.1397` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.2882` n `139` status `ready` deltaP `20.3013` edge `0.1575` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.6256` n `139` status `ready` deltaP `6.9738` edge `0.2716` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.5991` n `139` status `ready` deltaP `6.8679` edge `0.0952` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.3425` n `139` status `ready` deltaP `6.5061` edge `0.0513` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.2898` n `139` status `ready` deltaP `6.9552` edge `0.0068` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.529` n `139` status `ready` deltaP `3.4568` edge `0.0182` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5591` n `139` status `ready` deltaP `1.0414` edge `0.0094` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.7197` n `139` status `ready` deltaP `-0.7507` edge `0.041` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1648` n `139` status `ready` deltaP `-8.8184` edge `-0.0025` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2088` n `139` status `ready` deltaP `10.2869` edge `-0.0022` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5243` n `139` status `ready` deltaP `-10.5281` edge `0.0242` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.01` n `139` status `ready` deltaP `-11.4171` edge `-0.0141` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1891` n `139` status `ready` deltaP `-7.225` edge `0.039` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.837` n `139` status `ready` deltaP `-11.3222` edge `-0.0024` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

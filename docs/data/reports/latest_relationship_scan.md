# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T16:52:28.952969+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7792`

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

- `news_risk_high->unknown_24h` score `2678.6112` n `139` status `ready` deltaP `1.2153` edge `223.2095` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.9736` n `139` status `ready` deltaP `23.2127` edge `0.9049` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `5.0901` n `139` status `ready` deltaP `19.3382` edge `0.7387` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `4.9456` n `139` status `ready` deltaP `22.8105` edge `0.5157` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.9999` n `139` status `ready` deltaP `28.4423` edge `0.1299` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `2.281` n `139` status `ready` deltaP `24.887` edge `0.1851` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.8543` n `139` status `ready` deltaP `20.8221` edge `0.2012` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.592` n `139` status `ready` deltaP `6.9738` edge `0.2688` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.5595` n `139` status `ready` deltaP `6.7182` edge `0.0929` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.4541` n `139` status `ready` deltaP `6.9552` edge `0.0576` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4288` n `139` status `ready` deltaP `8.4522` edge `0.0084` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.2075` n `139` status `ready` deltaP `6.2007` edge `0.0267` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5711` n `139` status `ready` deltaP `0.8917` edge `0.0094` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6745` n `139` status `ready` deltaP `-0.1519` edge `0.0428` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1804` n `139` status `ready` deltaP `-9.1178` edge `-0.0025` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2049` n `139` status `ready` deltaP `10.2869` edge `-0.0017` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5093` n `139` status `ready` deltaP `-10.3757` edge `0.0251` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.9829` n `139` status `ready` deltaP `-6.0055` edge `0.0573` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0303` n `139` status `ready` deltaP `-11.8662` edge `-0.0137` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.9311` n `139` status `ready` deltaP `-11.7795` edge `-0.0072` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T17:04:08.784821+00:00`
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

- `news_risk_high->unknown_24h` score `2678.1744` n `139` status `ready` deltaP `1.2153` edge `223.1731` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.0883` n `139` status `ready` deltaP `23.3863` edge `0.9133` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `5.158` n `139` status `ready` deltaP `19.5118` edge `0.7432` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `5.0422` n `139` status `ready` deltaP `22.9841` edge `0.5226` maxDD `-11.1179`
- `news_risk_high->index_24h` score `3.0222` n `139` status `ready` deltaP `28.6159` edge `0.1306` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `2.31` n `139` status `ready` deltaP `25.0395` edge `0.1865` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.8922` n `139` status `ready` deltaP `20.9957` edge `0.2032` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.61` n `139` status `ready` deltaP `6.9738` edge `0.2703` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.5331` n `139` status `ready` deltaP `6.5685` edge `0.0917` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.4529` n `139` status `ready` deltaP `6.9552` edge `0.0575` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4288` n `139` status `ready` deltaP `8.4522` edge `0.0084` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1929` n `139` status `ready` deltaP `6.3531` edge `0.0269` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5711` n `139` status `ready` deltaP `0.8917` edge `0.0094` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6846` n `139` status `ready` deltaP `-0.3016` edge `0.0425` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1882` n `139` status `ready` deltaP `-9.2675` edge `-0.0025` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2049` n `139` status `ready` deltaP `10.2869` edge `-0.0017` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4999` n `139` status `ready` deltaP `-10.2232` edge `0.0253` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.9602` n `139` status `ready` deltaP `-5.853` edge `0.0592` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0186` n `139` status `ready` deltaP `-11.7165` edge `-0.0132` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.9129` n `139` status `ready` deltaP `-11.6271` edge `-0.0067` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

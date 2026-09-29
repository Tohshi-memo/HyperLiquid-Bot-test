# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T04:37:29.467760+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7190`

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

- `news_risk_high->unknown_24h` score `2626.3152` n `139` status `ready` deltaP `1.2153` edge `218.8515` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.78` n `139` status `ready` deltaP `31.3724` edge `1.4177` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.0519` n `139` status `ready` deltaP `30.9702` edge `0.8035` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.4946` n `139` status `ready` deltaP `26.6299` edge `0.9738` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.8806` n `139` status `ready` deltaP `35.3867` edge `0.157` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.5144` n `139` status `ready` deltaP `28.8082` edge `0.2863` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4555` n `139` status `ready` deltaP `27.1736` edge `0.1844` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.3065` n `139` status `ready` deltaP `9.2604` edge `0.3131` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7023` n `139` status `ready` deltaP `7.0176` edge `0.1028` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6015` n `139` status `ready` deltaP `8.3025` edge `0.0609` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4611` n `139` status `ready` deltaP `8.7516` edge `0.0091` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1281` n `139` status `ready` deltaP `7.2678` edge `0.0262` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5603` n `139` status `ready` deltaP `0.8917` edge `0.0103` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5996` n `139` status `ready` deltaP `0.2972` edge `0.0494` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2341` n `139` status `ready` deltaP `-10.016` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3146` n `139` status `ready` deltaP `8.7625` edge `-0.0056` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.464` n `139` status `ready` deltaP `-9.3086` edge `0.0238` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.7973` n `139` status `ready` deltaP `-5.0908` edge `0.075` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0116` n `139` status `ready` deltaP `-11.5668` edge `-0.0133` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7898` n `139` status `ready` deltaP `-11.0173` edge `-0.0005` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

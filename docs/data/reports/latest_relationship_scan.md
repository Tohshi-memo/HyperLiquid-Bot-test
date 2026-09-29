# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T02:22:26.972380+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7166`

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

- `news_risk_high->unknown_24h` score `2627.784` n `139` status `ready` deltaP `1.2153` edge `218.9739` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.3794` n `139` status `ready` deltaP `29.8099` edge `1.3114` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `8.4397` n `139` status `ready` deltaP `29.4077` edge `0.7629` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `7.7036` n `139` status `ready` deltaP `25.0674` edge `0.9183` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.7668` n `139` status `ready` deltaP `34.5186` edge `0.1533` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.2929` n `139` status `ready` deltaP `27.4194` edge `0.2771` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5239` n `139` status `ready` deltaP `27.1736` edge `0.1901` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.9791` n `139` status `ready` deltaP `8.4982` edge `0.2909` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.8018` n `139` status `ready` deltaP `7.4667` edge `0.1081` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6399` n `139` status `ready` deltaP `8.3025` edge `0.0641` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4623` n `139` status `ready` deltaP `8.7516` edge `0.0092` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1221` n `139` status `ready` deltaP `7.2678` edge `0.0267` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5208` n `139` status `ready` deltaP `1.3408` edge `0.0106` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5537` n `139` status `ready` deltaP `0.5966` edge `0.0533` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2341` n `139` status `ready` deltaP `-10.016` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3573` n `139` status `ready` deltaP `8.0003` edge `-0.006` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4461` n `139` status `ready` deltaP `-9.3086` edge `0.0261` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8992` n `139` status `ready` deltaP `-5.7006` edge `0.066` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0038` n `139` status `ready` deltaP `-11.4171` edge `-0.0133` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7254` n `139` status `ready` deltaP `-10.4075` edge `0.0008` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

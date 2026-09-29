# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T03:07:34.061161+00:00`
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

- `news_risk_high->unknown_24h` score `2627.304` n `139` status `ready` deltaP `1.2153` edge `218.9339` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.8819` n `139` status `ready` deltaP `30.3308` edge `1.3498` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `8.6338` n `139` status `ready` deltaP `29.9285` edge `0.7756` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `7.9757` n `139` status `ready` deltaP `25.5882` edge `0.9375` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.7939` n `139` status `ready` deltaP `34.6923` edge `0.1544` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.353` n `139` status `ready` deltaP `27.7666` edge `0.2798` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4987` n `139` status `ready` deltaP `27.1736` edge `0.188` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.1067` n `139` status `ready` deltaP `8.8031` edge `0.2995` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.863` n `139` status `ready` deltaP `7.7661` edge `0.1112` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6554` n `139` status `ready` deltaP `8.4522` edge `0.0644` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4755` n `139` status `ready` deltaP `8.9013` edge `0.0093` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1233` n `139` status `ready` deltaP `7.2678` edge `0.0266` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.5435` n `139` status `ready` deltaP `0.5966` edge `0.0546` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5615` n `139` status `ready` deltaP `0.8917` edge `0.0102` maxDD `-0.7016`
- `news_risk_high->fx_1h` score `-1.2341` n `139` status `ready` deltaP `-10.016` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3486` n `139` status `ready` deltaP `8.1527` edge `-0.0059` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4523` n `139` status `ready` deltaP `-9.3086` edge `0.0253` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8413` n `139` status `ready` deltaP `-5.3957` edge `0.0714` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0116` n `139` status `ready` deltaP `-11.5668` edge `-0.0133` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7242` n `139` status `ready` deltaP `-10.4075` edge `0.0009` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

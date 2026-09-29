# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T03:22:32.041231+00:00`
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

- `news_risk_high->unknown_24h` score `2627.1144` n `139` status `ready` deltaP `1.2153` edge `218.9181` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.0493` n `139` status `ready` deltaP `30.5044` edge `1.3626` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `8.6969` n `139` status `ready` deltaP `30.1021` edge `0.7797` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.0724` n `139` status `ready` deltaP `25.7618` edge `0.9444` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.7975` n `139` status `ready` deltaP `34.6923` edge `0.1547` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.3765` n `139` status `ready` deltaP `27.9402` edge `0.2806` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4927` n `139` status `ready` deltaP `27.1736` edge `0.1875` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.1537` n `139` status `ready` deltaP `8.9555` edge `0.3024` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.8594` n `139` status `ready` deltaP `7.7661` edge `0.1109` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6518` n `139` status `ready` deltaP `8.4522` edge `0.0641` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4755` n `139` status `ready` deltaP `8.9013` edge `0.0093` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1245` n `139` status `ready` deltaP `7.2678` edge `0.0265` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.5373` n `139` status `ready` deltaP `0.5966` edge `0.0554` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5735` n `139` status `ready` deltaP `0.742` edge `0.0102` maxDD `-0.7016`
- `news_risk_high->fx_1h` score `-1.2341` n `139` status `ready` deltaP `-10.016` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3399` n `139` status `ready` deltaP `8.3052` edge `-0.0058` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4539` n `139` status `ready` deltaP `-9.3086` edge `0.0251` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8224` n `139` status `ready` deltaP `-5.2433` edge `0.0728` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0124` n `139` status `ready` deltaP `-11.5668` edge `-0.0134` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7254` n `139` status `ready` deltaP `-10.4075` edge `0.0008` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

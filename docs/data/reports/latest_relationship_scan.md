# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T16:22:30.521303+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7160`

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

- `news_risk_high->unknown_24h` score `2584.5432` n `139` status `ready` deltaP `1.2153` edge `215.3705` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.3138` n `139` status `ready` deltaP `31.7196` edge `1.5432` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.0663` n `139` status `ready` deltaP `34.0952` edge `0.8672` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.0605` n `139` status `ready` deltaP `24.8938` edge `0.9492` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.175` n `139` status `ready` deltaP `38.5117` edge `0.1607` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.7678` n `139` status `ready` deltaP `31.586` edge `0.2889` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.7978` n `142` status `ready` deltaP `28.4374` edge `0.2045` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.3017` n `142` status `ready` deltaP `9.3954` edge `0.3118` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.9156` n `142` status `ready` deltaP `7.4197` edge `0.1179` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6554` n `142` status `ready` deltaP `7.8519` edge `0.0684` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4958` n `142` status `ready` deltaP `8.8998` edge `0.011` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.1158` n `142` status `ready` deltaP `9.5972` edge `0.031` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2964` n `142` status `ready` deltaP `2.7389` edge `0.072` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5181` n `142` status `ready` deltaP `1.0141` edge `0.013` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2737` n `142` status `ready` deltaP `-7.2397` edge `0.0344` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.2858` n `142` status `ready` deltaP `9.4362` edge `-0.0064` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.6282` n `142` status `ready` deltaP `-4.073` edge `0.0899` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8193` n `142` status `ready` deltaP `-8.9947` edge `-0.0036` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.904` n `142` status `ready` deltaP `-9.9034` edge `-0.0106` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3536` n `142` status `ready` deltaP `-9.6122` edge `0.0042` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

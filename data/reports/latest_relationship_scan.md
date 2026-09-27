# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T21:52:28.497075+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7936`

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

- `news_risk_high->unknown_24h` score `720.2124` n `136` status `ready` deltaP `1.2153` edge `60.0096` maxDD `0.0`
- `news_risk_high->index_24h` score `1.3264` n `136` status `ready` deltaP `17.5143` edge `0.0633` maxDD `-2.2287`
- `news_risk_high->crypto_alt_24h` score `1.1502` n `136` status `ready` deltaP `14.6446` edge `0.3934` maxDD `-29.2814`
- `news_risk_high->metal_24h` score `0.822` n `136` status `ready` deltaP `19.4241` edge `0.1245` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `-0.0771` n `139` status `ready` deltaP `15.4358` edge `0.0516` maxDD `-9.2079`
- `news_risk_high->index_1h` score `-0.0959` n `139` status `ready` deltaP `2.6139` edge `0.0036` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0965` n `139` status `ready` deltaP `4.323` edge `0.0542` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.2904` n `139` status `ready` deltaP `2.6139` edge `0.0245` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.7353` n `139` status `ready` deltaP `-0.3059` edge `0.0037` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.0341` n `139` status `ready` deltaP `13.0308` edge `0.0019` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.062` n `139` status `ready` deltaP `-7.022` edge `-0.0013` maxDD `-1.0436`
- `news_risk_high->equity_24h` score `-1.1223` n `136` status `ready` deltaP `11.8975` edge `0.0828` maxDD `-11.1179`
- `news_risk_high->crypto_major_1h` score `-1.1686` n `139` status `ready` deltaP `-4.1938` edge `0.0064` maxDD `-7.2607`
- `news_risk_high->index_4h` score `-1.2134` n `139` status `ready` deltaP `-3.403` edge `0.0069` maxDD `-1.493`
- `news_risk_high->crypto_alt_4h` score `-1.8177` n `139` status `ready` deltaP `1.3336` edge `0.1056` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.8891` n `139` status `ready` deltaP `-14.0342` edge `0.0008` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9096` n `139` status `ready` deltaP `-9.9201` edge `-0.0112` maxDD `-3.3986`
- `news_risk_high->crypto_major_24h` score `-3.1348` n `136` status `ready` deltaP `8.2516` edge `0.1272` maxDD `-26.1424`
- `news_risk_high->crypto_major_4h` score `-3.573` n `139` status `ready` deltaP `-13.0177` edge `-0.0998` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6454` n `139` status `ready` deltaP `-9.7978` edge `0.0034` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

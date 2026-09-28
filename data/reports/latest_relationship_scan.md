# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T02:37:26.997775+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7628`

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

- `news_risk_high->unknown_24h` score `591.246` n `139` status `ready` deltaP `1.2153` edge `49.2624` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `1.9395` n `139` status `ready` deltaP `14.0113` edge `0.4634` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.5974` n `139` status `ready` deltaP `18.5464` edge `0.079` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.885` n `139` status `ready` deltaP `20.3013` edge `0.1239` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.3574` n `139` status `ready` deltaP `17.4175` edge `0.0746` maxDD `-9.2079`
- `news_risk_high->index_1h` score `0.0311` n `139` status `ready` deltaP `3.9612` edge `0.0052` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `0.0307` n `139` status `ready` deltaP `4.6224` edge `0.0628` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.0255` n `139` status `ready` deltaP `4.1109` edge `0.0366` maxDD `-1.957`
- `news_risk_high->equity_24h` score `-0.1865` n `139` status `ready` deltaP `12.9146` edge `0.154` maxDD `-11.1179`
- `news_risk_high->metal_1h` score `-0.6334` n `139` status `ready` deltaP `0.4426` edge `0.0072` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.9605` n `139` status `ready` deltaP `-0.8115` edge `0.0107` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-1.0119` n `139` status `ready` deltaP `-2.8465` edge `0.0175` maxDD `-7.2607`
- `news_risk_high->fx_4h` score `-1.1329` n `139` status `ready` deltaP `11.5064` edge `-0.0006` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.15` n `139` status `ready` deltaP `-8.519` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->crypto_major_24h` score `-1.2348` n `139` status `ready` deltaP `9.4424` edge `0.2776` maxDD `-26.1424`
- `news_risk_high->crypto_alt_4h` score `-1.4065` n `139` status `ready` deltaP `2.858` edge `0.1297` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.7871` n `139` status `ready` deltaP `-13.272` edge `0.0088` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9695` n `139` status `ready` deltaP `-10.968` edge `-0.0119` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.3337` n `139` status `ready` deltaP `-11.3408` edge `-0.0803` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.5508` n `139` status `ready` deltaP `-9.0356` edge `0.0062` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

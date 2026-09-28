# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T02:07:30.834876+00:00`
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

- `news_risk_high->unknown_24h` score `591.2796` n `139` status `ready` deltaP `1.2153` edge `49.2652` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `1.7125` n `139` status `ready` deltaP `13.6641` edge `0.4468` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.5432` n `139` status `ready` deltaP `18.1992` edge `0.0768` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.8598` n `139` status `ready` deltaP `20.3013` edge `0.1218` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.285` n `139` status `ready` deltaP `17.1127` edge `0.0706` maxDD `-9.2079`
- `news_risk_high->index_1h` score `0.0047` n `139` status `ready` deltaP `3.6618` edge `0.005` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0521` n `139` status `ready` deltaP `4.323` edge `0.0579` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.0722` n `139` status `ready` deltaP `3.8115` edge `0.0347` maxDD `-1.957`
- `news_risk_high->equity_24h` score `-0.3691` n `139` status `ready` deltaP `12.5674` edge `0.1411` maxDD `-11.1179`
- `news_risk_high->metal_1h` score `-0.6346` n `139` status `ready` deltaP `0.4426` edge `0.0071` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.9897` n `139` status `ready` deltaP `-1.1164` edge `0.0103` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-1.0462` n `139` status `ready` deltaP `-3.1459` edge `0.0151` maxDD `-7.2607`
- `news_risk_high->fx_4h` score `-1.1139` n `139` status `ready` deltaP `11.8113` edge `-0.0002` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.1415` n `139` status `ready` deltaP `-8.3693` edge `-0.0025` maxDD `-1.0436`
- `news_risk_high->crypto_major_24h` score `-1.5025` n `139` status `ready` deltaP `9.0952` edge `0.2576` maxDD `-26.1424`
- `news_risk_high->crypto_alt_4h` score `-1.5077` n `139` status `ready` deltaP `2.5531` edge `0.1233` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.7965` n `139` status `ready` deltaP `-13.272` edge `0.0076` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9524` n `139` status `ready` deltaP `-10.6686` edge `-0.0117` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.3768` n `139` status `ready` deltaP `-11.6457` edge `-0.0838` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.563` n `139` status `ready` deltaP `-9.188` edge `0.0062` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

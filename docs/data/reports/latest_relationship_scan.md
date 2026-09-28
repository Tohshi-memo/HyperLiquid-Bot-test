# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T12:52:29.799879+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7916`

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

- `news_risk_high->unknown_24h` score `1181.2812` n `139` status `ready` deltaP `1.2153` edge `98.432` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.5144` n `139` status `ready` deltaP `20.7821` edge `0.7995` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `3.8575` n `139` status `ready` deltaP `16.5605` edge `0.6545` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `3.3589` n `139` status `ready` deltaP `20.0327` edge `0.402` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.6133` n `139` status `ready` deltaP `25.6645` edge `0.1162` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.8092` n `139` status `ready` deltaP `22.9053` edge `0.159` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.491` n `139` status `ready` deltaP `20.3013` edge `0.1744` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.6993` n `139` status `ready` deltaP `7.4311` edge `0.2747` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.5379` n `139` status `ready` deltaP `6.7182` edge `0.0911` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.285` n `139` status `ready` deltaP `6.9552` edge `0.0064` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.2359` n `139` status `ready` deltaP `5.6079` edge `0.0484` maxDD `-1.957`
- `news_risk_high->index_4h` score `-0.404` n `139` status `ready` deltaP `4.5239` edge `0.0215` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5172` n `139` status `ready` deltaP `1.4905` edge `0.0099` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.7244` n `139` status `ready` deltaP `-0.4513` edge `0.0384` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1399` n `139` status `ready` deltaP `-8.3693` edge `-0.0023` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1534` n `139` status `ready` deltaP `11.2015` edge `-0.0012` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5456` n `139` status `ready` deltaP `-10.833` edge `0.0235` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0256` n `139` status `ready` deltaP `-11.7165` edge `-0.0141` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1131` n `139` status `ready` deltaP `-6.7677` edge `0.0457` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0755` n `139` status `ready` deltaP `-12.999` edge `-0.0111` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

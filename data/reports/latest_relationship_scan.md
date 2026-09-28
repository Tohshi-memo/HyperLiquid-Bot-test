# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T07:52:28.763930+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7886`

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

- `news_risk_high->unknown_24h` score `716.2404` n `139` status `ready` deltaP `1.2153` edge `59.6786` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `4.3312` n `139` status `ready` deltaP `17.6571` edge `0.6384` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.1315` n `139` status `ready` deltaP `22.1923` edge `0.0992` maxDD `-2.2287`
- `news_risk_high->crypto_major_24h` score `1.6453` n `139` status `ready` deltaP `13.0882` edge `0.4933` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `1.6208` n `139` status `ready` deltaP `16.5605` edge `0.2803` maxDD `-11.1179`
- `news_risk_high->equity_4h` score `1.2171` n `139` status `ready` deltaP `20.6188` edge `0.1249` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.1802` n `139` status `ready` deltaP `20.3013` edge `0.1485` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.442` n `139` status `ready` deltaP `6.1194` edge `0.0871` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.2012` n `139` status `ready` deltaP `5.9073` edge `0.0064` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.1999` n `139` status `ready` deltaP `5.4582` edge `0.0464` maxDD `-1.957`
- `news_risk_high->crypto_alt_4h` score `0.1756` n `139` status `ready` deltaP `6.0592` edge `0.2402` maxDD `-15.9436`
- `news_risk_high->metal_1h` score `-0.5472` n `139` status `ready` deltaP `1.1911` edge `0.0094` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.6324` n `139` status `ready` deltaP `2.3897` edge `0.0167` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.8007` n `139` status `ready` deltaP `-1.1998` edge `0.0336` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1671` n `139` status `ready` deltaP `-8.8184` edge `-0.0028` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2713` n `139` status `ready` deltaP `9.2198` edge `-0.0031` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.6149` n `139` status `ready` deltaP `-11.5952` edge `0.0197` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9641` n `139` status `ready` deltaP `-10.8183` edge `-0.0122` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.4083` n `139` status `ready` deltaP `-8.1396` edge `0.017` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.7036` n `139` status `ready` deltaP `-10.2551` edge `0.0016` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

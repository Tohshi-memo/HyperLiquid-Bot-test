# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T14:22:34.064495+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7776`

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

- `news_risk_high->unknown_24h` score `1626.9804` n `139` status `ready` deltaP `1.2153` edge `135.5736` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.0501` n `139` status `ready` deltaP `21.8238` edge `0.8372` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `4.3836` n `139` status `ready` deltaP `17.6021` edge `0.6914` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `3.9427` n `139` status `ready` deltaP `21.0743` edge `0.4437` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.7614` n `139` status `ready` deltaP `26.7061` edge `0.1216` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.9178` n `139` status `ready` deltaP `23.3627` edge `0.165` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.6002` n `139` status `ready` deltaP `20.3013` edge `0.1835` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.617` n `139` status `ready` deltaP `7.1673` edge `0.0947` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.4524` n `139` status `ready` deltaP `6.6689` edge `0.2592` maxDD `-15.9436`
- `news_risk_high->equity_1h` score `0.3797` n `139` status `ready` deltaP `6.5061` edge `0.0544` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.3725` n `139` status `ready` deltaP `7.8534` edge `0.0077` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.3714` n `139` status `ready` deltaP `4.6763` edge `0.0232` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5603` n `139` status `ready` deltaP `1.0414` edge `0.0093` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6644` n `139` status `ready` deltaP `-0.0022` edge `0.0431` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1555` n `139` status `ready` deltaP `-8.6687` edge `-0.0023` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1613` n `139` status `ready` deltaP `11.0491` edge `-0.0012` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5803` n `139` status `ready` deltaP `-11.2903` edge `0.0221` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0279` n `139` status `ready` deltaP `-11.7165` edge `-0.0144` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1514` n `139` status `ready` deltaP `-6.9201` edge `0.0418` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0501` n `139` status `ready` deltaP `-12.8466` edge `-0.01` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

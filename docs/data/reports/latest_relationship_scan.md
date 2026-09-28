# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T07:07:26.643781+00:00`
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

- `news_risk_high->unknown_24h` score `646.1952` n `139` status `ready` deltaP `1.2153` edge `53.8415` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `3.8791` n `139` status `ready` deltaP `17.1363` edge `0.6042` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.0586` n `139` status `ready` deltaP `21.6714` edge `0.0966` maxDD `-2.2287`
- `news_risk_high->equity_24h` score `1.3607` n `139` status `ready` deltaP `16.0396` edge `0.2621` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `1.204` n `139` status `ready` deltaP `12.5674` edge `0.46` maxDD `-26.1424`
- `news_risk_high->metal_24h` score `1.1322` n `139` status `ready` deltaP `20.3013` edge `0.1445` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `1.1061` n `139` status `ready` deltaP `20.1614` edge `0.1187` maxDD `-9.2079`
- `news_risk_high->crypto_alt_1h` score `0.3185` n `139` status `ready` deltaP `5.6703` edge `0.0798` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.1616` n `139` status `ready` deltaP `5.4582` edge `0.0061` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.1208` n `139` status `ready` deltaP `5.0091` edge `0.0428` maxDD `-1.957`
- `news_risk_high->crypto_alt_4h` score `-0.0902` n `139` status `ready` deltaP `5.6019` edge `0.2211` maxDD `-15.9436`
- `news_risk_high->metal_1h` score `-0.5963` n `139` status `ready` deltaP `0.742` edge `0.0083` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.6774` n `139` status `ready` deltaP `1.9324` edge `0.016` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.8771` n `139` status `ready` deltaP `-1.6489` edge `0.0268` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1578` n `139` status `ready` deltaP `-8.6687` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2459` n `139` status `ready` deltaP `9.6771` edge `-0.0029` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.6519` n `139` status `ready` deltaP `-12.0525` edge `0.018` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9532` n `139` status `ready` deltaP `-10.6686` edge `-0.0118` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.5678` n `139` status `ready` deltaP `-8.5969` edge `-0.0004` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6514` n `139` status `ready` deltaP `-9.7978` edge `0.0029` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

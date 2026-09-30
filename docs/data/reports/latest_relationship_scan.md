# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T01:07:28.835277+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7026`

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

- `news_risk_high->unknown_24h` score `1690.5352` n `137` status `ready` deltaP `1.9097` edge `140.8652` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5124` n `137` status `ready` deltaP `28.7447` edge `1.381` maxDD `-20.7279`
- `news_risk_high->equity_24h` score `8.6424` n `137` status `ready` deltaP `29.0691` edge `0.7613` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.6923` n `137` status `ready` deltaP `24.5552` edge `0.8284` maxDD `-18.7528`
- `news_risk_high->index_24h` score `3.7902` n `137` status `ready` deltaP `35.1531` edge `0.1423` maxDD `-1.5309`
- `news_risk_high->metal_24h` score `3.183` n `137` status `ready` deltaP `27.6967` edge `0.2452` maxDD `-5.1675`
- `news_risk_high->equity_4h` score `2.8599` n `140` status `ready` deltaP `28.9722` edge `0.2053` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.4257` n `140` status `ready` deltaP `13.1707` edge `0.3803` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.3901` n `140` status `ready` deltaP `10.3807` edge `0.1377` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7542` n `140` status `ready` deltaP `8.1223` edge `0.0714` maxDD `-1.6827`
- `news_risk_high->index_1h` score `0.482` n `140` status `ready` deltaP `8.7211` edge `0.0108` maxDD `-0.302`
- `news_risk_high->index_4h` score `0.0031` n `140` status `ready` deltaP `8.5627` edge `0.0285` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.1359` n `140` status `ready` deltaP `4.3413` edge `0.0819` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5804` n `140` status `ready` deltaP `0.2053` edge `0.0132` maxDD `-0.7016`
- `news_risk_high->crypto_major_4h` score `-1.2062` n `140` status `ready` deltaP `-1.4939` edge `0.1268` maxDD `-13.719`
- `news_risk_high->metal_4h` score `-1.3622` n `140` status `ready` deltaP `-8.4539` edge `0.0277` maxDD `-3.3454`
- `news_risk_high->fx_4h` score `-1.3961` n `140` status `ready` deltaP `7.5088` edge `-0.0077` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8573` n `140` status `ready` deltaP `-9.3798` edge `-0.0042` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8678` n `140` status `ready` deltaP `-9.4012` edge `-0.0093` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2774` n `140` status `ready` deltaP `-9.2857` edge `0.0118` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

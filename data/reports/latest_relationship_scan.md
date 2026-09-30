# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T00:52:30.833649+00:00`
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

- `news_risk_high->unknown_24h` score `1742.962` n `137` status `ready` deltaP `1.9097` edge `145.2341` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.6439` n `137` status `ready` deltaP `28.9183` edge `1.3908` maxDD `-20.7279`
- `news_risk_high->equity_24h` score `8.7115` n `137` status `ready` deltaP `29.2427` edge `0.7659` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.789` n `137` status `ready` deltaP `24.7288` edge `0.8353` maxDD `-18.7528`
- `news_risk_high->index_24h` score `3.8137` n `137` status `ready` deltaP `35.3267` edge `0.1431` maxDD `-1.5309`
- `news_risk_high->metal_24h` score `3.2173` n `137` status `ready` deltaP `27.8703` edge `0.2469` maxDD `-5.1675`
- `news_risk_high->equity_4h` score `2.8733` n `140` status `ready` deltaP `29.1246` edge `0.2054` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.3979` n `140` status `ready` deltaP `13.0183` edge `0.379` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.4237` n `140` status `ready` deltaP `10.5304` edge `0.1395` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7554` n `140` status `ready` deltaP `8.1223` edge `0.0715` maxDD `-1.6827`
- `news_risk_high->index_1h` score `0.482` n `140` status `ready` deltaP `8.7211` edge `0.0108` maxDD `-0.302`
- `news_risk_high->index_4h` score `0.0165` n `140` status `ready` deltaP `8.7152` edge `0.0286` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.1281` n `140` status `ready` deltaP `4.3413` edge `0.0829` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.578` n `140` status `ready` deltaP `0.2053` edge `0.0134` maxDD `-0.7016`
- `news_risk_high->crypto_major_4h` score `-1.222` n `140` status `ready` deltaP `-1.6463` edge `0.1258` maxDD `-13.719`
- `news_risk_high->metal_4h` score `-1.3614` n `140` status `ready` deltaP `-8.4539` edge `0.0278` maxDD `-3.3454`
- `news_risk_high->fx_4h` score `-1.3874` n `140` status `ready` deltaP `7.6612` edge `-0.0076` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8441` n `140` status `ready` deltaP `-9.2301` edge `-0.0041` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8592` n `140` status `ready` deltaP `-9.2515` edge `-0.0092` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2663` n `140` status `ready` deltaP `-9.1333` edge `0.0122` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

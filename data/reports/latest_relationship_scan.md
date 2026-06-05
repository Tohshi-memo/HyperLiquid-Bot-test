# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T07:52:21.200898+00:00`
- Price records: `672`
- Market context records: `2950`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.0464` n `132` status `ready` deltaP `14.5518` edge `1.7152` maxDD `-22.6673`
- `market_context_high->equity_24h` score `8.1302` n `132` status `ready` deltaP `18.4185` edge `0.7551` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `7.7084` n `132` status `ready` deltaP `16.7455` edge `0.5772` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `4.0154` n `132` status `ready` deltaP `20.6597` edge `0.4216` maxDD `-8.9772`
- `market_context_high->index_24h` score `3.0774` n `132` status `ready` deltaP `14.2834` edge `0.2593` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.1134` n `133` status `ready` deltaP `12.1504` edge `0.1766` maxDD `-3.852`
- `market_context_high->crypto_alt_4h` score `0.9208` n `133` status `ready` deltaP `18.5345` edge `0.4093` maxDD `-30.8239`
- `market_context_high->index_4h` score `0.7504` n `133` status `ready` deltaP `14.8141` edge `0.0816` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.4203` n `133` status `ready` deltaP `4.4196` edge `0.1109` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.1291` n `133` status `ready` deltaP `6.5474` edge `0.0223` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.0838` n `133` status `ready` deltaP `2.3491` edge `0.0528` maxDD `-2.0358`
- `market_context_high->fx_1h` score `-0.2958` n `133` status `ready` deltaP `0.3861` edge `0.0035` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.2964` n `133` status `ready` deltaP `6.2413` edge `0.0964` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.5796` n `133` status `ready` deltaP `0.8149` edge `0.009` maxDD `-3.4325`
- `market_context_high->crypto_major_1h` score `-0.6143` n `133` status `ready` deltaP `4.8737` edge `0.0757` maxDD `-9.622`
- `market_context_high->fx_4h` score `-0.7319` n `133` status `ready` deltaP `1.1072` edge `0.0095` maxDD `-0.5631`
- `market_context_high->commodity_1h` score `-0.7971` n `133` status `ready` deltaP `-2.169` edge `-0.0124` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.8738` n `133` status `ready` deltaP `1.1346` edge `-0.0073` maxDD `-3.1801`
- `market_context_high->commodity_4h` score `-0.9711` n `133` status `ready` deltaP `4.1846` edge `0.0284` maxDD `-9.1306`
- `market_context_high->crypto_major_4h` score `-1.2527` n `133` status `ready` deltaP `8.7807` edge `0.2934` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

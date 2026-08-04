# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T15:07:31.824990+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9839`

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

- `market_context_high->unknown_24h` score `33.9251` n `49` status `ready` deltaP `22.4384` edge `2.6818` maxDD `-0.0103`
- `market_context_high->commodity_24h` score `6.664` n `49` status `ready` deltaP `33.8471` edge `0.3805` maxDD `-3.0652`
- `market_context_high->crypto_alt_24h` score `6.3368` n `49` status `ready` deltaP `33.762` edge `0.3223` maxDD `-0.5453`
- `market_context_high->unknown_4h` score `5.1873` n `89` status `ready` deltaP `-0.1319` edge `0.5327` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.0547` n `89` status `ready` deltaP `14.4628` edge `0.0761` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2256` n `89` status `ready` deltaP `5.5053` edge `0.0237` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2221` n `89` status `ready` deltaP `15.8965` edge `0.0085` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1865` n `89` status `ready` deltaP `8.0536` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.501` n `89` status `ready` deltaP `1.016` edge `-0.0176` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5527` n `89` status `ready` deltaP `-1.682` edge `-0.0102` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6138` n `89` status `ready` deltaP `4.2718` edge `0.0163` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8297` n `89` status `ready` deltaP `4.6383` edge `0.0017` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.0895` n `89` status `ready` deltaP `-1.9848` edge `-0.0065` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7005` n `89` status `ready` deltaP `4.5381` edge `-0.0947` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.7239` n `49` status `ready` deltaP `-5.1126` edge `0.011` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.8638` n `89` status `ready` deltaP `-10.1261` edge `-0.046` maxDD `-4.7021`
- `market_context_high->metal_24h` score `-2.7992` n `49` status `ready` deltaP `-22.6403` edge `-0.0911` maxDD `-2.6802`
- `market_context_high->unknown_1h` score `-3.3991` n `89` status `ready` deltaP `2.8107` edge `-0.2573` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5133` n `89` status `ready` deltaP `-12.5463` edge `-0.0718` maxDD `-7.6533`
- `market_context_high->index_24h` score `-5.0838` n `49` status `ready` deltaP `-26.938` edge `-0.2527` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

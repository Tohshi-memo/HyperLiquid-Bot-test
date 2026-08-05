# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T13:07:35.789404+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11664`

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

- `market_context_high->unknown_24h` score `13.8975` n `89` status `ready` deltaP `8.5986` edge `1.1051` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3133` n `94` status `ready` deltaP `3.0034` edge `0.5223` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.7167` n `94` status `ready` deltaP `17.6375` edge `0.1101` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1295` n `89` status `ready` deltaP `27.0131` edge `0.0853` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.8729` n `89` status `ready` deltaP `1.6268` edge `0.2179` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4897` n `98` status `ready` deltaP `7.8914` edge `0.0298` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0971` n `98` status `ready` deltaP `6.9382` edge `-0.0032` maxDD `-0.7973`
- `market_context_high->fx_4h` score `-0.0008` n `94` status `ready` deltaP `11.8643` edge `0.0068` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5723` n `98` status `ready` deltaP `-2.0286` edge `-0.0104` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6831` n `98` status `ready` deltaP `-2.2608` edge `-0.0191` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9516` n `94` status `ready` deltaP `1.0314` edge `-0.0054` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9721` n `98` status `ready` deltaP `-4.5857` edge `-0.023` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.4718` n `89` status `ready` deltaP `0.6768` edge `-0.0489` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.6135` n `94` status `ready` deltaP `-1.226` edge `-0.0597` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8057` n `98` status `ready` deltaP `2.3647` edge `-0.0937` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.133` n `94` status `ready` deltaP `-12.7984` edge `-0.0627` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5404` n `89` status `ready` deltaP `-11.4759` edge `-0.0297` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.1265` n `98` status `ready` deltaP `4.7477` edge `-0.2475` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6716` n `98` status `ready` deltaP `-13.5647` edge `-0.0782` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.003` n `89` status `ready` deltaP `11.1716` edge `-0.0291` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

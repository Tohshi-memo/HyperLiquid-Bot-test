# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T21:34:58.329312+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9856`

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

- `market_context_high->unknown_24h` score `19.798` n `75` status `ready` deltaP `18.9792` edge `1.5276` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3809` n `90` status `ready` deltaP `1.7479` edge `0.5363` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5425` n `90` status `ready` deltaP `17.08` edge `0.0993` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.6654` n `75` status `ready` deltaP `-2.618` edge `0.2196` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.6079` n `75` status `ready` deltaP `19.0069` edge `0.0718` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2498` n `90` status `ready` deltaP `5.4923` edge `0.0258` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.1282` n `90` status `ready` deltaP `14.2243` edge `0.0076` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1243` n `90` status `ready` deltaP `7.3054` edge `-0.0035` maxDD `-0.7878`
- `market_context_high->crypto_alt_24h` score `-0.1866` n `75` status `ready` deltaP `5.6597` edge `0.0805` maxDD `-4.3728`
- `market_context_high->metal_1h` score `-0.5324` n `90` status `ready` deltaP `-1.4571` edge `-0.0091` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5363` n `90` status `ready` deltaP `0.4425` edge `-0.0183` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.7071` n `90` status `ready` deltaP `-2.0093` edge `-0.0062` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7346` n `90` status `ready` deltaP `2.8794` edge `0.0101` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8853` n `90` status `ready` deltaP `3.9431` edge `-0.0008` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6269` n `90` status `ready` deltaP `5.0998` edge `-0.089` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0028` n `90` status `ready` deltaP `-11.6734` edge `-0.0535` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.1425` n `75` status `ready` deltaP `-8.6389` edge `0.0024` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.3637` n `90` status `ready` deltaP `-11.2608` edge `-0.0679` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.448` n `90` status `ready` deltaP `1.8995` edge `-0.2553` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-4.0446` n `75` status `ready` deltaP `9.3542` edge `-0.0452` maxDD `-33.189`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

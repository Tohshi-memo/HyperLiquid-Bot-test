# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T07:07:31.154290+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11632`

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

- `market_context_high->unknown_24h` score `14.6996` n `88` status `ready` deltaP `12.5789` edge `1.1454` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.6393` n `90` status `ready` deltaP `2.0528` edge `0.5558` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5932` n `90` status `ready` deltaP `17.3849` edge `0.1015` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1762` n `88` status `ready` deltaP `27.7304` edge `0.0865` maxDD `-4.3126`
- `market_context_high->metal_24h` score `1.0831` n `88` status `ready` deltaP `2.0991` edge `0.2417` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.3075` n `92` status `ready` deltaP `6.0336` edge `0.027` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0735` n `90` status `ready` deltaP `13.1572` edge `0.0077` maxDD `-1.8797`
- `market_context_high->fx_1h` score `-0.0007` n `92` status `ready` deltaP `5.8514` edge `-0.0041` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.4649` n `92` status `ready` deltaP `-0.4426` edge `-0.0072` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6175` n `92` status `ready` deltaP `-0.9242` edge `-0.0196` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8317` n `90` status `ready` deltaP `2.4221` edge `0.0007` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.8664` n `92` status `ready` deltaP `-3.3325` edge `-0.0178` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.0844` n `88` status `ready` deltaP `3.567` edge `-0.0185` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.3405` n `90` status `ready` deltaP `1.504` edge `-0.0429` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8235` n `92` status `ready` deltaP `2.8639` edge `-0.0993` maxDD `-10.619`
- `market_context_high->index_24h` score `-2.054` n `88` status `ready` deltaP `-7.7178` edge `0.0076` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1162` n `90` status `ready` deltaP `-13.0454` edge `-0.0589` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.2763` n `92` status `ready` deltaP `3.0396` edge `-0.2486` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.324` n `92` status `ready` deltaP `-10.7199` edge `-0.0682` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.4291` n `88` status `ready` deltaP `7.8756` edge `-0.0806` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

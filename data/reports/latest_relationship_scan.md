# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T09:07:36.620214+00:00`
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

- `market_context_high->unknown_24h` score `14.4685` n `88` status `ready` deltaP `11.19` edge `1.1354` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4703` n `91` status `ready` deltaP `1.8461` edge `0.5431` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.6427` n `91` status `ready` deltaP `17.7634` edge `0.1031` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1687` n `88` status `ready` deltaP `27.5568` edge `0.0867` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.91` n `88` status `ready` deltaP `1.231` edge `0.2253` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.2583` n `92` status `ready` deltaP `5.5845` edge `0.0259` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.078` n `91` status `ready` deltaP `13.3041` edge `0.0073` maxDD `-1.8797`
- `market_context_high->fx_1h` score `-0.0007` n `92` status `ready` deltaP `5.8514` edge `-0.0041` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.4711` n `92` status `ready` deltaP `-0.5923` edge `-0.007` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5707` n `92` status `ready` deltaP `-0.1757` edge `-0.0186` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.8484` n `92` status `ready` deltaP `-3.1828` edge `-0.0165` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.9025` n `91` status `ready` deltaP `1.63` edge `-0.0031` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.265` n `88` status `ready` deltaP `2.1781` edge `-0.0324` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.478` n `91` status `ready` deltaP `-0.149` edge `-0.0495` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7112` n `92` status `ready` deltaP `3.7621` edge `-0.0909` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1016` n `91` status `ready` deltaP `-12.8083` edge `-0.0586` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.2472` n `88` status `ready` deltaP `-9.1067` edge `-0.0079` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.3291` n `92` status `ready` deltaP `2.5905` edge `-0.25` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3396` n `92` status `ready` deltaP `-10.8696` edge `-0.0685` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.1354` n `88` status `ready` deltaP `9.2645` edge `-0.0522` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

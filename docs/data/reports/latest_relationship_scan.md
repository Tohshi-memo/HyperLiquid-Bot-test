# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T08:37:30.944575+00:00`
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

- `market_context_high->unknown_24h` score `14.5202` n `88` status `ready` deltaP `11.5372` edge `1.1374` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.5737` n `90` status `ready` deltaP `1.4431` edge `0.5544` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5848` n `90` status `ready` deltaP `17.3849` edge `0.1008` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.168` n `88` status `ready` deltaP `27.5568` edge `0.0866` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.9366` n `88` status `ready` deltaP `1.231` edge `0.2287` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.2571` n `92` status `ready` deltaP `5.5845` edge `0.0258` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0624` n `90` status `ready` deltaP `13.0048` edge `0.0073` maxDD `-1.8797`
- `market_context_high->fx_1h` score `-0.0007` n `92` status `ready` deltaP `5.8514` edge `-0.0041` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.4742` n `92` status `ready` deltaP `-0.5923` edge `-0.0074` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5902` n `92` status `ready` deltaP `-0.4751` edge `-0.0191` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.8718` n `92` status `ready` deltaP `-3.4822` edge `-0.0175` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.912` n `90` status `ready` deltaP `1.5074` edge `-0.0035` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.2267` n `88` status `ready` deltaP `2.5253` edge `-0.0298` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.424` n `90` status `ready` deltaP `0.5894` edge `-0.0475` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7572` n `92` status `ready` deltaP `3.4627` edge `-0.0948` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0767` n `90` status `ready` deltaP `-12.4356` edge `-0.0579` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.2002` n `88` status `ready` deltaP `-8.7594` edge `-0.0042` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.3423` n `92` status `ready` deltaP `2.4408` edge `-0.2501` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3432` n `92` status `ready` deltaP `-10.8696` edge `-0.0688` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.2112` n `88` status `ready` deltaP `8.9173` edge `-0.0596` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

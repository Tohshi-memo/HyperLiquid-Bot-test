# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T22:07:30.678402+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9857`

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

- `market_context_high->unknown_24h` score `19.0602` n `77` status `ready` deltaP `18.6666` edge `1.4682` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3929` n `90` status `ready` deltaP `1.7479` edge `0.5373` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5896` n `90` status `ready` deltaP `17.3849` edge `0.1012` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8055` n `77` status `ready` deltaP `-1.5444` edge `0.2304` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7016` n `77` status `ready` deltaP `20.3575` edge `0.0748` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2797` n `90` status `ready` deltaP `5.642` edge `0.0273` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.1195` n `90` status `ready` deltaP `14.0718` edge `0.0075` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1111` n `90` status `ready` deltaP `7.1557` edge `-0.0036` maxDD `-0.7878`
- `market_context_high->crypto_alt_24h` score `-0.3414` n `77` status `ready` deltaP `5.2264` edge `0.0657` maxDD `-4.5445`
- `market_context_high->metal_1h` score `-0.5426` n `90` status `ready` deltaP `-1.6068` edge `-0.0094` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5549` n `90` status `ready` deltaP `0.1431` edge `-0.0187` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.7211` n `90` status `ready` deltaP `-2.159` edge `-0.007` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7243` n `90` status `ready` deltaP `3.0318` edge `0.0104` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.923` n `90` status `ready` deltaP `3.6382` edge `-0.0036` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6588` n `90` status `ready` deltaP `4.8004` edge `-0.0911` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0146` n `90` status `ready` deltaP `-11.8259` edge `-0.054` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.0436` n `77` status `ready` deltaP `-7.8778` edge `0.01` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.3733` n `90` status `ready` deltaP `-11.2608` edge `-0.0687` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4456` n `90` status `ready` deltaP `1.8995` edge `-0.2551` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-4.5629` n `77` status `ready` deltaP `8.2815` edge `-0.0651` maxDD `-35.6742`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

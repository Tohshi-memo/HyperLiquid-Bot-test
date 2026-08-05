# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T14:22:41.796854+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11668`

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

- `market_context_high->unknown_24h` score `13.7736` n `89` status `ready` deltaP `7.9042` edge `1.0994` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.5713` n `98` status `ready` deltaP `1.5275` edge `0.4703` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4589` n `98` status `ready` deltaP `15.751` edge `0.1012` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.0649` n `89` status `ready` deltaP `26.1451` edge `0.0828` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.8713` n `89` status `ready` deltaP `1.6268` edge `0.2177` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4173` n `100` status `ready` deltaP `7.497` edge `0.0264` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0143` n `100` status `ready` deltaP `5.9042` edge `-0.0032` maxDD `-0.7973`
- `market_context_high->fx_4h` score `-0.0822` n `98` status `ready` deltaP `10.3441` edge `0.0065` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.511` n `100` status `ready` deltaP `-1.3892` edge `-0.0068` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6803` n `100` status `ready` deltaP `-2.1317` edge `-0.0196` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.885` n `98` status `ready` deltaP `1.7266` edge `-0.0015` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-1.4731` n `100` status `ready` deltaP `-4.3952` edge `-0.0224` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.5105` n `89` status `ready` deltaP `0.5032` edge `-0.0527` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.7201` n `98` status `ready` deltaP `-2.1808` edge `-0.067` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7766` n `100` status `ready` deltaP `2.6707` edge `-0.092` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0268` n `98` status `ready` deltaP `-11.2805` edge `-0.0592` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.594` n `89` status `ready` deltaP `-11.9968` edge `-0.0331` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.0903` n `100` status `ready` deltaP `5.6048` edge `-0.2502` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5127` n `100` status `ready` deltaP `-12.2994` edge `-0.0734` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0007` n `89` status `ready` deltaP `11.1716` edge `-0.0288` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

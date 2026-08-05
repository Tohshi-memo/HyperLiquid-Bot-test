# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T17:22:50.099762+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `13.2318` n `90` status `ready` deltaP `6.007` edge `1.0669` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.151` n `100` status `ready` deltaP `0.8049` edge `0.4401` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4509` n `100` status `ready` deltaP `15.7256` edge `0.1007` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.95` n `90` status `ready` deltaP `2.0139` edge `0.2252` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.9477` n `90` status `ready` deltaP `24.8959` edge `0.0761` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4741` n `106` status `ready` deltaP `7.9511` edge `0.0281` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0063` n `106` status `ready` deltaP `5.7508` edge `-0.0028` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0625` n `100` status `ready` deltaP `10.5732` edge `0.0075` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5734` n `106` status `ready` deltaP `-2.4093` edge `-0.008` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7628` n `100` status `ready` deltaP `2.7866` edge `0.0071` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.7686` n `106` status `ready` deltaP `-3.8159` edge `-0.0197` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.4094` n `90` status `ready` deltaP `0.9027` edge `-0.0424` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.4568` n `106` status `ready` deltaP `-4.5814` edge `-0.0198` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7626` n `106` status `ready` deltaP `2.0846` edge `-0.0863` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0659` n `100` status `ready` deltaP `-11.8232` edge `-0.0606` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5272` n `90` status `ready` deltaP `-11.5973` edge `-0.0272` maxDD `-7.8922`
- `market_context_high->crypto_alt_4h` score `-2.5911` n `100` status `ready` deltaP `-1.5061` edge `-0.0669` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.342` n `106` status `ready` deltaP `-11.2756` edge `-0.066` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4826` n `106` status `ready` deltaP `2.6212` edge `-0.263` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0374` n `90` status `ready` deltaP `10.8334` edge `-0.0248` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

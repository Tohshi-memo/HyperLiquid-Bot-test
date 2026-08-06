# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T00:22:28.883638+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `market_context_high->unknown_24h` score `12.658` n `90` status `ready` deltaP `4.4445` edge `1.0295` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.8847` n `109` status `ready` deltaP `-2.26` edge `0.355` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1962` n `109` status `ready` deltaP `14.0566` edge `0.0906` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8571` n `90` status `ready` deltaP `2.0139` edge `0.2133` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7994` n `90` status `ready` deltaP `24.5486` edge `0.0594` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4371` n `109` status `ready` deltaP `7.9094` edge `0.0253` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0164` n `109` status `ready` deltaP `5.8328` edge `-0.0025` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1375` n `109` status `ready` deltaP `9.0093` edge `0.0083` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5253` n `109` status `ready` deltaP `-1.5602` edge `-0.0075` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7556` n `109` status `ready` deltaP `-3.5063` edge `-0.0201` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7981` n `109` status `ready` deltaP `2.6321` edge `0.0036` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.305` n `90` status `ready` deltaP `0.5555` edge `-0.0267` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5241` n `109` status `ready` deltaP `-4.9882` edge `-0.0227` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.826` n `109` status `ready` deltaP `1.1194` edge `-0.088` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.9644` n `90` status `ready` deltaP `-6.9098` edge `0.0137` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1707` n `109` status `ready` deltaP `-13.5825` edge `-0.0623` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1891` n `109` status `ready` deltaP `0.7747` edge `-0.0486` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.3559` n `109` status `ready` deltaP `-11.4487` edge `-0.066` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4852` n `109` status `ready` deltaP `1.5835` edge `-0.2563` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0848` n `90` status `ready` deltaP `10.3125` edge `-0.0274` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

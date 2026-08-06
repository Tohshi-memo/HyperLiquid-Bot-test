# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T03:37:33.385161+00:00`
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

- `market_context_high->unknown_24h` score `12.4132` n `90` status `ready` deltaP `4.4445` edge `1.0091` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `3.9536` n `109` status `ready` deltaP `-1.4978` edge `0.439` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2492` n `109` status `ready` deltaP `14.209` edge `0.094` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.7713` n `90` status `ready` deltaP `2.0139` edge `0.2023` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7336` n `90` status `ready` deltaP `23.8542` edge `0.0556` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4263` n `109` status `ready` deltaP `7.9094` edge `0.0244` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.032` n `109` status `ready` deltaP `5.9825` edge `-0.0022` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1414` n `109` status `ready` deltaP `9.0093` edge `0.0078` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5666` n `109` status `ready` deltaP `-2.159` edge `-0.0088` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7354` n `109` status `ready` deltaP `-3.2069` edge `-0.0195` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.98` n `109` status `ready` deltaP `0.6504` edge `-0.0065` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.3007` n `90` status `ready` deltaP `0.3819` edge `-0.025` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.4558` n `109` status `ready` deltaP `-4.8385` edge `-0.018` maxDD `-3.0178`
- `market_context_high->index_24h` score `-1.61` n `90` status `ready` deltaP `-4.6528` edge `0.0441` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.8463` n `109` status `ready` deltaP `1.1194` edge `-0.0906` maxDD `-10.619`
- `market_context_high->crypto_alt_4h` score `-2.1479` n `109` status `ready` deltaP `1.0796` edge `-0.0472` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1628` n `109` status `ready` deltaP `-13.43` edge `-0.0623` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.2525` n `109` status `ready` deltaP `2.1823` edge `-0.2409` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.2959` n `109` status `ready` deltaP `-11.4487` edge `-0.061` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.1549` n `90` status `ready` deltaP `9.4445` edge `-0.0306` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

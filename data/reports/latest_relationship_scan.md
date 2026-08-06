# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T00:52:27.417965+00:00`
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

- `market_context_high->unknown_24h` score `12.6172` n `90` status `ready` deltaP `4.4445` edge `1.0261` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.8907` n `109` status `ready` deltaP `-2.26` edge `0.3555` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2096` n `109` status `ready` deltaP `14.209` edge `0.0907` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8462` n `90` status `ready` deltaP `2.0139` edge `0.2119` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7947` n `90` status `ready` deltaP `24.5486` edge `0.0588` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4503` n `109` status `ready` deltaP `8.0591` edge `0.0254` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0428` n `109` status `ready` deltaP `6.1322` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1375` n `109` status `ready` deltaP `9.0093` edge `0.0083` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5245` n `109` status `ready` deltaP `-1.5602` edge `-0.0074` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.733` n `109` status `ready` deltaP `-3.2069` edge `-0.0192` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8241` n `109` status `ready` deltaP `2.3272` edge `0.0023` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.3073` n `90` status `ready` deltaP `0.5555` edge `-0.027` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5169` n `109` status `ready` deltaP `-4.9882` edge `-0.0221` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7832` n `109` status `ready` deltaP `1.4188` edge `-0.0845` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.9082` n `90` status `ready` deltaP `-6.5625` edge `0.0186` maxDD `-7.8922`
- `market_context_high->crypto_alt_4h` score `-2.1503` n `109` status `ready` deltaP `1.0796` edge `-0.0474` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1596` n `109` status `ready` deltaP `-13.43` edge `-0.0619` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3257` n `109` status `ready` deltaP `1.8829` edge `-0.245` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3643` n `109` status `ready` deltaP `-11.5984` edge `-0.0657` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0597` n `90` status `ready` deltaP `10.6598` edge `-0.0265` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

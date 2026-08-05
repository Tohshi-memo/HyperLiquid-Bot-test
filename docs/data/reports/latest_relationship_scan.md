# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T22:22:26.204762+00:00`
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

- `market_context_high->unknown_24h` score `12.8152` n `90` status `ready` deltaP `4.4445` edge `1.0426` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.8811` n `109` status `ready` deltaP `-2.26` edge `0.3547` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2106` n `109` status `ready` deltaP `14.0566` edge `0.0918` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9008` n `90` status `ready` deltaP `2.0139` edge `0.2189` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.8458` n `90` status `ready` deltaP `24.7223` edge `0.0642` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.412` n `109` status `ready` deltaP `7.61` edge `0.0252` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0931` n `109` status `ready` deltaP `6.731` edge `-0.0021` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0702` n `109` status `ready` deltaP `10.2288` edge `0.0088` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.4856` n `109` status `ready` deltaP `-0.9614` edge `-0.0064` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7517` n `109` status `ready` deltaP `3.0894` edge `0.0065` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.7915` n `109` status `ready` deltaP `-4.1051` edge `-0.0207` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.3424` n `90` status `ready` deltaP `0.5555` edge `-0.0315` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.4978` n `109` status `ready` deltaP `-4.6888` edge `-0.0225` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8642` n `109` status `ready` deltaP `0.82` edge `-0.0909` maxDD `-10.619`
- `market_context_high->index_24h` score `-2.1498` n `90` status `ready` deltaP `-8.2987` edge `-0.0008` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.2251` n `109` status `ready` deltaP `-14.3447` edge `-0.0642` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.3738` n `109` status `ready` deltaP `-0.1399` edge `-0.0579` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.3319` n `109` status `ready` deltaP `-11.1493` edge `-0.066` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.5608` n `109` status `ready` deltaP `1.5835` edge `-0.2626` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0954` n `90` status `ready` deltaP `10.1389` edge `-0.0276` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

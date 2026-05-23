# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T21:37:16.224352+00:00`
- Price records: `672`
- Market context records: `1670`
- Flow alert records: `6715`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `9.5511` n `163` status `ready` deltaP `28.3238` edge `0.8497` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.9714` n `195` status `ready` deltaP `22.8901` edge `0.5281` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8319` n `163` status `ready` deltaP `19.9089` edge `0.3244` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.087` n `195` status `ready` deltaP `18.9955` edge `0.4015` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.252` n `195` status `ready` deltaP `13.2028` edge `0.2091` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8295` n `163` status `ready` deltaP `19.185` edge `0.5144` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7278` n `206` status `ready` deltaP `6.4517` edge `0.12` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.5855` n `163` status `ready` deltaP `25.9654` edge `1.0566` maxDD `-88.8062`
- `market_context_high->crypto_major_24h` score `0.4029` n `163` status `ready` deltaP `25.1152` edge `0.7428` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.1322` n `206` status `ready` deltaP `3.3806` edge `0.0473` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.1904` n `195` status `ready` deltaP `3.8751` edge `0.0672` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.2902` n `206` status `ready` deltaP `4.0652` edge `0.0761` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.4247` n `163` status `ready` deltaP `6.9024` edge `0.0235` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6137` n `206` status `ready` deltaP `-0.2805` edge `0.0139` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8245` n `206` status `ready` deltaP `-0.4171` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-1.0223` n `195` status `ready` deltaP `10.4847` edge `0.1141` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-1.0662` n `206` status `ready` deltaP `5.1494` edge `0.0104` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.2595` n `195` status `ready` deltaP `-8.3224` edge `-0.0131` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.2488` n `206` status `ready` deltaP `-1.3836` edge `-0.0344` maxDD `-14.9083`
- `market_context_high->unknown_24h` score `-2.5997` n `163` status `ready` deltaP `10.3604` edge `0.263` maxDD `-35.8966`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

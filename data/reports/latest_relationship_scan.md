# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T21:37:28.903420+00:00`
- Price records: `672`
- Market context records: `8027`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11832`

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

- `market_context_high->equity_24h` score `16.4749` n `86` status `ready` deltaP `26.4842` edge `1.3199` maxDD `-5.8845`
- `market_context_high->metal_24h` score `7.928` n `86` status `ready` deltaP `35.8752` edge `0.4215` maxDD `0.0`
- `market_context_high->equity_4h` score `6.3812` n `99` status `ready` deltaP `24.8928` edge `0.4551` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.1714` n `86` status `ready` deltaP `24.8015` edge `0.2269` maxDD `-6.2367`
- `market_context_high->metal_4h` score `2.625` n `99` status `ready` deltaP `23.5783` edge `0.1238` maxDD `-0.979`
- `market_context_high->index_4h` score `2.5355` n `99` status `ready` deltaP `26.4425` edge `0.071` maxDD `-0.8791`
- `market_context_high->index_24h` score `1.9199` n `86` status `ready` deltaP `10.6525` edge `0.156` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6961` n `99` status `ready` deltaP `13.9343` edge `0.1302` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.4114` n `86` status `ready` deltaP `25.6862` edge `0.0375` maxDD `-2.2901`
- `market_context_high->index_1h` score `0.8584` n `99` status `ready` deltaP `13.9721` edge `0.0214` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.7628` n `99` status `ready` deltaP `10.6802` edge `0.0302` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.6027` n `99` status `ready` deltaP `9.0494` edge `0.1617` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.5878` n `99` status `ready` deltaP `5.7147` edge `0.1226` maxDD `-3.9374`
- `market_context_high->crypto_major_1h` score `0.5834` n `99` status `ready` deltaP `11.3168` edge `0.0404` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `0.0164` n `99` status `ready` deltaP `1.7027` edge `0.034` maxDD `-1.4603`
- `market_context_high->fx_4h` score `-0.4992` n `99` status `ready` deltaP `4.5247` edge `0.003` maxDD `-0.9813`
- `market_context_high->fx_1h` score `-0.5409` n `99` status `ready` deltaP `-1.2521` edge `0.0` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.6576` n `99` status `ready` deltaP `-2.3392` edge `-0.0064` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.2454` n `99` status `ready` deltaP `-0.1937` edge `-0.0082` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.8352` n `99` status `ready` deltaP `7.6514` edge `-0.1616` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

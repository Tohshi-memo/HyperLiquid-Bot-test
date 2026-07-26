# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T21:22:27.999540+00:00`
- Price records: `672`
- Market context records: `8026`
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

- `market_context_high->equity_24h` score `16.2003` n `87` status `ready` deltaP `25.7754` edge `1.307` maxDD `-5.9718`
- `market_context_high->metal_24h` score `7.8788` n `87` status `ready` deltaP `35.8752` edge `0.4174` maxDD `0.0`
- `market_context_high->equity_4h` score `6.3586` n `100` status `ready` deltaP `25.0746` edge `0.452` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `2.9583` n `87` status `ready` deltaP `23.9327` edge `0.2191` maxDD `-6.2367`
- `market_context_high->metal_4h` score `2.5425` n `100` status `ready` deltaP `22.9224` edge `0.1213` maxDD `-0.979`
- `market_context_high->index_4h` score `2.5255` n `100` status `ready` deltaP `26.4216` edge `0.0703` maxDD `-0.8791`
- `market_context_high->index_24h` score `1.95` n `87` status `ready` deltaP `11.1337` edge `0.1553` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.7135` n `100` status `ready` deltaP `14.2575` edge `0.1295` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3418` n `87` status `ready` deltaP `25.2714` edge `0.0363` maxDD `-2.4366`
- `market_context_high->index_1h` score `0.8851` n `100` status `ready` deltaP `14.3054` edge `0.0214` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.7186` n `100` status `ready` deltaP `10.2036` edge `0.0297` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.6458` n `100` status `ready` deltaP `9.4231` edge `0.1628` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.6249` n `100` status `ready` deltaP `6.1187` edge `0.123` maxDD `-3.9374`
- `market_context_high->crypto_major_1h` score `0.6159` n `100` status `ready` deltaP `11.7006` edge `0.042` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `0.0538` n `100` status `ready` deltaP `2.1976` edge `0.0355` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.3271` n `100` status `ready` deltaP `-0.8563` edge `0.0005` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4508` n `100` status `ready` deltaP `5.1005` edge `0.0032` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.6358` n `100` status `ready` deltaP `-1.994` edge `-0.0059` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.2646` n `100` status `ready` deltaP `-0.5769` edge `-0.0081` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.8212` n `100` status `ready` deltaP `7.9461` edge `-0.1624` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

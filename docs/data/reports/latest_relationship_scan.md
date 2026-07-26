# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T20:52:28.084440+00:00`
- Price records: `672`
- Market context records: `8023`
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

- `market_context_high->equity_24h` score `15.959` n `88` status `ready` deltaP `25.26` edge `1.2957` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.832` n `88` status `ready` deltaP `35.8752` edge `0.4135` maxDD `0.0`
- `market_context_high->equity_4h` score `6.3259` n `101` status `ready` deltaP `25.1006` edge `0.4491` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `2.7552` n `88` status `ready` deltaP `23.0837` edge `0.212` maxDD `-6.2367`
- `market_context_high->index_4h` score `2.5102` n `101` status `ready` deltaP `26.2459` edge `0.0702` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.4771` n `101` status `ready` deltaP `22.4347` edge `0.1191` maxDD `-0.979`
- `market_context_high->index_24h` score `1.9828` n `88` status `ready` deltaP `11.6039` edge `0.1549` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.7317` n `101` status `ready` deltaP `14.5743` edge `0.1289` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2897` n `88` status `ready` deltaP `25.0433` edge `0.0354` maxDD `-2.5901`
- `market_context_high->index_1h` score `0.8873` n `101` status `ready` deltaP `14.3327` edge `0.0214` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6779` n `101` status `ready` deltaP `9.7394` edge `0.0294` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.6519` n `101` status `ready` deltaP `9.485` edge `0.1629` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.6347` n `101` status `ready` deltaP `11.9271` edge `0.0429` maxDD `-1.6171`
- `market_context_high->crypto_alt_4h` score `0.625` n `101` status `ready` deltaP `6.2103` edge `0.1224` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.079` n `101` status `ready` deltaP `2.533` edge `0.0365` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.3117` n `101` status `ready` deltaP `-0.621` edge `0.0009` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4008` n `101` status `ready` deltaP `5.6649` edge `0.0036` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.6152` n `101` status `ready` deltaP `-1.6586` edge `-0.0055` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.2342` n `101` status `ready` deltaP `-0.1116` edge `-0.0073` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.8788` n `101` status `ready` deltaP `7.3916` edge `-0.1635` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

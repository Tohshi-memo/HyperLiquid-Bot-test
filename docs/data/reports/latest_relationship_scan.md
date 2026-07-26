# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T22:52:25.407610+00:00`
- Price records: `672`
- Market context records: `8033`
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

- `market_context_high->equity_24h` score `16.2735` n `86` status `ready` deltaP `25.6177` edge `1.3089` maxDD `-5.8845`
- `market_context_high->metal_24h` score `7.9004` n `86` status `ready` deltaP `35.8752` edge `0.4192` maxDD `0.0`
- `market_context_high->equity_4h` score `6.4057` n `99` status `ready` deltaP `24.9584` edge `0.4567` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.1894` n `86` status `ready` deltaP `24.8015` edge `0.2284` maxDD `-6.2367`
- `market_context_high->metal_4h` score `2.6024` n `99` status `ready` deltaP `23.491` edge `0.1225` maxDD `-0.979`
- `market_context_high->index_4h` score `2.5476` n `99` status `ready` deltaP `26.5028` edge `0.0716` maxDD `-0.8791`
- `market_context_high->index_24h` score `1.9019` n `86` status `ready` deltaP `10.6525` edge `0.1545` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6541` n `99` status `ready` deltaP `13.7846` edge `0.1277` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3145` n `86` status `ready` deltaP `24.8196` edge `0.0352` maxDD `-2.2901`
- `market_context_high->index_1h` score `0.8261` n `99` status `ready` deltaP `13.6727` edge `0.0207` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6849` n `99` status `ready` deltaP `9.9317` edge `0.0287` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.5832` n `99` status `ready` deltaP `9.1202` edge `0.1596` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.5766` n `99` status `ready` deltaP `5.785` edge `0.1212` maxDD `-3.9374`
- `market_context_high->crypto_major_1h` score `0.5148` n `99` status `ready` deltaP `10.8677` edge `0.0346` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.06` n `99` status `ready` deltaP `1.1039` edge `0.0282` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.5541` n `99` status `ready` deltaP `-1.4018` edge `-0.0001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.5586` n `99` status `ready` deltaP `3.8571` edge `0.0025` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.614` n `99` status `ready` deltaP `-1.8901` edge `-0.0038` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.2396` n `99` status `ready` deltaP `-0.2756` edge `-0.0069` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.8412` n `99` status `ready` deltaP `7.5017` edge `-0.1611` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

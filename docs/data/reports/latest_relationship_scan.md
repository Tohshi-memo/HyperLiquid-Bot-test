# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T13:52:27.063690+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `market_context_high->unknown_1h` score `0.8177` n `148` status `ready` deltaP `6.4898` edge `0.0476` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5504` n `142` status `ready` deltaP `18.5375` edge `-0.0338` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1273` n `142` status `ready` deltaP `8.4872` edge `0.01` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0323` n `148` status `ready` deltaP `6.6839` edge `0.0044` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0596` n `148` status `ready` deltaP `3.5321` edge `0.0047` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2366` n `142` status `ready` deltaP `7.2247` edge `-0.0169` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.3294` n `148` status `ready` deltaP `0.6797` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->equity_1h` score `-0.3611` n `148` status `ready` deltaP `4.2887` edge `0.0321` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.4817` n `142` status `ready` deltaP `4.5303` edge `0.0116` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8063` n `142` status `ready` deltaP `-2.9457` edge `0.0013` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0765` n `148` status `ready` deltaP `-8.0272` edge `-0.0029` maxDD `-1.1941`
- `market_context_high->fx_24h` score `-1.6597` n `128` status `ready` deltaP `1.7361` edge `0.0111` maxDD `-2.2121`
- `market_context_high->equity_4h` score `-1.767` n `142` status `ready` deltaP `-2.0976` edge `0.0681` maxDD `-16.1188`
- `market_context_high->commodity_24h` score `-2.1679` n `128` status `ready` deltaP `-5.9896` edge `0.0426` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-2.2502` n `142` status `ready` deltaP `4.38` edge `-0.0699` maxDD `-7.0785`
- `market_context_high->crypto_alt_1h` score `-2.4852` n `148` status `ready` deltaP `-2.4478` edge `-0.0413` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.5472` n `148` status `ready` deltaP `-5.1586` edge `-0.1153` maxDD `-7.6729`
- `market_context_high->index_24h` score `-4.5452` n `128` status `ready` deltaP `-9.1145` edge `-0.0424` maxDD `-21.0313`
- `market_context_high->metal_24h` score `-5.5228` n `128` status `ready` deltaP `-25.4341` edge `-0.2077` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.6006` n `142` status `ready` deltaP `-0.949` edge `-0.3274` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

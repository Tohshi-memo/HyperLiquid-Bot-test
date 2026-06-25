# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T14:22:36.709381+00:00`
- Price records: `672`
- Market context records: `4731`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7448`

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

- `market_context_high->unknown_1h` score `79.3638` n `141` status `ready` deltaP `15.0911` edge `6.5548` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.3899` n `141` status `ready` deltaP `14.685` edge `0.4723` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.3839` n `132` status `ready` deltaP `17.0139` edge `0.2609` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3471` n `141` status `ready` deltaP `1.859` edge `0.0227` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.5829` n `141` status `ready` deltaP `5.2197` edge `-0.0001` maxDD `-5.7542`
- `market_context_high->fx_4h` score `-0.8487` n `141` status `ready` deltaP `0.0627` edge `-0.0018` maxDD `-1.9274`
- `market_context_high->equity_1h` score `-0.938` n `141` status `ready` deltaP `-1.3632` edge `-0.0136` maxDD `-5.4726`
- `market_context_high->index_1h` score `-1.0037` n `141` status `ready` deltaP `-3.1596` edge `-0.0072` maxDD `-2.6999`
- `market_context_high->equity_4h` score `-1.1216` n `141` status `ready` deltaP `3.4434` edge `0.006` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-1.3989` n `141` status `ready` deltaP `-6.3915` edge `-0.006` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.5279` n `141` status `ready` deltaP `8.6457` edge `0.0258` maxDD `-9.1941`
- `market_context_high->metal_1h` score `-2.7417` n `141` status `ready` deltaP `-5.3829` edge `-0.0746` maxDD `-15.9475`
- `market_context_high->crypto_alt_1h` score `-2.8833` n `141` status `ready` deltaP `-0.0159` edge `-0.055` maxDD `-21.1642`
- `market_context_high->crypto_major_1h` score `-3.538` n `141` status `ready` deltaP `-0.6466` edge `-0.0752` maxDD `-27.2597`
- `market_context_high->commodity_24h` score `-4.109` n `132` status `ready` deltaP `17.1086` edge `0.0683` maxDD `-28.6488`
- `market_context_high->fx_24h` score `-4.7305` n `132` status `ready` deltaP `-13.81` edge `-0.0193` maxDD `-5.2943`
- `market_context_high->crypto_alt_4h` score `-7.2558` n `141` status `ready` deltaP `-1.0574` edge `-0.1122` maxDD `-59.5456`
- `market_context_high->index_24h` score `-8.1101` n `132` status `ready` deltaP `-11.3794` edge `-0.1002` maxDD `-27.3155`
- `market_context_high->metal_4h` score `-8.5223` n `141` status `ready` deltaP `2.1504` edge `-0.2573` maxDD `-62.6377`
- `market_context_high->crypto_major_4h` score `-10.1979` n `141` status `ready` deltaP `-0.6465` edge `-0.2295` maxDD `-80.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

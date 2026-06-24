# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T09:07:28.617005+00:00`
- Price records: `672`
- Market context records: `4606`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9851`

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

- `market_context_high->unknown_1h` score `69.2599` n `147` status `ready` deltaP `7.2091` edge `5.7695` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.2432` n `147` status `ready` deltaP `8.7512` edge `0.4163` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.4845` n `147` status `ready` deltaP `2.0286` edge `0.0257` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5544` n `147` status `ready` deltaP `-1.7272` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.739` n `147` status `ready` deltaP `2.0989` edge `-0.0005` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.9129` n `147` status `ready` deltaP `-2.5856` edge `-0.0011` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.9568` n `147` status `ready` deltaP `0.7518` edge `-0.0154` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1695` n `147` status `ready` deltaP `3.7395` edge `0.0359` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.7479` n `147` status `ready` deltaP `-4.6947` edge `-0.0135` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.7835` n `147` status `ready` deltaP `-1.3709` edge `-0.0426` maxDD `-8.8203`
- `market_context_high->unknown_24h` score `-2.3849` n `145` status `ready` deltaP `2.579` edge `-0.1236` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-3.0117` n `147` status `ready` deltaP `-4.7477` edge `-0.0893` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.5921` n `145` status `ready` deltaP `11.6295` edge `0.0647` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.3581` n `145` status `ready` deltaP `-12.6724` edge `-0.0108` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.6276` n `147` status `ready` deltaP `-2.7353` edge `-0.122` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8745` n `147` status `ready` deltaP `-6.4493` edge `-0.1546` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.4759` n `145` status `ready` deltaP `-8.3166` edge `-0.1134` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.2459` n `147` status `ready` deltaP `-3.9986` edge `-0.293` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.3985` n `147` status `ready` deltaP `-7.343` edge `-0.3628` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.3947` n `147` status `ready` deltaP `-6.0281` edge `-0.4545` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

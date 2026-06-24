# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T13:22:30.977417+00:00`
- Price records: `672`
- Market context records: `4625`
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

- `market_context_high->unknown_1h` score `69.375` n `147` status `ready` deltaP `8.4067` edge `5.7711` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.3706` n `147` status `ready` deltaP `9.8183` edge `0.4198` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.3623` n `147` status `ready` deltaP `3.0765` edge `0.0289` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5529` n `147` status `ready` deltaP `-1.7272` edge `-0.0039` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7613` n `147` status `ready` deltaP `1.6416` edge `-0.0003` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.8817` n `147` status `ready` deltaP `-2.1365` edge `-0.0001` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.9189` n `147` status `ready` deltaP `1.3616` edge `-0.0146` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.0417` n `147` status `ready` deltaP `5.4163` edge `0.0411` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-1.5455` n `145` status `ready` deltaP `4.836` edge `-0.0687` maxDD `-4.7201`
- `market_context_high->index_1h` score `-1.7288` n `147` status `ready` deltaP `-4.545` edge `-0.0129` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.775` n `147` status `ready` deltaP `-1.3709` edge `-0.0415` maxDD `-8.8203`
- `market_context_high->metal_1h` score `-2.9337` n `147` status `ready` deltaP `-4.1489` edge `-0.0833` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.7793` n `145` status `ready` deltaP `11.6295` edge `0.0491` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.1282` n `145` status `ready` deltaP `-10.0682` edge `-0.009` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.6264` n `147` status `ready` deltaP `-2.5856` edge `-0.1229` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8686` n `147` status `ready` deltaP `-6.2996` edge `-0.1551` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.1495` n `145` status `ready` deltaP `-8.3166` edge `-0.0862` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.2413` n `147` status `ready` deltaP `-3.9986` edge `-0.2924` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2554` n `147` status `ready` deltaP `-6.8857` edge `-0.3475` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.39` n `147` status `ready` deltaP `-6.0281` edge `-0.4539` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

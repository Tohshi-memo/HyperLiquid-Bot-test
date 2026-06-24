# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T22:22:27.455507+00:00`
- Price records: `672`
- Market context records: `4664`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9996`

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

- `market_context_high->unknown_1h` score `70.2839` n `146` status `ready` deltaP `9.0579` edge `5.8425` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.5093` n `146` status `ready` deltaP `10.038` edge `0.4299` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.4307` n `146` status `ready` deltaP `8.9945` edge `0.1516` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.46` n `146` status `ready` deltaP `2.4998` edge `0.0246` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5473` n `146` status `ready` deltaP `-1.6508` edge `-0.0037` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.6817` n `146` status `ready` deltaP `4.1827` edge `-0.003` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.7532` n `146` status `ready` deltaP `1.6017` edge `0.001` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.7697` n `146` status `ready` deltaP `-1.0479` edge `0.007` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.0485` n `146` status `ready` deltaP `2.3555` edge `0.0268` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2645` n `146` status `ready` deltaP `4.5815` edge `0.0181` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6939` n `146` status `ready` deltaP `-4.2142` edge `-0.0122` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8216` n `146` status `ready` deltaP `-3.7917` edge `-0.0713` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6668` n `146` status `ready` deltaP `13.7153` edge `0.0701` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-5.157` n `146` status `ready` deltaP `-10.2478` edge `-0.0102` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.2477` n `146` status `ready` deltaP `-1.3473` edge `-0.0996` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.4649` n `146` status `ready` deltaP `-4.9442` edge `-0.1305` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.3478` n `146` status `ready` deltaP `-6.3951` edge `-0.0322` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-7.9047` n `146` status `ready` deltaP `0.0` edge `-0.1477` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.4744` n `146` status `ready` deltaP `-2.7272` edge `-0.2751` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.0711` n `146` status `ready` deltaP `-2.2052` edge `-0.3103` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T19:52:29.715781+00:00`
- Price records: `672`
- Market context records: `4653`
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

- `market_context_high->unknown_1h` score `70.3798` n `146` status `ready` deltaP `9.2076` edge `5.8495` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `5.4241` n `146` status `ready` deltaP `11.2575` edge `0.498` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `0.7207` n `146` status `ready` deltaP `7.2584` edge `0.104` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3725` n `146` status `ready` deltaP `3.2483` edge `0.0269` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5535` n `146` status `ready` deltaP `-1.8005` edge `-0.0035` maxDD `-1.1038`
- `market_context_high->equity_1h` score `-0.6154` n `146` status `ready` deltaP `-0.2994` edge `0.0218` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.6511` n `146` status `ready` deltaP `4.3351` edge `-0.0001` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.7516` n `146` status `ready` deltaP `1.6017` edge `0.0012` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.8831` n `146` status `ready` deltaP `2.3555` edge `0.048` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2317` n `146` status `ready` deltaP `4.5815` edge `0.0223` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.634` n `146` status `ready` deltaP `-3.7651` edge `-0.0102` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.7842` n `146` status `ready` deltaP `-3.1929` edge `-0.0705` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-5.0205` n `146` status `ready` deltaP `11.9792` edge `0.0522` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-5.0441` n `146` status `ready` deltaP `-9.0325` edge `-0.0089` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.057` n `146` status `ready` deltaP `-0.8982` edge `-0.0867` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.2658` n `146` status `ready` deltaP `-4.3454` edge `-0.1179` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.4114` n `146` status `ready` deltaP `-6.3951` edge `-0.0375` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-7.7706` n `146` status `ready` deltaP `-0.1524` edge `-0.1295` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.5671` n `146` status `ready` deltaP `-3.4894` edge `-0.2819` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-10.9026` n `146` status `ready` deltaP `-2.2052` edge `-0.2887` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

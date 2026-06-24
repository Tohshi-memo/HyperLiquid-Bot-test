# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T22:07:31.545856+00:00`
- Price records: `672`
- Market context records: `4663`
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

- `market_context_high->unknown_1h` score `70.4603` n `146` status `ready` deltaP `9.0579` edge `5.8572` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.5563` n `146` status `ready` deltaP `10.1905` edge `0.4328` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.3725` n `146` status `ready` deltaP `8.8209` edge `0.1479` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4588` n `146` status `ready` deltaP `2.4998` edge `0.0247` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5567` n `146` status `ready` deltaP `-1.8005` edge `-0.0039` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.6652` n `146` status `ready` deltaP `4.3351` edge `-0.0019` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.7557` n `146` status `ready` deltaP `-0.8982` edge `0.0078` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.7627` n `146` status `ready` deltaP `1.4492` edge `0.0008` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-1.0227` n `146` status `ready` deltaP `2.3555` edge `0.0301` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2653` n `146` status `ready` deltaP `4.5815` edge `0.018` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6927` n `146` status `ready` deltaP `-4.2142` edge `-0.0121` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8138` n `146` status `ready` deltaP `-3.642` edge `-0.0713` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.7059` n `146` status `ready` deltaP `13.5417` edge `0.068` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-5.157` n `146` status `ready` deltaP `-10.2478` edge `-0.0102` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.2189` n `146` status `ready` deltaP `-1.1976` edge `-0.0982` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.4386` n `146` status `ready` deltaP `-4.7945` edge `-0.1293` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.3478` n `146` status `ready` deltaP `-6.3951` edge `-0.0322` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-7.8836` n `146` status `ready` deltaP `0.0` edge `-0.145` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.4713` n `146` status `ready` deltaP `-2.7272` edge `-0.2747` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.0485` n `146` status `ready` deltaP `-2.2052` edge `-0.3074` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

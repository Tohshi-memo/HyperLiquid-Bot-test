# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T20:37:30.388436+00:00`
- Price records: `672`
- Market context records: `4656`
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

- `market_context_high->unknown_1h` score `70.5323` n `146` status `ready` deltaP `9.0579` edge `5.8632` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `5.3843` n `146` status `ready` deltaP `11.1051` edge `0.4957` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `0.9675` n `146` status `ready` deltaP `7.7792` edge `0.1211` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3929` n `146` status `ready` deltaP `3.0986` edge `0.0262` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5458` n `146` status `ready` deltaP `-1.6508` edge `-0.0035` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.6488` n `146` status `ready` deltaP `4.3351` edge `0.0002` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.7152` n `146` status `ready` deltaP `-0.7485` edge `0.012` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.7706` n `146` status `ready` deltaP `1.2968` edge `0.0008` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.894` n `146` status `ready` deltaP `2.3555` edge `0.0466` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2497` n `146` status `ready` deltaP `4.5815` edge `0.02` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.7011` n `146` status `ready` deltaP `-4.2142` edge `-0.0128` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8068` n `146` status `ready` deltaP `-3.3426` edge `-0.0724` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.926` n `146` status `ready` deltaP `12.5` edge `0.0566` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-5.093` n `146` status `ready` deltaP `-9.5533` edge `-0.0095` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.141` n `146` status `ready` deltaP `-0.8982` edge `-0.0937` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.3426` n `146` status `ready` deltaP `-4.3454` edge `-0.1243` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.3838` n `146` status `ready` deltaP `-6.3951` edge `-0.0352` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-7.7346` n `146` status `ready` deltaP `0.0` edge `-0.1259` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.5082` n `146` status `ready` deltaP `-3.0321` edge `-0.2774` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-10.894` n `146` status `ready` deltaP `-2.2052` edge `-0.2876` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

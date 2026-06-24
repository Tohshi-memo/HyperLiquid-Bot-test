# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T17:22:29.751593+00:00`
- Price records: `672`
- Market context records: `4642`
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

- `market_context_high->unknown_1h` score `70.0931` n `146` status `ready` deltaP `8.7585` edge `5.8286` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.8127` n `146` status `ready` deltaP `9.8856` edge `0.4562` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `-0.2755` n `146` status `ready` deltaP `5.6959` edge `0.0314` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3485` n `146` status `ready` deltaP `2.9489` edge `0.0309` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5816` n `146` status `ready` deltaP `-2.2496` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7002` n `146` status `ready` deltaP `2.5163` edge `0.0017` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.7486` n `146` status `ready` deltaP `-1.1976` edge `0.0107` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.8061` n `146` status `ready` deltaP `2.8107` edge `-0.0098` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.0866` n `146` status `ready` deltaP `5.6485` edge `0.0338` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.2611` n `146` status `ready` deltaP `0.8311` edge `0.0097` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7083` n `146` status `ready` deltaP `-4.3639` edge `-0.0124` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9409` n `146` status `ready` deltaP `-4.2408` edge `-0.0836` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-4.9893` n `146` status `ready` deltaP `-8.5117` edge `-0.0078` maxDD `-6.0982`
- `market_context_high->commodity_24h` score `-5.1745` n `146` status `ready` deltaP `11.2847` edge `0.044` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.2945` n `146` status `ready` deltaP `-1.497` edge `-0.1025` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.5201` n `146` status `ready` deltaP `-4.9442` edge `-0.1351` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.7281` n `146` status `ready` deltaP `-7.2631` edge `-0.0581` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.4287` n `146` status `ready` deltaP `-1.6768` edge `-0.2037` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.9178` n `146` status `ready` deltaP `-5.0138` edge `-0.3167` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.5529` n `146` status `ready` deltaP `-3.7296` edge `-0.3619` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

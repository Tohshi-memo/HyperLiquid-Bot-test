# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T16:37:31.960611+00:00`
- Price records: `672`
- Market context records: `4639`
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

- `market_context_high->unknown_1h` score `70.0068` n `146` status `ready` deltaP `8.3094` edge `5.8244` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.6493` n `146` status `ready` deltaP `9.7331` edge `0.4436` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.3161` n `146` status `ready` deltaP `3.2483` edge `0.0316` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5816` n `146` status `ready` deltaP `-2.2496` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->unknown_24h` score `-0.6278` n `146` status `ready` deltaP `5.5223` edge `0.0032` maxDD `-4.7201`
- `market_context_high->fx_4h` score `-0.7041` n `146` status `ready` deltaP `2.5163` edge `0.0012` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.7954` n `146` status `ready` deltaP `-1.497` edge `0.0067` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.8415` n `146` status `ready` deltaP `2.3534` edge `-0.0113` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.0333` n `146` status `ready` deltaP `5.9534` edge `0.0386` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.3878` n `146` status `ready` deltaP `0.3738` edge `-0.0035` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7382` n `146` status `ready` deltaP `-4.6633` edge `-0.0129` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9533` n `146` status `ready` deltaP `-4.3905` edge `-0.0842` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-4.9893` n `146` status `ready` deltaP `-8.5117` edge `-0.0078` maxDD `-6.0982`
- `market_context_high->commodity_24h` score `-5.1625` n `146` status `ready` deltaP `11.2847` edge `0.045` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.4492` n `146` status `ready` deltaP `-1.7964` edge `-0.1134` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.6401` n `146` status `ready` deltaP `-5.3933` edge `-0.1421` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.835` n `146` status `ready` deltaP `-7.6104` edge `-0.0647` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6904` n `146` status `ready` deltaP `-2.1341` edge `-0.2342` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.0016` n `146` status `ready` deltaP `-5.4711` edge `-0.3244` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.8075` n `146` status `ready` deltaP `-4.1869` edge `-0.3915` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

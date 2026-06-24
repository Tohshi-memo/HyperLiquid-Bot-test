# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T15:52:30.783198+00:00`
- Price records: `672`
- Market context records: `4636`
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

- `market_context_high->unknown_1h` score `70.002` n `146` status `ready` deltaP `8.3094` edge `5.824` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.5161` n `146` status `ready` deltaP `9.7331` edge `0.4325` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.3041` n `146` status `ready` deltaP `3.398` edge `0.0316` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5738` n `146` status `ready` deltaP `-2.0999` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7238` n `146` status `ready` deltaP `2.2114` edge `0.0007` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.8328` n `146` status `ready` deltaP `-1.9461` edge `0.0049` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.8786` n `146` status `ready` deltaP `1.8961` edge `-0.013` maxDD `-5.9823`
- `market_context_high->unknown_24h` score `-1.0041` n `146` status `ready` deltaP `5.3487` edge `-0.027` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `-1.0106` n `146` status `ready` deltaP `5.9534` edge `0.0415` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.513` n `146` status `ready` deltaP `-0.0835` edge `-0.0165` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7514` n `146` status `ready` deltaP `-4.813` edge `-0.013` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9533` n `146` status `ready` deltaP `-4.3905` edge `-0.0842` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-4.9893` n `146` status `ready` deltaP `-8.5117` edge `-0.0078` maxDD `-6.0982`
- `market_context_high->commodity_24h` score `-5.1517` n `146` status `ready` deltaP `11.2847` edge `0.0459` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.5416` n `146` status `ready` deltaP `-2.2455` edge `-0.1181` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7336` n `146` status `ready` deltaP `-5.8424` edge `-0.1469` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.913` n `146` status `ready` deltaP `-7.6104` edge `-0.0712` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.9138` n `146` status `ready` deltaP `-2.5915` edge `-0.2598` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.0964` n `146` status `ready` deltaP `-5.9284` edge `-0.3335` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.0474` n `146` status `ready` deltaP `-4.6442` edge `-0.4192` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T18:22:29.158628+00:00`
- Price records: `672`
- Market context records: `4646`
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

- `market_context_high->unknown_1h` score `70.1219` n `146` status `ready` deltaP `9.0579` edge `5.829` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `5.1315` n `146` status `ready` deltaP `10.4953` edge `0.4787` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `0.2137` n `146` status `ready` deltaP `6.2167` edge `0.0687` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3952` n `146` status `ready` deltaP `2.7992` edge `0.028` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5738` n `146` status `ready` deltaP `-2.0999` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->equity_1h` score `-0.6871` n `146` status `ready` deltaP `-0.7485` edge `0.0156` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.7255` n `146` status `ready` deltaP `2.059` edge `0.0015` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.7463` n `146` status `ready` deltaP `3.4205` edge `-0.0062` maxDD `-5.9823`
- `market_context_high->equity_4h` score `-1.1007` n `146` status `ready` deltaP `1.4408` edge `0.0262` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.1775` n `146` status `ready` deltaP `5.0388` edge `0.0262` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6747` n `146` status `ready` deltaP `-4.0645` edge `-0.0116` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8777` n `146` status `ready` deltaP `-3.642` edge `-0.0795` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-5.008` n `146` status `ready` deltaP `-8.6853` edge `-0.0082` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.1434` n `146` status `ready` deltaP `-1.0479` edge `-0.0929` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.1697` n `146` status `ready` deltaP `11.2847` edge `0.0444` maxDD `-30.7016`
- `market_context_high->crypto_major_1h` score `-6.3798` n `146` status `ready` deltaP `-4.4951` edge `-0.1264` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.576` n `146` status `ready` deltaP `-6.7423` edge `-0.0489` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.0889` n `146` status `ready` deltaP `-1.0671` edge `-0.1642` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.7597` n `146` status `ready` deltaP `-4.404` edge `-0.3005` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.2123` n `146` status `ready` deltaP `-3.1198` edge `-0.3223` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

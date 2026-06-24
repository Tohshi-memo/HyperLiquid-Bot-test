# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T21:52:45.823199+00:00`
- Price records: `672`
- Market context records: `4662`
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

- `market_context_high->unknown_1h` score `70.4783` n `146` status `ready` deltaP `9.0579` edge `5.8587` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.7293` n `146` status `ready` deltaP `10.3429` edge `0.4462` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.3118` n `146` status `ready` deltaP `8.6473` edge `0.144` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4576` n `146` status `ready` deltaP `2.4998` edge `0.0248` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5652` n `146` status `ready` deltaP `-1.9502` edge `-0.004` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.6589` n `146` status `ready` deltaP `4.3351` edge `-0.0011` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.7432` n `146` status `ready` deltaP `-0.7485` edge `0.0084` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.7722` n `146` status `ready` deltaP `1.2968` edge `0.0006` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.9923` n `146` status `ready` deltaP `2.3555` edge `0.034` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2653` n `146` status `ready` deltaP `4.5815` edge `0.018` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6927` n `146` status `ready` deltaP `-4.2142` edge `-0.0121` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8052` n `146` status `ready` deltaP `-3.4923` edge `-0.0712` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.7474` n `146` status `ready` deltaP `13.3681` edge `0.0657` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-5.1582` n `146` status `ready` deltaP `-10.2478` edge `-0.0103` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.1806` n `146` status `ready` deltaP `-1.0479` edge `-0.096` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.4026` n `146` status `ready` deltaP `-4.6448` edge `-0.1273` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.349` n `146` status `ready` deltaP `-6.3951` edge `-0.0323` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-7.8509` n `146` status `ready` deltaP `0.0` edge `-0.1408` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.4666` n `146` status `ready` deltaP `-2.7272` edge `-0.2741` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.0142` n `146` status `ready` deltaP `-2.2052` edge `-0.303` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

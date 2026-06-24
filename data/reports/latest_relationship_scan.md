# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T20:22:26.369198+00:00`
- Price records: `672`
- Market context records: `4655`
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

- `market_context_high->unknown_1h` score `70.6366` n `146` status `ready` deltaP `9.2076` edge `5.8709` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `5.4241` n `146` status `ready` deltaP `11.2575` edge `0.498` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `0.8792` n `146` status `ready` deltaP `7.6056` edge `0.1149` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3893` n `146` status `ready` deltaP `3.0986` edge `0.0265` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.545` n `146` status `ready` deltaP `-1.6508` edge `-0.0034` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.6488` n `146` status `ready` deltaP `4.3351` edge `0.0002` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.6816` n `146` status `ready` deltaP `-0.5988` edge `0.0153` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.7698` n `146` status `ready` deltaP `1.2968` edge `0.0009` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.8839` n `146` status `ready` deltaP `2.3555` edge `0.0479` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2427` n `146` status `ready` deltaP `4.5815` edge `0.0209` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6783` n `146` status `ready` deltaP `-4.0645` edge `-0.0119` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8044` n `146` status `ready` deltaP `-3.3426` edge `-0.0721` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.9567` n `146` status `ready` deltaP `12.3264` edge `0.0552` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-5.0779` n `146` status `ready` deltaP `-9.3797` edge `-0.0094` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.1206` n `146` status `ready` deltaP `-0.8982` edge `-0.092` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.3222` n `146` status `ready` deltaP `-4.3454` edge `-0.1226` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.3934` n `146` status `ready` deltaP `-6.3951` edge `-0.036` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-7.7424` n `146` status `ready` deltaP `0.0` edge `-0.1269` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.5286` n `146` status `ready` deltaP `-3.1845` edge `-0.279` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-10.8925` n `146` status `ready` deltaP `-2.2052` edge `-0.2874` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

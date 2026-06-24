# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T21:07:46.921207+00:00`
- Price records: `672`
- Market context records: `4659`
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

- `market_context_high->unknown_1h` score `70.4255` n `146` status `ready` deltaP `8.9082` edge `5.8553` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `5.2243` n `146` status `ready` deltaP `10.8002` edge `0.4844` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.1093` n `146` status `ready` deltaP `8.1265` edge `0.1306` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4133` n `146` status `ready` deltaP `2.9489` edge `0.0255` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5645` n `146` status `ready` deltaP `-1.9502` edge `-0.0039` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.6519` n `146` status `ready` deltaP `4.3351` edge `-0.0002` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.7464` n `146` status `ready` deltaP `-0.7485` edge `0.008` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.7888` n `146` status `ready` deltaP `0.9919` edge `0.0005` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.9237` n `146` status `ready` deltaP `2.3555` edge `0.0428` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.259` n `146` status `ready` deltaP `4.5815` edge `0.0188` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.7059` n `146` status `ready` deltaP `-4.2142` edge `-0.0132` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.7943` n `146` status `ready` deltaP `-3.1929` edge `-0.0718` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.8575` n `146` status `ready` deltaP `12.8472` edge `0.06` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-5.1256` n `146` status `ready` deltaP `-9.9006` edge `-0.0099` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.1374` n `146` status `ready` deltaP `-0.7485` edge `-0.0944` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.3594` n `146` status `ready` deltaP `-4.3454` edge `-0.1257` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.3706` n `146` status `ready` deltaP `-6.3951` edge `-0.0341` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-7.7604` n `146` status `ready` deltaP `0.0` edge `-0.1292` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.4736` n `146` status `ready` deltaP `-2.7272` edge `-0.275` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-10.9229` n `146` status `ready` deltaP `-2.2052` edge `-0.2913` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

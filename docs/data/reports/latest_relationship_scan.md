# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T05:37:28.988199+00:00`
- Price records: `672`
- Market context records: `4591`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9937`

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

- `market_context_high->unknown_1h` score `67.3589` n `150` status `ready` deltaP `6.1477` edge `5.6223` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.9427` n `150` status `ready` deltaP `7.9207` edge `0.3968` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.52` n `150` status `ready` deltaP `1.6746` edge `0.0251` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.6882` n `150` status `ready` deltaP `2.8963` edge `0.0007` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-0.857` n `150` status `ready` deltaP `-1.8224` edge `-0.0038` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8938` n `150` status `ready` deltaP `1.4838` edge `-0.0122` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9988` n `150` status `ready` deltaP `-3.8782` edge `-0.0035` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.1974` n `150` status `ready` deltaP `3.622` edge `0.0331` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.5787` n `150` status `ready` deltaP `0.0935` edge `-0.0261` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7269` n `150` status `ready` deltaP `-4.477` edge `-0.0132` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.6766` n `148` status `ready` deltaP `1.7972` edge `-0.1427` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.9729` n `150` status `ready` deltaP `-4.4212` edge `-0.0865` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6701` n `148` status `ready` deltaP `10.609` edge `0.065` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.4403` n `148` status `ready` deltaP `-13.5792` edge `-0.0116` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5523` n `150` status `ready` deltaP `-2.3952` edge `-0.118` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8564` n `150` status `ready` deltaP `-6.4631` edge `-0.153` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.4091` n `148` status `ready` deltaP `-7.6014` edge `-0.1126` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.1095` n `150` status `ready` deltaP `-3.9248` edge `-0.276` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2296` n `150` status `ready` deltaP `-6.1504` edge `-0.3491` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.1437` n `150` status `ready` deltaP `-4.2479` edge `-0.4342` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

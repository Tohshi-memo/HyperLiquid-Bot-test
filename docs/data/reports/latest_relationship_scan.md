# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T18:07:29.826254+00:00`
- Price records: `672`
- Market context records: `5689`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8856`

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

- `market_context_high->equity_24h` score `1.7717` n `207` status `ready` deltaP `16.1761` edge `0.5477` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.4499` n `257` status `ready` deltaP `12.3369` edge `0.2271` maxDD `-10.7482`
- `market_context_high->crypto_alt_4h` score `0.8499` n `257` status `ready` deltaP `9.4245` edge `0.1689` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2029` n `257` status `ready` deltaP `6.2957` edge `0.1388` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2643` n `269` status `ready` deltaP `1.8949` edge `0.0011` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.3818` n `269` status `ready` deltaP `2.9128` edge `0.0415` maxDD `-4.7522`
- `market_context_high->metal_1h` score `-0.4881` n `269` status `ready` deltaP `0.847` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5141` n `269` status `ready` deltaP `4.5645` edge `0.0428` maxDD `-6.2855`
- `market_context_high->equity_1h` score `-0.5738` n `269` status `ready` deltaP `3.6413` edge `0.0286` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6293` n `269` status `ready` deltaP `0.2482` edge `0.0045` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.8975` n `207` status `ready` deltaP `13.5115` edge `0.0463` maxDD `-3.1151`
- `market_context_high->commodity_1h` score `-0.9407` n `269` status `ready` deltaP `0.2632` edge `-0.0036` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1253` n `257` status `ready` deltaP `4.7956` edge `0.0072` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2918` n `257` status `ready` deltaP `-0.8767` edge `0.0074` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.6435` n `207` status `ready` deltaP `4.9064` edge `0.0346` maxDD `-17.4972`
- `market_context_high->metal_4h` score `-2.8259` n `257` status `ready` deltaP `-10.7887` edge `-0.0528` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.8367` n `257` status `ready` deltaP `-3.0102` edge `-0.0321` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.5474` n `207` status `ready` deltaP `4.6121` edge `0.036` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.2178` n `207` status `ready` deltaP `-11.0733` edge `-0.2467` maxDD `-32.6431`
- `market_context_high->commodity_24h` score `-12.0707` n `207` status `ready` deltaP `-10.5299` edge `-0.0748` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

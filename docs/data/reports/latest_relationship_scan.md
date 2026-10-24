# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T21:22:30.642181+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7816`

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

- `market_context_high->unknown_4h` score `17.6158` n `102` status `ready` deltaP `-2.1431` edge `1.5158` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.7008` n `69` status `ready` deltaP `23.1658` edge `0.0782` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.9741` n `102` status `ready` deltaP `12.9453` edge `0.0511` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.0383` n `107` status `ready` deltaP `5.4718` edge `0.0104` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.2074` n `107` status `ready` deltaP `0.957` edge `0.0025` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.398` n `102` status `ready` deltaP `0.5858` edge `0.0057` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.0888` n `107` status `ready` deltaP `-2.7814` edge `-0.007` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.3096` n `107` status `ready` deltaP `-3.5257` edge `-0.0062` maxDD `-1.6873`
- `market_context_high->fx_24h` score `-2.8812` n `69` status `ready` deltaP `-9.9184` edge `-0.0052` maxDD `-2.169`
- `market_context_high->crypto_major_1h` score `-3.1103` n `107` status `ready` deltaP `-3.2346` edge `-0.0577` maxDD `-11.0607`
- `market_context_high->metal_4h` score `-3.6005` n `102` status `ready` deltaP `-12.4253` edge `-0.0298` maxDD `-5.9927`
- `market_context_high->equity_1h` score `-4.2667` n `107` status `ready` deltaP `-3.4893` edge `-0.0994` maxDD `-12.6316`
- `market_context_high->metal_24h` score `-4.2695` n `69` status `ready` deltaP `-13.9266` edge `0.0204` maxDD `-8.0012`
- `market_context_high->crypto_alt_1h` score `-4.8021` n `107` status `ready` deltaP `-8.1258` edge `-0.0901` maxDD `-16.1391`
- `market_context_high->index_4h` score `-4.9258` n `102` status `ready` deltaP `-23.924` edge `-0.0507` maxDD `-5.3565`
- `market_context_high->crypto_major_24h` score `-5.692` n `69` status `ready` deltaP `-10.7488` edge `-0.2307` maxDD `-26.5244`
- `market_context_high->index_24h` score `-8.5468` n `69` status `ready` deltaP `-38.6398` edge `-0.1682` maxDD `-7.9149`
- `market_context_high->crypto_alt_24h` score `-15.3546` n `69` status `ready` deltaP `-7.6842` edge `-0.6921` maxDD `-86.0169`
- `market_context_high->crypto_major_4h` score `-15.9965` n `102` status `ready` deltaP `-29.8721` edge `-0.3894` maxDD `-47.893`
- `market_context_high->equity_4h` score `-17.1276` n `102` status `ready` deltaP `-23.9898` edge `-0.472` maxDD `-51.2958`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

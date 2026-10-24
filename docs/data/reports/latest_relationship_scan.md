# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T21:52:28.698488+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7318`

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

- `market_context_high->unknown_4h` score `18.5677` n `101` status `ready` deltaP `-1.5093` edge `1.5909` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.9021` n `67` status `ready` deltaP `25.1114` edge `0.082` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `1.0579` n `101` status `ready` deltaP `13.6636` edge `0.0533` maxDD `-1.165`
- `market_context_high->commodity_1h` score `0.1245` n `107` status `ready` deltaP `7.0415` edge `0.0135` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.1658` n `107` status `ready` deltaP `1.7418` edge `0.0026` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.4191` n `101` status `ready` deltaP `0.1947` edge `0.0056` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.0876` n `107` status `ready` deltaP `-2.7814` edge `-0.0069` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.3132` n `107` status `ready` deltaP `-3.5257` edge `-0.0065` maxDD `-1.6873`
- `market_context_high->fx_24h` score `-2.7152` n `67` status `ready` deltaP `-9.3128` edge `-0.0049` maxDD `-2.0758`
- `market_context_high->crypto_major_1h` score `-3.2851` n `107` status `ready` deltaP `-4.8044` edge `-0.0618` maxDD `-11.0607`
- `market_context_high->metal_4h` score `-3.5299` n `101` status `ready` deltaP `-11.5265` edge `-0.03` maxDD `-5.985`
- `market_context_high->metal_24h` score `-4.1316` n `67` status `ready` deltaP `-13.5805` edge `0.0195` maxDD `-7.8608`
- `market_context_high->equity_1h` score `-4.2715` n `107` status `ready` deltaP `-3.4893` edge `-0.0998` maxDD `-12.6316`
- `market_context_high->crypto_alt_1h` score `-4.627` n `107` status `ready` deltaP `-8.1258` edge `-0.0898` maxDD `-15.6625`
- `market_context_high->index_4h` score `-4.9935` n `101` status `ready` deltaP `-24.7102` edge `-0.0511` maxDD `-5.3565`
- `market_context_high->crypto_major_24h` score `-5.2148` n `67` status `ready` deltaP `-9.4942` edge `-0.2064` maxDD `-24.9098`
- `market_context_high->index_24h` score `-8.3908` n `67` status `ready` deltaP `-38.3369` edge `-0.1684` maxDD `-7.6871`
- `market_context_high->crypto_alt_24h` score `-14.2304` n `67` status `ready` deltaP `-6.4729` edge `-0.6339` maxDD `-80.4555`
- `market_context_high->crypto_major_4h` score `-15.7578` n `101` status `ready` deltaP `-29.0509` edge `-0.3853` maxDD `-47.7343`
- `market_context_high->equity_4h` score `-17.153` n `101` status `ready` deltaP `-23.948` edge `-0.4744` maxDD `-51.2958`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

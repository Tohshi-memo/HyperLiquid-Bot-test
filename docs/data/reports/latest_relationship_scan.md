# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T23:07:26.406879+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `20.9343` n `99` status `ready` deltaP `2.379` edge `1.7622` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.7946` n `62` status `ready` deltaP `23.9472` edge `0.0808` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.8923` n `99` status `ready` deltaP `11.7132` edge `0.0525` maxDD `-1.165`
- `market_context_high->commodity_1h` score `0.1125` n `107` status `ready` deltaP `7.0415` edge `0.0125` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3807` n `107` status `ready` deltaP `0.1721` edge `0.0026` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.5084` n `99` status `ready` deltaP `-1.4782` edge `0.0053` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.0876` n `107` status `ready` deltaP `-2.7814` edge `-0.0069` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.1188` n `107` status `ready` deltaP `-1.171` edge `-0.006` maxDD `-1.6873`
- `market_context_high->fx_24h` score `-2.275` n `62` status `ready` deltaP `-7.6277` edge `-0.0033` maxDD `-1.8345`
- `market_context_high->crypto_major_1h` score `-3.0316` n `107` status `ready` deltaP `-3.2346` edge `-0.0539` maxDD `-10.8405`
- `market_context_high->metal_4h` score `-3.5957` n `99` status `ready` deltaP `-12.229` edge `-0.0308` maxDD `-5.985`
- `market_context_high->metal_24h` score `-3.8` n `62` status `ready` deltaP `-12.6176` edge `0.0157` maxDD `-7.5265`
- `market_context_high->crypto_major_24h` score `-3.8448` n `62` status `ready` deltaP `-6.0036` edge `-0.1349` maxDD `-20.1066`
- `market_context_high->crypto_alt_1h` score `-4.0006` n `107` status `ready` deltaP `-4.2014` edge `-0.0763` maxDD `-14.9927`
- `market_context_high->equity_1h` score `-4.0435` n `107` status `ready` deltaP `-1.1347` edge `-0.0965` maxDD `-12.6316`
- `market_context_high->index_4h` score `-5.1399` n `99` status `ready` deltaP `-26.3304` edge `-0.0525` maxDD `-5.3565`
- `market_context_high->index_24h` score `-8.0663` n `62` status `ready` deltaP `-37.8416` edge `-0.171` maxDD `-7.2467`
- `market_context_high->crypto_alt_24h` score `-11.4358` n `62` status `ready` deltaP `-3.1026` edge `-0.4872` maxDD `-66.9926`
- `market_context_high->crypto_major_4h` score `-15.0052` n `99` status `ready` deltaP `-26.4828` edge `-0.3736` maxDD `-46.6889`
- `market_context_high->equity_4h` score `-17.3762` n `99` status `ready` deltaP `-25.5682` edge `-0.4822` maxDD `-51.2958`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

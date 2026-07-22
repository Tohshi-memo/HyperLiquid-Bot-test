# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T16:52:30.153097+00:00`
- Price records: `672`
- Market context records: `7584`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14534`

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

- `market_context_high->commodity_4h` score `0.1816` n `158` status `ready` deltaP `9.4859` edge `0.0279` maxDD `-2.4139`
- `market_context_high->index_1h` score `0.0311` n `158` status `ready` deltaP `6.0498` edge `0.0125` maxDD `-0.9072`
- `market_context_high->commodity_24h` score `-0.0745` n `150` status `ready` deltaP `12.4111` edge `0.0694` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.1496` n `158` status `ready` deltaP `6.0079` edge `0.0047` maxDD `-1.5775`
- `market_context_high->unknown_24h` score `-0.4094` n `151` status `ready` deltaP `9.383` edge `0.098` maxDD `-8.3767`
- `market_context_high->crypto_alt_1h` score `-0.4726` n `158` status `ready` deltaP `0.4832` edge `0.0108` maxDD `-3.6359`
- `market_context_high->crypto_major_1h` score `-0.5014` n `158` status `ready` deltaP `6.0638` edge `0.0105` maxDD `-5.5504`
- `market_context_high->fx_1h` score `-0.5301` n `158` status `ready` deltaP `0.9542` edge `-0.0006` maxDD `-0.6615`
- `market_context_high->index_4h` score `-0.538` n `158` status `ready` deltaP `10.3899` edge `0.0344` maxDD `-3.4775`
- `market_context_high->equity_1h` score `-0.5813` n `158` status `ready` deltaP `5.7172` edge `0.0569` maxDD `-8.8965`
- `market_context_high->fx_24h` score `-0.6327` n `150` status `ready` deltaP `7.7631` edge `0.0151` maxDD `-3.5661`
- `market_context_high->metal_1h` score `-0.9459` n `158` status `ready` deltaP `1.4288` edge `0.0162` maxDD `-1.0307`
- `market_context_high->unknown_1h` score `-0.9587` n `158` status `ready` deltaP `0.0815` edge `-0.0611` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.1923` n `158` status `ready` deltaP `1.5938` edge `0.0463` maxDD `-10.1158`
- `market_context_high->equity_4h` score `-1.5697` n `158` status `ready` deltaP `3.1007` edge `0.2148` maxDD `-21.9375`
- `market_context_high->metal_4h` score `-1.5863` n `158` status `ready` deltaP `-0.7023` edge `0.0495` maxDD `-4.8549`
- `market_context_high->crypto_major_4h` score `-1.7741` n `158` status `ready` deltaP `5.8486` edge `0.0505` maxDD `-17.6887`
- `market_context_high->fx_4h` score `-2.2463` n `158` status `ready` deltaP `-2.5239` edge `-0.0019` maxDD `-2.1439`
- `market_context_high->unknown_4h` score `-2.6109` n `158` status `ready` deltaP `10.1999` edge `-0.1682` maxDD `-6.0958`
- `market_context_high->metal_24h` score `-3.0755` n `151` status `ready` deltaP `-4.2023` edge `0.0866` maxDD `-13.5636`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

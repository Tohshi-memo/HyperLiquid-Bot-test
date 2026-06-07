# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T00:52:22.874387+00:00`
- Price records: `672`
- Market context records: `3129`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7125`

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

- `market_context_high->commodity_24h` score `14.213` n `106` status `ready` deltaP `47.5858` edge `0.91` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.6372` n `106` status `ready` deltaP `20.7842` edge `0.88` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `10.7327` n `106` status `ready` deltaP `9.8991` edge `2.3076` maxDD `-71.142`
- `market_context_high->index_24h` score `6.4297` n `106` status `ready` deltaP `30.3557` edge `0.8774` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.3048` n `106` status `ready` deltaP `10.682` edge `1.3223` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.0783` n `132` status `ready` deltaP `19.8032` edge `0.1703` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.0572` n `144` status `ready` deltaP `3.0647` edge `0.0266` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4273` n `144` status `ready` deltaP `4.8736` edge `0.019` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.4669` n `106` status `ready` deltaP `5.3328` edge `-0.0017` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.5073` n `144` status `ready` deltaP `5.4183` edge `0.1118` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.8798` n `144` status `ready` deltaP `2.3827` edge `0.0199` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.0701` n `144` status `ready` deltaP `2.4742` edge `0.0726` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.2049` n `144` status `ready` deltaP `-12.0925` edge `-0.0056` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.2535` n `132` status `ready` deltaP `11.5207` edge `0.0534` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4998` n `132` status `ready` deltaP `-14.5326` edge `-0.0086` maxDD `-1.2769`
- `market_context_high->metal_1h` score `-2.0297` n `144` status `ready` deltaP `-4.0461` edge `-0.0028` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.2444` n `132` status `ready` deltaP `3.2982` edge `0.0132` maxDD `-14.7778`
- `market_context_high->unknown_1h` score `-3.0806` n `144` status `ready` deltaP `1.9087` edge `-0.0668` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.1399` n `132` status `ready` deltaP `16.4449` edge `0.2923` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.4956` n `132` status `ready` deltaP `10.0055` edge `0.0157` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

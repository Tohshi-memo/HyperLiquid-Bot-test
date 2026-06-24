# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T03:52:25.803621+00:00`
- Price records: `672`
- Market context records: `4584`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9993`

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

- `market_context_high->unknown_1h` score `70.0038` n `157` status `ready` deltaP `6.7347` edge `5.8388` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.7327` n `157` status `ready` deltaP `8.3696` edge `0.3763` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.6188` n `157` status `ready` deltaP `4.1566` edge `0.0012` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6392` n `157` status `ready` deltaP `0.9497` edge `0.02` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.7741` n `157` status `ready` deltaP `-0.8467` edge `-0.0034` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8111` n `157` status `ready` deltaP `2.6536` edge `-0.0094` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8548` n `157` status `ready` deltaP `-1.8889` edge `0.0017` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.0961` n `157` status `ready` deltaP `2.1147` edge `0.0223` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.193` n `157` status `ready` deltaP `3.6614` edge `0.0334` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5684` n `157` status `ready` deltaP `-2.8252` edge `-0.011` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.2516` n `155` status `ready` deltaP `1.875` edge `-0.1078` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.8987` n `157` status `ready` deltaP `-3.8055` edge `-0.0811` maxDD `-17.8795`
- `market_context_high->index_24h` score `-5.1543` n `155` status `ready` deltaP `-6.4976` edge `-0.08` maxDD `-29.3321`
- `market_context_high->fx_24h` score `-5.2426` n `155` status `ready` deltaP `-11.4684` edge `-0.0092` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.4428` n `157` status `ready` deltaP `-2.2264` edge `-0.11` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.9169` n `155` status `ready` deltaP `8.3815` edge `0.0355` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.7015` n `157` status `ready` deltaP `-5.9365` edge `-0.1436` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-8.9994` n `157` status `ready` deltaP `-3.1876` edge `-0.2668` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.1483` n `157` status `ready` deltaP `-6.9054` edge `-0.3333` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.9112` n `157` status `ready` deltaP `-3.4217` edge `-0.4099` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

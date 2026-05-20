# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T12:22:18.753155+00:00`
- Price records: `672`
- Market context records: `1320`
- Flow alert records: `5712`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8783`

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

- `market_context_high->crypto_major_24h` score `16.1106` n `128` status `ready` deltaP `38.9756` edge `1.1959` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.475` n `128` status `ready` deltaP `13.7153` edge `1.1982` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.7152` n `128` status `ready` deltaP `28.3854` edge `0.822` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.6084` n `128` status `ready` deltaP `29.3403` edge `0.3804` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.3693` n `128` status `ready` deltaP `22.2222` edge `0.5165` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.4221` n `157` status `ready` deltaP `12.501` edge `0.189` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `1.9079` n `128` status `ready` deltaP `-1.0417` edge `0.4389` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.2452` n `128` status `ready` deltaP `-13.1944` edge `0.3399` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.9902` n `128` status `ready` deltaP `11.5452` edge `0.052` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.2008` n `157` status `ready` deltaP `3.5174` edge `0.036` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1164` n `157` status `ready` deltaP `5.1791` edge `0.0893` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.0898` n `157` status `ready` deltaP `5.763` edge `0.0185` maxDD `-1.6329`
- `market_context_high->metal_4h` score `0.0889` n `157` status `ready` deltaP `12.9156` edge `0.0644` maxDD `-6.4478`
- `market_context_high->metal_1h` score `-0.093` n `157` status `ready` deltaP `8.6426` edge `0.0036` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.5505` n `157` status `ready` deltaP `0.5092` edge `-0.0037` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5941` n `157` status `ready` deltaP `0.697` edge `0.0329` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.8229` n `157` status `ready` deltaP `10.6018` edge `0.1927` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.9023` n `157` status `ready` deltaP `-1.2167` edge `-0.0055` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.9127` n `157` status `ready` deltaP `4.0207` edge `0.0833` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-0.9593` n `157` status `ready` deltaP `-2.0033` edge `-0.0051` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

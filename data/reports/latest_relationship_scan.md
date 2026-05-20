# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T11:37:18.818598+00:00`
- Price records: `672`
- Market context records: `1317`
- Flow alert records: `5702`
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

- `market_context_high->crypto_major_24h` score `16.3154` n `128` status `ready` deltaP `39.4965` edge `1.2095` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.3758` n `128` status `ready` deltaP `13.1944` edge `1.1934` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.6744` n `128` status `ready` deltaP `28.3854` edge `0.8186` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.7281` n `128` status `ready` deltaP `29.8611` edge `0.3869` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.5181` n `128` status `ready` deltaP `22.7431` edge `0.5321` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.4971` n `157` status `ready` deltaP `12.9583` edge `0.1922` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.0131` n `128` status `ready` deltaP `-0.5208` edge `0.4442` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.152` n `128` status `ready` deltaP `-13.7153` edge `0.3356` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.9317` n `128` status `ready` deltaP `11.0244` edge `0.0506` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.2428` n `157` status `ready` deltaP `3.8169` edge `0.0375` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1527` n `157` status `ready` deltaP `5.6364` edge `0.0909` maxDD `-3.7119`
- `market_context_high->metal_4h` score `0.1289` n `157` status `ready` deltaP `13.2205` edge `0.0657` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.1201` n `157` status `ready` deltaP `6.2121` edge `0.0194` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0942` n `157` status `ready` deltaP `8.6426` edge `0.0035` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.5242` n `157` status `ready` deltaP `0.8086` edge `-0.0035` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6049` n `157` status `ready` deltaP `0.697` edge `0.032` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.8447` n `157` status `ready` deltaP `10.4493` edge `0.1919` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.9008` n `157` status `ready` deltaP `-1.2167` edge `-0.0053` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.9261` n `157` status `ready` deltaP `3.8683` edge `0.0826` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-0.9784` n `157` status `ready` deltaP `-2.153` edge `-0.0057` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

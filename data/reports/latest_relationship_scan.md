# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T11:52:15.517623+00:00`
- Price records: `672`
- Market context records: `1318`
- Flow alert records: `5705`
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

- `market_context_high->crypto_major_24h` score `16.2475` n `128` status `ready` deltaP `39.3229` edge `1.205` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.4053` n `128` status `ready` deltaP `13.3681` edge `1.1947` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.69` n `128` status `ready` deltaP `28.3854` edge `0.8199` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.6902` n `128` status `ready` deltaP `29.6875` edge `0.3849` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.4693` n `128` status `ready` deltaP `22.5694` edge `0.527` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.4765` n `157` status `ready` deltaP `12.8058` edge `0.1915` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `1.9837` n `128` status `ready` deltaP `-0.6944` edge `0.4429` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.1886` n `128` status `ready` deltaP `-13.5417` edge `0.3375` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.9516` n `128` status `ready` deltaP `11.198` edge `0.0511` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.2428` n `157` status `ready` deltaP `3.8169` edge `0.0375` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1417` n `157` status `ready` deltaP `5.4839` edge `0.0905` maxDD `-3.7119`
- `market_context_high->metal_4h` score `0.1217` n `157` status `ready` deltaP `13.2205` edge `0.0651` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.1108` n `157` status `ready` deltaP `6.0624` edge `0.0192` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0954` n `157` status `ready` deltaP `8.6426` edge `0.0034` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.5254` n `157` status `ready` deltaP `0.8086` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5989` n `157` status `ready` deltaP `0.697` edge `0.0325` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.8229` n `157` status `ready` deltaP `10.6018` edge `0.1927` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.9008` n `157` status `ready` deltaP `-1.2167` edge `-0.0053` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.9119` n `157` status `ready` deltaP `4.0207` edge `0.0834` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-0.982` n `157` status `ready` deltaP `-2.153` edge `-0.006` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T15:22:18.496234+00:00`
- Price records: `672`
- Market context records: `1332`
- Flow alert records: `5748`
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

- `market_context_high->crypto_major_24h` score `15.1555` n `128` status `ready` deltaP `36.8923` edge `1.1302` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.2436` n `128` status `ready` deltaP `12.8472` edge `1.1847` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.624` n `128` status `ready` deltaP `28.3854` edge `0.8144` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.9881` n `128` status `ready` deltaP `27.2569` edge `0.3426` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6994` n `128` status `ready` deltaP `20.1389` edge `0.4445` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3243` n `157` status `ready` deltaP `12.0436` edge `0.1839` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `1.8787` n `128` status `ready` deltaP `-11.1111` edge `0.3788` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `1.3116` n `128` status `ready` deltaP `-3.125` edge `0.4031` maxDD `-10.1706`
- `market_context_high->fx_24h` score `1.2156` n `128` status `ready` deltaP `13.6285` edge `0.0569` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.1871` n `157` status `ready` deltaP `13.6778` edge `0.0675` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.1445` n `157` status `ready` deltaP `3.218` edge `0.0333` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.0624` n `157` status `ready` deltaP `4.8742` edge `0.0844` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.022` n `157` status `ready` deltaP `5.0145` edge `0.0148` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0919` n `157` status `ready` deltaP `9.0917` edge `0.0007` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4739` n `157` status `ready` deltaP `1.4074` edge `-0.0033` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6936` n `157` status `ready` deltaP `0.3976` edge `0.0266` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.8262` n `157` status `ready` deltaP `-1.4045` edge `0.002` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-0.9935` n `157` status `ready` deltaP `-2.1149` edge `-0.0112` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-1.1758` n `157` status `ready` deltaP `2.8012` edge `0.0577` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.2039` n `157` status `ready` deltaP `9.2298` edge `0.1701` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

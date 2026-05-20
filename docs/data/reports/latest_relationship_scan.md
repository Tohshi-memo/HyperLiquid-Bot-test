# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T09:52:15.035216+00:00`
- Price records: `672`
- Market context records: `1309`
- Flow alert records: `5681`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8781`

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

- `market_context_high->crypto_major_24h` score `16.7498` n `128` status `ready` deltaP `40.7118` edge `1.2376` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.1448` n `128` status `ready` deltaP `12.1528` edge `1.1811` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.5844` n `128` status `ready` deltaP `28.3854` edge `0.8111` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.9633` n `128` status `ready` deltaP `31.0764` edge `0.3984` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.8285` n `128` status `ready` deltaP `23.9583` edge `0.5638` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.5729` n `157` status `ready` deltaP `13.1107` edge `0.1975` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.1556` n `128` status `ready` deltaP `0.0` edge `0.4526` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.9263` n `128` status `ready` deltaP `-14.9306` edge `0.3249` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.7901` n `128` status `ready` deltaP `9.8091` edge `0.0469` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.208` n `157` status `ready` deltaP `3.6671` edge `0.0356` maxDD `-1.7505`
- `market_context_high->metal_4h` score `0.1977` n `157` status `ready` deltaP `13.5253` edge `0.0694` maxDD `-6.4478`
- `market_context_high->index_4h` score `0.1896` n `157` status `ready` deltaP `5.9413` edge `0.0936` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.1014` n `157` status `ready` deltaP `6.0624` edge `0.018` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0847` n `157` status `ready` deltaP `8.7923` edge `0.0033` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4978` n `157` status `ready` deltaP `1.108` edge `-0.0033` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6301` n `157` status `ready` deltaP `0.5473` edge `0.0309` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.8593` n `157` status `ready` deltaP `10.2969` edge `0.1917` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.907` n `157` status `ready` deltaP `-1.3664` edge `-0.0051` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.9529` n `157` status `ready` deltaP `3.5634` edge `0.0812` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-1.0072` n `157` status `ready` deltaP `-2.3027` edge `-0.0071` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

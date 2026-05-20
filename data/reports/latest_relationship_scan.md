# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T16:52:33.915756+00:00`
- Price records: `672`
- Market context records: `1339`
- Flow alert records: `5767`
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

- `market_context_high->crypto_major_24h` score `14.651` n `128` status `ready` deltaP `35.8506` edge `1.0951` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.0313` n `128` status `ready` deltaP `11.9792` edge `1.1728` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.4908` n `128` status `ready` deltaP `28.3854` edge `0.8033` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.6648` n `128` status `ready` deltaP `26.2153` edge `0.3226` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.3987` n `128` status `ready` deltaP `19.0972` edge `0.4129` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `2.316` n `128` status `ready` deltaP `-10.0694` edge `0.4083` maxDD `-6.8535`
- `market_context_high->equity_4h` score `2.252` n `157` status `ready` deltaP `11.7388` edge `0.1799` maxDD `-3.6396`
- `market_context_high->fx_24h` score `1.2813` n `128` status `ready` deltaP `14.1494` edge `0.0589` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.9823` n `128` status `ready` deltaP `-4.1667` edge `0.3826` maxDD `-10.1706`
- `market_context_high->metal_4h` score `0.1379` n `157` status `ready` deltaP `13.6778` edge `0.0634` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.0989` n `157` status `ready` deltaP `3.0683` edge `0.0305` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.0202` n `157` status `ready` deltaP `4.8742` edge `0.079` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.0017` n `157` status `ready` deltaP `4.7151` edge `0.0142` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0427` n `157` status `ready` deltaP `9.3911` edge `0.0028` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4739` n `157` status `ready` deltaP `1.4074` edge `-0.0033` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.7686` n `157` status `ready` deltaP `-1.1051` edge `0.0048` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8351` n `157` status `ready` deltaP `-0.2012` edge `0.0188` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.0512` n `157` status `ready` deltaP `-2.564` edge `-0.0156` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-1.3177` n `157` status `ready` deltaP `1.8866` edge `0.0456` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.4917` n `157` status `ready` deltaP `8.4676` edge `0.1512` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

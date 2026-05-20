# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T15:52:19.629207+00:00`
- Price records: `672`
- Market context records: `1334`
- Flow alert records: `5754`
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

- `market_context_high->crypto_major_24h` score `14.9777` n `128` status `ready` deltaP `36.5451` edge `1.1177` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.1582` n `128` status `ready` deltaP `12.5` edge `1.1799` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.57` n `128` status `ready` deltaP `28.3854` edge `0.8099` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.868` n `128` status `ready` deltaP `26.9097` edge `0.3349` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.5791` n `128` status `ready` deltaP `19.7917` edge `0.4314` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.2676` n `157` status `ready` deltaP `11.7388` edge `0.1812` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `2.0241` n `128` status `ready` deltaP `-10.7639` edge `0.3886` maxDD `-6.8535`
- `market_context_high->fx_24h` score `1.2518` n `128` status `ready` deltaP `13.9757` edge `0.0576` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `1.2118` n `128` status `ready` deltaP `-3.4722` edge `0.3971` maxDD `-10.1706`
- `market_context_high->metal_4h` score `0.1703` n `157` status `ready` deltaP `13.6778` edge `0.0661` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.0881` n `157` status `ready` deltaP `2.9186` edge `0.0306` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.0475` n `157` status `ready` deltaP `4.8742` edge `0.0825` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.0025` n `157` status `ready` deltaP `4.7151` edge `0.0143` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.1147` n `157` status `ready` deltaP `8.942` edge `-0.0002` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4607` n `157` status `ready` deltaP `1.5571` edge `-0.0032` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.7524` n `157` status `ready` deltaP `0.0982` edge `0.0237` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.7746` n `157` status `ready` deltaP `-1.1051` edge `0.0043` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-1.0239` n `157` status `ready` deltaP `-2.4143` edge `-0.0131` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-1.2252` n `157` status `ready` deltaP `2.4963` edge `0.0534` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.3243` n `157` status `ready` deltaP `8.9249` edge `0.1621` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T13:37:31.128339+00:00`
- Price records: `672`
- Market context records: `1325`
- Flow alert records: `5727`
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

- `market_context_high->crypto_major_24h` score `15.7579` n `128` status `ready` deltaP `38.1076` edge `1.1723` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.5021` n `128` status `ready` deltaP `13.8889` edge `1.1993` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.7248` n `128` status `ready` deltaP `28.3854` edge `0.8228` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.4178` n `128` status `ready` deltaP `28.4722` edge `0.3703` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.1315` n `128` status `ready` deltaP `21.3542` edge `0.4918` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3266` n `157` status `ready` deltaP `11.8912` edge `0.1851` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `1.6896` n `128` status `ready` deltaP `-1.9097` edge `0.4265` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.4887` n `128` status `ready` deltaP `-12.3264` edge `0.3544` maxDD `-6.8535`
- `market_context_high->fx_24h` score `1.0848` n `128` status `ready` deltaP `12.4132` edge `0.0541` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.1447` n `157` status `ready` deltaP `13.3729` edge `0.066` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.1433` n `157` status `ready` deltaP `3.0683` edge `0.0342` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.0943` n `157` status `ready` deltaP `4.8742` edge `0.0885` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.0625` n `157` status `ready` deltaP `5.3139` edge `0.018` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0259` n `157` status `ready` deltaP `9.2414` edge `0.0052` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.5254` n `157` status `ready` deltaP `0.8086` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6073` n `157` status `ready` deltaP `0.5473` edge `0.0328` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.9257` n `157` status `ready` deltaP `-1.8536` edge `-0.0033` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-0.9272` n `157` status `ready` deltaP `-1.5161` edge `-0.0067` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.9461` n `157` status `ready` deltaP `9.992` edge `0.1865` maxDD `-19.5565`
- `market_context_high->unknown_4h` score `-0.9761` n `157` status `ready` deltaP `3.7158` edge `0.0772` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

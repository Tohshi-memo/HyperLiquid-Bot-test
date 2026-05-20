# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T19:52:19.416013+00:00`
- Price records: `672`
- Market context records: `1351`
- Flow alert records: `5804`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8793`

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

- `market_context_high->crypto_major_24h` score `13.7307` n `128` status `ready` deltaP `33.7673` edge `1.0323` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.7463` n `128` status `ready` deltaP `11.8056` edge `1.1502` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.3708` n `128` status `ready` deltaP `28.3854` edge `0.7933` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1501` n `128` status `ready` deltaP `24.1319` edge `0.2936` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.2567` n `128` status `ready` deltaP `-7.9861` edge `0.4728` maxDD `-6.8535`
- `market_context_high->equity_4h` score `2.2664` n `157` status `ready` deltaP `11.7388` edge `0.1811` maxDD `-3.6396`
- `market_context_high->equity_24h` score `1.9628` n `128` status `ready` deltaP `17.0139` edge `0.3709` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.502` n `128` status `ready` deltaP `16.2327` edge `0.0634` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.584` n `128` status `ready` deltaP `-5.0347` edge `0.3552` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.1106` n `163` status `ready` deltaP `5.6437` edge `0.017` maxDD `-1.6329`
- `market_context_high->metal_4h` score `0.0423` n `157` status `ready` deltaP `13.068` edge `0.0595` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.0067` n `163` status `ready` deltaP `2.3061` edge `0.0279` maxDD `-1.7505`
- `market_context_high->index_4h` score `-0.0071` n `157` status `ready` deltaP `4.8742` edge `0.0755` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.1281` n `163` status `ready` deltaP `8.5789` edge `0.0011` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.3417` n `163` status `ready` deltaP `2.9692` edge `-0.0027` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5621` n `163` status `ready` deltaP `0.4711` edge `0.0115` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.9205` n `163` status `ready` deltaP `-0.653` edge `0.0147` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1881` n `163` status `ready` deltaP `-3.6148` edge `-0.0217` maxDD `-6.1883`
- `market_context_high->unknown_4h` score `-1.3922` n `157` status `ready` deltaP `1.4292` edge `0.0391` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.4029` n `157` status `ready` deltaP `8.4676` edge `0.1586` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

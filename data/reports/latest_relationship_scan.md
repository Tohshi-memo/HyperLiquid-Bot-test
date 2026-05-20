# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T18:37:20.348404+00:00`
- Price records: `672`
- Market context records: `1346`
- Flow alert records: `5789`
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

- `market_context_high->crypto_major_24h` score `14.1037` n `128` status `ready` deltaP `34.6354` edge `1.0576` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.8723` n `128` status `ready` deltaP `11.8056` edge `1.1607` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.4176` n `128` status `ready` deltaP `28.3854` edge `0.7972` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.3924` n `128` status `ready` deltaP `25.0` edge `0.308` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `2.8752` n `128` status `ready` deltaP `-8.8542` edge `0.4468` maxDD `-6.8535`
- `market_context_high->equity_4h` score `2.216` n `157` status `ready` deltaP `11.7388` edge `0.1769` maxDD `-3.6396`
- `market_context_high->equity_24h` score `2.1694` n `128` status `ready` deltaP `17.8819` edge `0.3916` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.4121` n `128` status `ready` deltaP `15.3646` edge `0.0617` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.6872` n `128` status `ready` deltaP `-5.0347` edge `0.3638` maxDD `-10.1706`
- `market_context_high->equity_1h` score `0.1004` n `158` status `ready` deltaP `3.1323` edge `0.0302` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.0064` n `158` status `ready` deltaP `4.745` edge `0.0146` maxDD `-1.6329`
- `market_context_high->index_4h` score `-0.0086` n `157` status `ready` deltaP `4.8742` edge `0.0753` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-0.0225` n `157` status `ready` deltaP `13.068` edge `0.0541` maxDD `-6.4478`
- `market_context_high->metal_1h` score `-0.075` n `158` status `ready` deltaP `9.1678` edge `0.0016` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4228` n `158` status `ready` deltaP `2.0011` edge `-0.003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.708` n `158` status `ready` deltaP `-0.7826` edge `0.0077` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.9405` n `158` status `ready` deltaP `-0.8432` edge `0.0143` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1423` n `158` status `ready` deltaP `-3.4772` edge `-0.0212` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-1.3844` n `157` status `ready` deltaP `1.4292` edge `0.0401` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.5337` n `157` status `ready` deltaP `8.4676` edge `0.1477` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

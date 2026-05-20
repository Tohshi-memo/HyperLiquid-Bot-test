# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T12:37:18.843081+00:00`
- Price records: `672`
- Market context records: `1321`
- Flow alert records: `5715`
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

- `market_context_high->crypto_major_24h` score `16.0391` n `128` status `ready` deltaP `38.802` edge `1.1911` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.5057` n `128` status `ready` deltaP `13.8889` edge `1.1996` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.7212` n `128` status `ready` deltaP `28.3854` edge `0.8225` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.5705` n `128` status `ready` deltaP `29.1667` edge `0.3784` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.3189` n `128` status `ready` deltaP `22.0486` edge `0.5112` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3931` n `157` status `ready` deltaP `12.3485` edge `0.1876` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `1.8724` n `128` status `ready` deltaP `-1.2153` edge `0.4371` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.2891` n `128` status `ready` deltaP `-13.0208` edge `0.3424` maxDD `-6.8535`
- `market_context_high->fx_24h` score `1.0088` n `128` status `ready` deltaP `11.7188` edge `0.0524` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.178` n `157` status `ready` deltaP `3.3677` edge `0.0351` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1062` n `157` status `ready` deltaP `5.0266` edge `0.089` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.0804` n `157` status `ready` deltaP `5.6133` edge `0.0183` maxDD `-1.6329`
- `market_context_high->metal_4h` score `0.0719` n `157` status `ready` deltaP `12.7631` edge `0.064` maxDD `-6.4478`
- `market_context_high->metal_1h` score `-0.0787` n `157` status `ready` deltaP `8.7923` edge `0.0038` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.5505` n `157` status `ready` deltaP `0.5092` edge `-0.0037` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5881` n `157` status `ready` deltaP `0.697` edge `0.0334` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.8423` n `157` status `ready` deltaP `10.4493` edge `0.1921` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.9023` n `157` status `ready` deltaP `-1.2167` edge `-0.0055` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.9119` n `157` status `ready` deltaP `4.0207` edge `0.0834` maxDD `-11.1695`
- `market_context_high->commodity_1h` score `-0.9353` n `157` status `ready` deltaP `-1.8536` edge `-0.0041` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

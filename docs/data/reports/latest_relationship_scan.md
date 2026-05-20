# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T19:37:18.474024+00:00`
- Price records: `672`
- Market context records: `1350`
- Flow alert records: `5801`
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

- `market_context_high->crypto_major_24h` score `13.8094` n `128` status `ready` deltaP `33.9409` edge `1.0377` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.7691` n `128` status `ready` deltaP `11.8056` edge `1.1521` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.3816` n `128` status `ready` deltaP `28.3854` edge `0.7942` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.2012` n `128` status `ready` deltaP `24.3056` edge `0.2967` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.1828` n `128` status `ready` deltaP `-8.1597` edge `0.4678` maxDD `-6.8535`
- `market_context_high->equity_4h` score `2.2544` n `157` status `ready` deltaP `11.7388` edge `0.1801` maxDD `-3.6396`
- `market_context_high->equity_24h` score `2.0069` n `128` status `ready` deltaP `17.1875` edge `0.3754` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.4833` n `128` status `ready` deltaP `16.0591` edge `0.063` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.6296` n `128` status `ready` deltaP `-5.0347` edge `0.359` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.0906` n `162` status `ready` deltaP `5.4392` edge `0.0167` maxDD `-1.6329`
- `market_context_high->metal_4h` score `0.0207` n `157` status `ready` deltaP `13.068` edge `0.0577` maxDD `-6.4478`
- `market_context_high->index_4h` score `-0.0086` n `157` status `ready` deltaP `4.8742` edge `0.0753` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0118` n `162` status `ready` deltaP `2.0902` edge `0.0278` maxDD `-1.7505`
- `market_context_high->metal_1h` score `-0.1325` n `162` status `ready` deltaP `8.5089` edge `0.0012` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.3507` n `162` status `ready` deltaP `2.8425` edge `-0.0026` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5768` n `162` status `ready` deltaP `0.3179` edge `0.0113` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.9756` n `162` status `ready` deltaP `-0.937` edge `0.012` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.2247` n `162` status `ready` deltaP `-3.9292` edge `-0.0243` maxDD `-6.1883`
- `market_context_high->unknown_4h` score `-1.3805` n `157` status `ready` deltaP `1.4292` edge `0.0406` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.4329` n `157` status `ready` deltaP `8.4676` edge `0.1561` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

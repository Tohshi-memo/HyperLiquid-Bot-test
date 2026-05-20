# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T16:23:42.074381+00:00`
- Price records: `672`
- Market context records: `1337`
- Flow alert records: `5760`
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

- `market_context_high->crypto_major_24h` score `14.8035` n `128` status `ready` deltaP `36.1979` edge `1.1055` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.0975` n `128` status `ready` deltaP `12.3264` edge `1.176` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.516` n `128` status `ready` deltaP `28.3854` edge `0.8054` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.7574` n `128` status `ready` deltaP `26.5625` edge `0.328` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4745` n `128` status `ready` deltaP `19.4444` edge `0.4203` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.2532` n `157` status `ready` deltaP `11.7388` edge `0.18` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `2.1634` n `128` status `ready` deltaP `-10.4167` edge `0.3979` maxDD `-6.8535`
- `market_context_high->fx_24h` score `1.2741` n `128` status `ready` deltaP `14.1494` edge `0.0583` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `1.1205` n `128` status `ready` deltaP `-3.8194` edge `0.3918` maxDD `-10.1706`
- `market_context_high->metal_4h` score `0.1523` n `157` status `ready` deltaP `13.6778` edge `0.0646` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.0629` n `157` status `ready` deltaP `2.7689` edge `0.0295` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.0327` n `157` status `ready` deltaP `4.8742` edge `0.0806` maxDD `-3.7119`
- `market_context_high->index_1h` score `-0.0076` n `157` status `ready` deltaP `4.5654` edge `0.014` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0919` n `157` status `ready` deltaP `9.0917` edge `0.0007` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4607` n `157` status `ready` deltaP `1.5571` edge `-0.0032` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.7662` n `157` status `ready` deltaP `-1.1051` edge `0.005` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8112` n `157` status `ready` deltaP `-0.0515` edge `0.0198` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.048` n `157` status `ready` deltaP `-2.564` edge `-0.0152` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-1.2637` n `157` status `ready` deltaP `2.1914` edge `0.0505` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-1.4399` n `157` status `ready` deltaP `8.62` edge `0.1545` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

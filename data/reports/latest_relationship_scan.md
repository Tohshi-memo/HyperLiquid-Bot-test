# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T21:42:24.855562+00:00`
- Price records: `672`
- Market context records: `1157`
- Flow alert records: `5233`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `20.363` n `146` status `ready` deltaP `44.6561` edge `1.5124` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.936` n `146` status `ready` deltaP `21.0355` edge `0.8894` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.7923` n `146` status `ready` deltaP `20.5146` edge `0.6056` maxDD `-6.4404`
- `market_context_high->index_24h` score `6.0867` n `146` status `ready` deltaP `19.1258` edge `0.4355` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.5967` n `146` status `ready` deltaP `-2.4734` edge `0.6496` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.4664` n `162` status `ready` deltaP `12.2045` edge `0.1905` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1694` n `162` status `ready` deltaP `9.263` edge `0.104` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4914` n `162` status `ready` deltaP `7.5515` edge `0.0223` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3443` n `162` status `ready` deltaP `3.249` edge `0.0448` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.1954` n `162` status `ready` deltaP `8.6345` edge `0.1596` maxDD `-8.3693`
- `market_context_high->fx_1h` score `0.139` n `162` status `ready` deltaP `8.4535` edge `0.0008` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0512` n `162` status `ready` deltaP `7.2947` edge `0.0345` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.2941` n `162` status `ready` deltaP `2.7852` edge `0.0412` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.3418` n `162` status `ready` deltaP `6.2634` edge `-0.0092` maxDD `-2.2164`
- `market_context_high->commodity_1h` score `-0.815` n `162` status `ready` deltaP `-2.9552` edge `-0.004` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.9038` n `162` status `ready` deltaP `-2.089` edge `-0.0023` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.0049` n `162` status `ready` deltaP `5.8284` edge `0.1288` maxDD `-16.7194`
- `market_context_high->unknown_24h` score `-1.3935` n `146` status `ready` deltaP `3.8313` edge `0.1313` maxDD `-10.1706`
- `market_context_high->metal_4h` score `-1.6745` n `162` status `ready` deltaP `6.4683` edge `-0.0624` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.2126` n `162` status `ready` deltaP `7.7499` edge `-0.1144` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

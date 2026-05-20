# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T07:37:15.413207+00:00`
- Price records: `672`
- Market context records: `1300`
- Flow alert records: `5653`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8780`

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

- `market_context_high->crypto_major_24h` score `17.205` n `128` status `ready` deltaP `41.4062` edge `1.2709` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.697` n `128` status `ready` deltaP `10.5903` edge `1.1542` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.5646` n `128` status `ready` deltaP `28.2118` edge `0.8106` maxDD `-15.1306`
- `market_context_high->index_24h` score `6.0247` n `128` status `ready` deltaP `31.4236` edge `0.4012` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0591` n `128` status `ready` deltaP `25.3472` edge `0.5841` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.4971` n `154` status `ready` deltaP `12.7633` edge `0.1935` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.2839` n `128` status `ready` deltaP `0.8681` edge `0.4575` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.7861` n `128` status `ready` deltaP `-15.7986` edge `0.319` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.6039` n `128` status `ready` deltaP `8.2466` edge `0.0418` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.1888` n `157` status `ready` deltaP `3.5174` edge `0.035` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1341` n `154` status `ready` deltaP `5.3829` edge `0.0902` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.103` n `157` status `ready` deltaP `6.0624` edge `0.0182` maxDD `-1.6329`
- `market_context_high->metal_4h` score `0.0728` n `154` status `ready` deltaP `12.8801` edge `0.0633` maxDD `-6.4478`
- `market_context_high->metal_1h` score `-0.0199` n `157` status `ready` deltaP `9.3911` edge `0.0047` maxDD `-2.8509`
- `market_context_high->unknown_4h` score `-0.4192` n `154` status `ready` deltaP `3.4605` edge `0.1503` maxDD `-11.1695`
- `market_context_high->fx_1h` score `-0.4727` n `157` status `ready` deltaP `1.4074` edge `-0.0032` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6049` n `157` status `ready` deltaP `0.697` edge `0.032` maxDD `-3.6309`
- `market_context_high->crypto_major_4h` score `-0.7925` n `154` status `ready` deltaP `5.8323` edge `0.1304` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-0.8509` n `157` status `ready` deltaP `-0.6179` edge `-0.0029` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.9316` n `154` status `ready` deltaP `10.249` edge `0.186` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

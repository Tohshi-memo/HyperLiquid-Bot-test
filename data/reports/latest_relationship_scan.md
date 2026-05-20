# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T08:07:14.831669+00:00`
- Price records: `672`
- Market context records: `1302`
- Flow alert records: `5659`
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

- `market_context_high->crypto_major_24h` score `17.1258` n `128` status `ready` deltaP `41.4062` edge `1.2643` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.8196` n `128` status `ready` deltaP `10.9375` edge `1.1621` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.5658` n `128` status `ready` deltaP `28.2118` edge `0.8107` maxDD `-15.1306`
- `market_context_high->index_24h` score `6.0614` n `128` status `ready` deltaP `31.5972` edge `0.4031` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0438` n `128` status `ready` deltaP `25.1736` edge `0.5833` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.5794` n `156` status `ready` deltaP `12.9964` edge `0.1988` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.2309` n `128` status `ready` deltaP `0.5208` edge `0.4554` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.7566` n `128` status `ready` deltaP `-15.9722` edge `0.3177` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.6448` n `128` status `ready` deltaP `8.5938` edge `0.0429` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.1939` n `156` status `ready` deltaP `13.313` edge `0.0705` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.1876` n `157` status `ready` deltaP `3.5174` edge `0.0349` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1777` n `156` status `ready` deltaP `5.7575` edge `0.0933` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.103` n `157` status `ready` deltaP `6.0624` edge `0.0182` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0343` n `157` status `ready` deltaP `9.2414` edge `0.0045` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4727` n `157` status `ready` deltaP `1.4074` edge `-0.0032` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5845` n `157` status `ready` deltaP `0.8467` edge `0.0327` maxDD `-3.6309`
- `market_context_high->unknown_4h` score `-0.7358` n `156` status `ready` deltaP `3.8383` edge `0.1072` maxDD `-11.1695`
- `market_context_high->crypto_alt_4h` score `-0.8306` n `156` status `ready` deltaP `10.3854` edge `0.1935` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.8486` n `157` status `ready` deltaP `-0.6179` edge `-0.0026` maxDD `-5.8323`
- `market_context_high->commodity_1h` score `-1.0324` n `157` status `ready` deltaP `-2.4524` edge `-0.0082` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

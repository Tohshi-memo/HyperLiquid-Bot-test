# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T06:07:18.742570+00:00`
- Price records: `672`
- Market context records: `1293`
- Flow alert records: `5635`
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

- `market_context_high->crypto_major_24h` score `17.4277` n `128` status `ready` deltaP `41.5798` edge `1.2883` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.2345` n `128` status `ready` deltaP `9.5486` edge `1.1226` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.4039` n `128` status `ready` deltaP `27.3437` edge `0.803` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.8285` n `128` status `ready` deltaP `30.3819` edge `0.3918` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0037` n `128` status `ready` deltaP `25.3472` edge `0.577` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3926` n `151` status `ready` deltaP `12.4021` edge `0.1872` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3562` n `128` status `ready` deltaP `1.5625` edge `0.4589` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.9784` n `128` status `ready` deltaP `-15.1042` edge `0.3304` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.4857` n `128` status `ready` deltaP `7.2049` edge `0.0389` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.1948` n `157` status `ready` deltaP `3.5174` edge `0.0355` maxDD `-1.7505`
- `market_context_high->unknown_4h` score `0.1716` n `151` status `ready` deltaP `3.3174` edge `0.2193` maxDD `-11.1695`
- `market_context_high->index_1h` score `0.11` n `157` status `ready` deltaP `6.2121` edge `0.0181` maxDD `-1.6329`
- `market_context_high->index_4h` score `0.1031` n `151` status `ready` deltaP `5.3121` edge `0.0867` maxDD `-3.7119`
- `market_context_high->metal_1h` score `0.0855` n `157` status `ready` deltaP `10.1396` edge `0.0085` maxDD `-2.8509`
- `market_context_high->metal_4h` score `0.0429` n `151` status `ready` deltaP `12.9714` edge `0.0602` maxDD `-6.4478`
- `market_context_high->fx_1h` score `-0.5373` n `157` status `ready` deltaP `0.6589` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.6037` n `157` status `ready` deltaP `0.8467` edge `0.0311` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.6907` n `151` status `ready` deltaP `9.8702` edge `0.1776` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.8248` n `151` status `ready` deltaP `5.7665` edge `0.1267` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-0.826` n `157` status `ready` deltaP `-0.3185` edge `-0.0017` maxDD `-5.8323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

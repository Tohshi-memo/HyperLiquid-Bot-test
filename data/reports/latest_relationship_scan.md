# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T13:07:23.106635+00:00`
- Price records: `672`
- Market context records: `1425`
- Flow alert records: `6018`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8785`

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

- `market_context_high->crypto_major_24h` score `11.774` n `154` status `ready` deltaP `27.3539` edge `0.912` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.7281` n `154` status `ready` deltaP `28.7811` edge `0.9871` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.6761` n `154` status `ready` deltaP `11.9882` edge `1.0598` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.8157` n `154` status `ready` deltaP `19.3813` edge `0.2974` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6559` n `154` status `ready` deltaP `12.5271` edge `0.3705` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.9364` n `202` status `ready` deltaP `5.3897` edge `0.1251` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0683` n `154` status `ready` deltaP `9.3592` edge `0.0482` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.2294` n `211` status `ready` deltaP `2.8032` edge `0.0087` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.3267` n `211` status `ready` deltaP `1.9794` edge `0.0196` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.4297` n `211` status `ready` deltaP `1.9575` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.6223` n `211` status `ready` deltaP `-0.3867` edge `0.0122` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.6852` n `202` status `ready` deltaP `-0.0151` edge `0.0519` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.8476` n `211` status `ready` deltaP `0.9344` edge `0.0255` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.953` n `211` status `ready` deltaP `3.6531` edge `-0.0144` maxDD `-6.2374`
- `market_context_high->crypto_alt_4h` score `-1.1668` n `202` status `ready` deltaP `7.954` edge `0.1817` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.283` n `202` status `ready` deltaP `5.29` edge `0.1287` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.6104` n `202` status `ready` deltaP `-4.1159` edge `-0.0097` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.857` n `211` status `ready` deltaP `-1.9589` edge `-0.006` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-2.6266` n `202` status `ready` deltaP `-10.2421` edge `-0.0138` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8061` n `202` status `ready` deltaP `4.3015` edge `-0.0027` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T08:07:18.054221+00:00`
- Price records: `672`
- Market context records: `1404`
- Flow alert records: `5956`
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

- `market_context_high->crypto_major_24h` score `12.3024` n `156` status `ready` deltaP `27.4038` edge `0.9557` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4817` n `156` status `ready` deltaP `28.8061` edge `0.9664` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.1834` n `156` status `ready` deltaP `10.5101` edge `1.0286` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.8118` n `156` status `ready` deltaP `19.4978` edge `0.2963` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.2334` n `156` status `ready` deltaP `12.6603` edge `0.3344` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0117` n `199` status `ready` deltaP `6.1811` edge `0.1261` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0614` n `156` status `ready` deltaP `9.7088` edge `0.0453` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0625` n `204` status `ready` deltaP `4.3502` edge `0.0123` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1423` n `204` status `ready` deltaP `2.7445` edge `0.0257` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2082` n `204` status `ready` deltaP `4.5761` edge `-0.0013` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.7092` n `204` status `ready` deltaP `4.9313` edge `-0.0063` maxDD `-5.0663`
- `market_context_high->crypto_alt_1h` score `-0.749` n `204` status `ready` deltaP `0.411` edge `0.0219` maxDD `-3.6309`
- `market_context_high->index_4h` score `-0.8026` n `199` status `ready` deltaP `-0.9277` edge `0.0482` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-0.8081` n `204` status `ready` deltaP `-1.3884` edge `0.0034` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-1.5472` n `204` status `ready` deltaP `-1.9725` edge `-0.0051` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.5489` n `199` status `ready` deltaP `-3.4525` edge `-0.009` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.5496` n `199` status `ready` deltaP `4.2828` edge `0.1132` maxDD `-13.3376`
- `market_context_high->crypto_alt_4h` score `-1.6249` n `199` status `ready` deltaP `5.497` edge `0.1599` maxDD `-19.5565`
- `market_context_high->metal_4h` score `-2.3936` n `199` status `ready` deltaP `5.4119` edge `0.0006` maxDD `-11.2249`
- `market_context_high->commodity_4h` score `-4.018` n `199` status `ready` deltaP `-10.2394` edge `-0.0119` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

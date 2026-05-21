# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T07:22:15.709309+00:00`
- Price records: `672`
- Market context records: `1401`
- Flow alert records: `5947`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8784`

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

- `market_context_high->crypto_major_24h` score `12.5107` n `156` status `ready` deltaP `27.5774` edge `0.9719` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4781` n `156` status `ready` deltaP `28.8061` edge `0.9661` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.2599` n `156` status `ready` deltaP `11.031` edge `1.0315` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.8622` n `156` status `ready` deltaP `19.4978` edge `0.3005` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.243` n `156` status `ready` deltaP `12.6603` edge `0.3352` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.2113` n `196` status `ready` deltaP `7.2361` edge `0.1357` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0542` n `156` status `ready` deltaP `9.7088` edge `0.0447` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0181` n `204` status `ready` deltaP `4.6496` edge `0.014` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0799` n `204` status `ready` deltaP `3.0439` edge `0.0289` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2477` n `204` status `ready` deltaP `4.127` edge `-0.0016` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.6529` n `196` status `ready` deltaP `0.1338` edge `0.0536` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.6811` n `204` status `ready` deltaP `5.2307` edge `-0.0047` maxDD `-5.0663`
- `market_context_high->crypto_alt_1h` score `-0.749` n `204` status `ready` deltaP `0.411` edge `0.0219` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.8848` n `204` status `ready` deltaP `-1.6878` edge `-0.001` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-1.4909` n `204` status `ready` deltaP `-1.6731` edge `-0.0024` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.5088` n `196` status `ready` deltaP `-2.9959` edge `-0.0087` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.5303` n `196` status `ready` deltaP `4.2994` edge `0.1147` maxDD `-13.3376`
- `market_context_high->crypto_alt_4h` score `-1.5942` n `196` status `ready` deltaP `6.0011` edge `0.1591` maxDD `-19.5565`
- `market_context_high->metal_4h` score `-1.8775` n `196` status `ready` deltaP `6.2811` edge `0.0093` maxDD `-9.9438`
- `market_context_high->commodity_4h` score `-4.1184` n `196` status `ready` deltaP `-10.8201` edge `-0.0164` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

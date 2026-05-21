# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T10:07:27.180674+00:00`
- Price records: `672`
- Market context records: `1413`
- Flow alert records: `5981`
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

- `market_context_high->crypto_major_24h` score `11.9212` n `155` status `ready` deltaP `27.379` edge `0.9241` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4687` n `155` status `ready` deltaP `28.7937` edge `0.9654` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.2368` n `155` status `ready` deltaP `10.3819` edge `1.0339` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.7352` n `155` status `ready` deltaP `19.4399` edge `0.2903` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.2305` n `155` status `ready` deltaP `12.5941` edge `0.3346` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.8466` n `203` status `ready` deltaP `5.0019` edge `0.1202` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0535` n `155` status `ready` deltaP `9.5351` edge `0.0458` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1143` n `203` status `ready` deltaP `3.9276` edge `0.0108` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1867` n `203` status `ready` deltaP `2.4741` edge `0.0238` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2781` n `203` status `ready` deltaP `3.7624` edge `-0.0017` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6266` n `203` status `ready` deltaP `0.9808` edge `0.0283` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.7513` n `203` status `ready` deltaP `-1.0383` edge `0.0058` maxDD `-2.252`
- `market_context_high->metal_1h` score `-0.7627` n `203` status `ready` deltaP `4.4726` edge `-0.0101` maxDD `-5.0663`
- `market_context_high->index_4h` score `-0.8883` n `203` status `ready` deltaP `-1.5785` edge `0.0454` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-1.4178` n `203` status `ready` deltaP `5.1499` edge `0.1184` maxDD `-13.3376`
- `market_context_high->crypto_alt_4h` score `-1.4695` n `203` status `ready` deltaP `6.5699` edge `0.1657` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.4862` n `203` status `ready` deltaP `-1.5693` edge `-0.0027` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.5911` n `203` status `ready` deltaP `-3.9048` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-2.5763` n `203` status `ready` deltaP `-9.9349` edge `-0.0094` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8437` n `203` status `ready` deltaP `4.1759` edge `-0.005` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

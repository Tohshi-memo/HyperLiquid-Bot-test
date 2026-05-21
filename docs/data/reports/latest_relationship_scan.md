# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T09:07:19.275360+00:00`
- Price records: `672`
- Market context records: `1409`
- Flow alert records: `5968`
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

- `market_context_high->crypto_major_24h` score `12.0396` n `156` status `ready` deltaP `27.4038` edge `0.9338` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4877` n `156` status `ready` deltaP `28.8061` edge `0.9669` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.1642` n `156` status `ready` deltaP `10.5101` edge `1.027` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.7854` n `156` status `ready` deltaP `19.4978` edge `0.2941` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.2706` n `156` status `ready` deltaP `12.6603` edge `0.3375` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.876` n `203` status `ready` deltaP `5.4592` edge `0.1196` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0662` n `156` status `ready` deltaP `9.7088` edge `0.0457` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1248` n `204` status `ready` deltaP `3.9011` edge `0.0101` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2142` n `204` status `ready` deltaP `2.2954` edge `0.0227` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2465` n `204` status `ready` deltaP `4.127` edge `-0.0015` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.7418` n `204` status `ready` deltaP `0.411` edge `0.0225` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.7421` n `204` status `ready` deltaP `-0.9393` edge `0.0059` maxDD `-2.252`
- `market_context_high->metal_1h` score `-0.77` n `204` status `ready` deltaP `4.3325` edge `-0.0101` maxDD `-5.0663`
- `market_context_high->index_4h` score `-0.8983` n `203` status `ready` deltaP `-1.6138` edge `0.0448` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-1.4761` n `203` status `ready` deltaP `4.9622` edge `0.1148` maxDD `-13.3376`
- `market_context_high->crypto_alt_4h` score `-1.5471` n `203` status `ready` deltaP `6.2297` edge `0.1615` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-1.5777` n `203` status `ready` deltaP `-3.7524` edge `-0.0094` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.5892` n `204` status `ready` deltaP `-2.2719` edge `-0.0066` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-2.8355` n `203` status `ready` deltaP `4.293` edge `-0.0051` maxDD `-11.7852`
- `market_context_high->commodity_4h` score `-3.9958` n `203` status `ready` deltaP `-10.052` edge `-0.0113` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

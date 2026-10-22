# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T17:52:32.778346+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6680`

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

- `risk_on_high->equity_1h` score `0.6101` n `37` status `ready` deltaP `15.8966` edge `0.0146` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6101` n `37` status `ready` deltaP `15.8966` edge `0.0146` maxDD `-0.7219`
- `risk_on_high->commodity_24h` score `0.4838` n `37` status `ready` deltaP `14.7751` edge `0.0433` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4838` n `37` status `ready` deltaP `14.7751` edge `0.0433` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4686` n `37` status `ready` deltaP `12.6032` edge `0.0031` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4686` n `37` status `ready` deltaP `12.6032` edge `0.0031` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.2409` n `77` status `ready` deltaP `12.4585` edge `0.0554` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.097` n `37` status `ready` deltaP `5.4014` edge `0.0023` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.097` n `37` status `ready` deltaP `5.4014` edge `0.0023` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1832` n `37` status `ready` deltaP `-0.1319` edge `0.0038` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1832` n `37` status `ready` deltaP `-0.1319` edge `0.0038` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.364` n `92` status `ready` deltaP `-0.8266` edge `-0.0013` maxDD `-0.5218`
- `risk_on_high->index_4h` score `-0.4439` n `37` status `ready` deltaP `5.0099` edge `-0.0058` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4439` n `37` status `ready` deltaP `5.0099` edge `-0.0058` maxDD `-0.7604`
- `market_context_high->index_1h` score `-0.5453` n `92` status `ready` deltaP `2.0567` edge `-0.0055` maxDD `-0.9588`
- `market_context_high->commodity_1h` score `-0.5483` n `92` status `ready` deltaP `-0.8201` edge `0.0019` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.6751` n `37` status `ready` deltaP `-4.9685` edge `0.0029` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.6751` n `37` status `ready` deltaP `-4.9685` edge `0.0029` maxDD `-0.0831`
- `market_context_high->commodity_4h` score `-0.7869` n `84` status `ready` deltaP `0.5226` edge `-0.0012` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.8203` n `92` status `ready` deltaP `-7.4655` edge `-0.0094` maxDD `-1.3465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

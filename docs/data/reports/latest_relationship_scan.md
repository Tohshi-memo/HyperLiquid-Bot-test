# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T16:52:30.745893+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6570`

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

- `risk_on_high->equity_1h` score `0.593` n `37` status `ready` deltaP `15.8966` edge `0.0124` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.593` n `37` status `ready` deltaP `15.8966` edge `0.0124` maxDD `-0.7219`
- `risk_on_high->commodity_24h` score `0.4905` n `37` status `ready` deltaP `14.905` edge `0.0433` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4905` n `37` status `ready` deltaP `14.905` edge `0.0433` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4772` n `37` status `ready` deltaP `12.7529` edge `0.0032` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4772` n `37` status `ready` deltaP `12.7529` edge `0.0032` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.1963` n `78` status `ready` deltaP `11.8558` edge `0.0537` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.104` n `37` status `ready` deltaP `5.5511` edge `0.0022` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.104` n `37` status `ready` deltaP `5.5511` edge `0.0022` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1563` n `37` status `ready` deltaP `0.3254` edge `0.0042` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1563` n `37` status `ready` deltaP `0.3254` edge `0.0042` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.4193` n `93` status `ready` deltaP `-1.1912` edge `-0.0016` maxDD `-0.5374`
- `risk_on_high->index_4h` score `-0.4524` n `37` status `ready` deltaP `5.0099` edge `-0.0069` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4524` n `37` status `ready` deltaP `5.0099` edge `-0.0069` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.4974` n `93` status `ready` deltaP `-0.0064` edge `0.003` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5766` n `93` status `ready` deltaP `1.6805` edge `-0.0056` maxDD `-0.9588`
- `market_context_high->commodity_4h` score `-0.6901` n `82` status `ready` deltaP `1.8292` edge `0.0025` maxDD `-2.9203`
- `risk_on_high->metal_1h` score `-0.7015` n `37` status `ready` deltaP `-5.2679` edge `0.0027` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7015` n `37` status `ready` deltaP `-5.2679` edge `0.0027` maxDD `-0.0831`
- `market_context_high->metal_1h` score `-0.7981` n `93` status `ready` deltaP `-7.0987` edge `-0.009` maxDD `-1.3465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

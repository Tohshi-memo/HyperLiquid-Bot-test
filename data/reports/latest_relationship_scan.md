# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T13:22:33.740525+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6614`

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

- `risk_on_high->equity_1h` score `0.6278` n `37` status `ready` deltaP `15.1481` edge `0.0218` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.6278` n `37` status `ready` deltaP `15.1481` edge `0.0218` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5286` n `37` status `ready` deltaP `13.3517` edge `0.0058` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5286` n `37` status `ready` deltaP `13.3517` edge `0.0058` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.3741` n `78` status `ready` deltaP `15.6651` edge `0.0511` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.1468` n `37` status `ready` deltaP `6.2996` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1468` n `37` status `ready` deltaP `6.2996` edge `0.0027` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.1108` n `37` status `ready` deltaP `11.022` edge `0.0205` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1108` n `37` status `ready` deltaP `11.022` edge `0.0205` maxDD `-1.7154`
- `market_context_high->fx_4h` score `-0.043` n `87` status `ready` deltaP `7.0718` edge `0.0099` maxDD `-0.5168`
- `risk_on_high->fx_4h` score `-0.0717` n `37` status `ready` deltaP `1.6974` edge `0.0059` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0717` n `37` status `ready` deltaP `1.6974` edge `0.0059` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1066` n `87` status `ready` deltaP `2.8202` edge `0.003` maxDD `-0.1712`
- `risk_on_high->index_4h` score `-0.2524` n `37` status `ready` deltaP `7.2965` edge `0.0035` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2524` n `37` status `ready` deltaP `7.2965` edge `0.0035` maxDD `-0.7604`
- `market_context_high->index_1h` score `-0.412` n `87` status `ready` deltaP `3.3175` edge `-0.0028` maxDD `-0.9588`
- `market_context_high->commodity_1h` score `-0.453` n `87` status `ready` deltaP `0.8793` edge `0.0028` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.5146` n `37` status `ready` deltaP `-3.3218` edge `0.0053` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.5146` n `37` status `ready` deltaP `-3.3218` edge `0.0053` maxDD `-0.0831`
- `market_context_high->commodity_4h` score `-0.6` n `87` status `ready` deltaP `2.453` edge `0.0099` maxDD `-2.9203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

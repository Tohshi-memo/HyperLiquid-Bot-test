# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T12:52:30.420694+00:00`
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

- `risk_on_high->equity_1h` score `0.6294` n `37` status `ready` deltaP `15.1481` edge `0.022` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.6294` n `37` status `ready` deltaP `15.1481` edge `0.022` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5286` n `37` status `ready` deltaP `13.3517` edge `0.0058` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5286` n `37` status `ready` deltaP `13.3517` edge `0.0058` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.3149` n `76` status `ready` deltaP `14.7204` edge `0.0498` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.1468` n `37` status `ready` deltaP `6.2996` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1468` n `37` status `ready` deltaP `6.2996` edge `0.0027` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.1007` n `37` status `ready` deltaP `11.022` edge `0.0192` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1007` n `37` status `ready` deltaP `11.022` edge `0.0192` maxDD `-1.7154`
- `market_context_high->fx_4h` score `-0.0698` n `87` status `ready` deltaP `6.7669` edge `0.0097` maxDD `-0.5168`
- `risk_on_high->fx_4h` score `-0.0891` n `37` status `ready` deltaP `1.3925` edge `0.0057` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0891` n `37` status `ready` deltaP `1.3925` edge `0.0057` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1066` n `87` status `ready` deltaP `2.8202` edge `0.003` maxDD `-0.1712`
- `risk_on_high->index_4h` score `-0.254` n `37` status `ready` deltaP `7.2965` edge `0.0033` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.254` n `37` status `ready` deltaP `7.2965` edge `0.0033` maxDD `-0.7604`
- `market_context_high->index_1h` score `-0.412` n `87` status `ready` deltaP `3.3175` edge `-0.0028` maxDD `-0.9588`
- `market_context_high->commodity_1h` score `-0.4561` n `87` status `ready` deltaP `0.8793` edge `0.0024` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.5002` n `37` status `ready` deltaP `-3.1721` edge `0.0055` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.5002` n `37` status `ready` deltaP `-3.1721` edge `0.0055` maxDD `-0.0831`
- `market_context_high->commodity_4h` score `-0.6015` n `87` status `ready` deltaP `2.453` edge `0.0097` maxDD `-2.9203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

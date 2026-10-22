# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T15:37:32.166241+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6396`

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

- `risk_on_high->equity_1h` score `0.5633` n `37` status `ready` deltaP `15.7469` edge `0.0096` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5633` n `37` status `ready` deltaP `15.7469` edge `0.0096` maxDD `-0.7219`
- `risk_on_high->commodity_24h` score `0.5118` n `37` status `ready` deltaP `15.2696` edge `0.0436` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5118` n `37` status `ready` deltaP `15.2696` edge `0.0436` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4951` n `37` status `ready` deltaP `13.0523` edge `0.0035` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4951` n `37` status `ready` deltaP `13.0523` edge `0.0035` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.2176` n `78` status `ready` deltaP `12.2204` edge `0.054` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.1118` n `37` status `ready` deltaP `5.7008` edge `0.0022` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1118` n `37` status `ready` deltaP `5.7008` edge `0.0022` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1381` n `37` status `ready` deltaP `0.6303` edge `0.0045` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1381` n `37` status `ready` deltaP `0.6303` edge `0.0045` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.3905` n `88` status `ready` deltaP `1.3201` edge `-0.0055` maxDD `-0.9361`
- `risk_on_high->index_4h` score `-0.4666` n `37` status `ready` deltaP `4.8575` edge `-0.0077` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4666` n `37` status `ready` deltaP `4.8575` edge `-0.0077` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.4949` n `88` status `ready` deltaP `0.0272` edge `0.0029` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.5024` n `78` status `ready` deltaP `4.6435` edge `0.0078` maxDD `-2.9203`
- `market_context_high->fx_1h` score `-0.5805` n `88` status `ready` deltaP `-4.0351` edge `-0.0033` maxDD `-0.5374`
- `market_context_high->metal_1h` score `-0.6172` n `88` status `ready` deltaP `-5.1987` edge `-0.0047` maxDD `-0.8482`
- `risk_on_high->metal_1h` score `-0.7326` n `37` status `ready` deltaP `-5.5673` edge `0.0021` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7326` n `37` status `ready` deltaP `-5.5673` edge `0.0021` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

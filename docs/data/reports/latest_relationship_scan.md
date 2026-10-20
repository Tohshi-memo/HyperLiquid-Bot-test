# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T23:07:30.216813+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8914`

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

- `risk_on_high->equity_1h` score `0.6803` n `37` status `ready` deltaP `16.196` edge `0.0216` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6803` n `37` status `ready` deltaP `16.196` edge `0.0216` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5441` n `37` status `ready` deltaP `13.6511` edge `0.0058` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5441` n `37` status `ready` deltaP `13.6511` edge `0.0058` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2589` n `37` status `ready` deltaP `15.5359` edge `0.0094` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2589` n `37` status `ready` deltaP `15.5359` edge `0.0094` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.0386` n `37` status `ready` deltaP `4.5032` edge `0.0008` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0386` n `37` status `ready` deltaP `4.5032` edge `0.0008` maxDD `-0.0698`
- `market_context_high->index_1h` score `0.0185` n `78` status `ready` deltaP `5.4737` edge `0.0014` maxDD `-0.5082`
- `market_context_high->commodity_24h` score `-0.0353` n `78` status `ready` deltaP `12.4867` edge `0.0198` maxDD `-3.6055`
- `risk_on_high->index_4h` score `-0.0482` n `37` status `ready` deltaP `9.888` edge `0.0124` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0482` n `37` status `ready` deltaP `9.888` edge `0.0124` maxDD `-0.7604`
- `risk_on_high->fx_4h` score `-0.1961` n `37` status `ready` deltaP `0.3254` edge `-0.0009` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1961` n `37` status `ready` deltaP `0.3254` edge `-0.0009` maxDD `-0.1126`
- `risk_on_high->equity_4h` score `-0.2344` n `37` status `ready` deltaP `7.3788` edge `0.0462` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.2344` n `37` status `ready` deltaP `7.3788` edge `0.0462` maxDD `-4.0351`
- `market_context_high->commodity_1h` score `-0.2375` n `78` status `ready` deltaP `3.9114` edge `0.01` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.2396` n `78` status `ready` deltaP `8.3021` edge `0.0171` maxDD `-2.9203`
- `risk_on_high->commodity_1h` score `-0.6674` n `37` status `ready` deltaP `-0.0041` edge `-0.019` maxDD `-0.9891`
- `risk_on_and_context->commodity_1h` score `-0.6674` n `37` status `ready` deltaP `-0.0041` edge `-0.019` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

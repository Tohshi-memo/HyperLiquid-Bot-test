# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-21T00:07:26.979128+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8806`

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

- `risk_on_high->equity_1h` score `0.72` n `37` status `ready` deltaP `16.6451` edge `0.0237` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.72` n `37` status `ready` deltaP `16.6451` edge `0.0237` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5706` n `37` status `ready` deltaP `14.1002` edge `0.0062` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5706` n `37` status `ready` deltaP `14.1002` edge `0.0062` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2233` n `37` status `ready` deltaP `15.0151` edge `0.0083` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2233` n `37` status `ready` deltaP `15.0151` edge `0.0083` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.0635` n `37` status `ready` deltaP `4.9523` edge `0.001` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0635` n `37` status `ready` deltaP `4.9523` edge `0.001` maxDD `-0.0698`
- `market_context_high->index_1h` score `0.045` n `78` status `ready` deltaP `5.9228` edge `0.0018` maxDD `-0.5082`
- `risk_on_high->index_4h` score `-0.0521` n `37` status `ready` deltaP `9.888` edge `0.0119` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0521` n `37` status `ready` deltaP `9.888` edge `0.0119` maxDD `-0.7604`
- `market_context_high->commodity_24h` score `-0.0709` n `78` status `ready` deltaP `11.9659` edge `0.0187` maxDD `-3.6055`
- `risk_on_high->fx_4h` score `-0.1874` n `37` status `ready` deltaP `0.4779` edge `-0.0008` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1874` n `37` status `ready` deltaP `0.4779` edge `-0.0008` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.2329` n `78` status `ready` deltaP `3.9114` edge `0.0106` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.2468` n `78` status `ready` deltaP `8.1496` edge `0.0172` maxDD `-2.9203`
- `risk_on_high->equity_4h` score `-0.2874` n `37` status `ready` deltaP `7.3788` edge `0.0394` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.2874` n `37` status `ready` deltaP `7.3788` edge `0.0394` maxDD `-4.0351`
- `market_context_high->metal_1h` score `-0.6526` n `78` status `ready` deltaP `-6.2798` edge `-0.0043` maxDD `-0.6669`
- `risk_on_high->commodity_1h` score `-0.6627` n `37` status `ready` deltaP `-0.0041` edge `-0.0184` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

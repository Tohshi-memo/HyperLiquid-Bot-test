# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T05:52:28.290943+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7288`

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

- `risk_on_high->equity_1h` score `0.5058` n `37` status `ready` deltaP `14.3996` edge `0.0112` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5058` n `37` status `ready` deltaP `14.3996` edge `0.0112` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.4702` n `37` status `ready` deltaP `12.4535` edge `0.0043` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4702` n `37` status `ready` deltaP `12.4535` edge `0.0043` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.2186` n `72` status `ready` deltaP `13.8889` edge `0.043` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.2153` n `37` status `ready` deltaP `12.2373` edge `0.0258` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2153` n `37` status `ready` deltaP `12.2373` edge `0.0258` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1118` n `37` status `ready` deltaP `5.7008` edge `0.0022` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1118` n `37` status `ready` deltaP `5.7008` edge `0.0022` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.1417` n `87` status `ready` deltaP `2.2214` edge `0.0025` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.1673` n `37` status `ready` deltaP `0.173` edge `0.0038` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1673` n `37` status `ready` deltaP `0.173` edge `0.0038` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.1901` n `87` status `ready` deltaP `5.5474` edge `0.0078` maxDD `-0.5168`
- `risk_on_high->index_4h` score `-0.2997` n `37` status `ready` deltaP `6.6868` edge `0.0015` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2997` n `37` status `ready` deltaP `6.6868` edge `0.0015` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.3677` n `87` status `ready` deltaP `5.9591` edge `0.0163` maxDD `-2.9203`
- `market_context_high->commodity_1h` score `-0.4241` n `87` status `ready` deltaP `1.3284` edge `0.0035` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5019` n `87` status `ready` deltaP `2.4193` edge `-0.0043` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.547` n `37` status `ready` deltaP `-3.6212` edge `0.0046` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.547` n `37` status `ready` deltaP `-3.6212` edge `0.0046` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

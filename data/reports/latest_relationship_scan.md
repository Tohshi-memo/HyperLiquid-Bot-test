# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T03:07:29.912848+00:00`
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

- `risk_on_high->equity_1h` score `0.5748` n `37` status `ready` deltaP `14.699` edge `0.018` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.5748` n `37` status `ready` deltaP `14.699` edge `0.018` maxDD `-0.7172`
- `market_context_high->commodity_24h` score `0.5158` n `82` status `ready` deltaP `16.5438` edge `0.0634` maxDD `-3.6055`
- `risk_on_high->index_1h` score `0.5075` n `37` status `ready` deltaP `13.0523` edge `0.0051` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5075` n `37` status `ready` deltaP `13.0523` edge `0.0051` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1912` n `37` status `ready` deltaP `11.3692` edge `0.0285` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1912` n `37` status `ready` deltaP `11.3692` edge `0.0285` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1702` n `37` status `ready` deltaP `6.7487` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1702` n `37` status `ready` deltaP `6.7487` edge `0.0027` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.0487` n `37` status `ready` deltaP `2.1547` edge `0.0058` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0487` n `37` status `ready` deltaP `2.1547` edge `0.0058` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.0706` n `82` status `ready` deltaP `3.9141` edge `0.0035` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.0967` n `82` status `ready` deltaP `5.9451` edge `0.0086` maxDD `-0.5168`
- `market_context_high->index_1h` score `-0.2558` n `82` status `ready` deltaP `3.5928` edge `-0.0031` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.3194` n `37` status `ready` deltaP `6.5343` edge `0.0` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3194` n `37` status `ready` deltaP `6.5343` edge `0.0` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.4583` n `37` status `ready` deltaP `-2.8727` edge `0.007` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4583` n `37` status `ready` deltaP `-2.8727` edge `0.007` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.5607` n `82` status `ready` deltaP `-0.3834` edge `-0.0026` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.8642` n `82` status `ready` deltaP `-1.3719` edge `-0.0029` maxDD `-2.8998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

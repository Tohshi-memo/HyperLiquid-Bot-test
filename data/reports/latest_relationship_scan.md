# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T03:37:29.839500+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7006`

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

- `risk_on_high->equity_1h` score `0.5522` n `37` status `ready` deltaP `14.3996` edge `0.0171` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.5522` n `37` status `ready` deltaP `14.3996` edge `0.0171` maxDD `-0.7172`
- `market_context_high->commodity_24h` score `0.522` n `82` status `ready` deltaP `16.5438` edge `0.0642` maxDD `-3.6055`
- `risk_on_high->index_1h` score `0.4904` n `37` status `ready` deltaP `12.7529` edge `0.0049` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4904` n `37` status `ready` deltaP `12.7529` edge `0.0049` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1975` n `37` status `ready` deltaP `11.3692` edge `0.0293` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1975` n `37` status `ready` deltaP `11.3692` edge `0.0293` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1694` n `37` status `ready` deltaP `6.7487` edge `0.0026` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1694` n `37` status `ready` deltaP `6.7487` edge `0.0026` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.0487` n `37` status `ready` deltaP `2.1547` edge `0.0058` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0487` n `37` status `ready` deltaP `2.1547` edge `0.0058` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.0718` n `82` status `ready` deltaP `3.9141` edge `0.0034` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.0967` n `82` status `ready` deltaP `5.9451` edge `0.0086` maxDD `-0.5168`
- `market_context_high->index_1h` score `-0.273` n `82` status `ready` deltaP `3.2934` edge `-0.0033` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.3438` n `37` status `ready` deltaP `6.2294` edge `-0.0011` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3438` n `37` status `ready` deltaP `6.2294` edge `-0.0011` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.4619` n `37` status `ready` deltaP `-2.8727` edge `0.0067` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4619` n `37` status `ready` deltaP `-2.8727` edge `0.0067` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.5607` n `82` status `ready` deltaP `-0.3834` edge `-0.0026` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.8508` n `82` status `ready` deltaP `-1.2195` edge `-0.0022` maxDD `-2.8998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

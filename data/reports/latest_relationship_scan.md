# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T09:52:27.066710+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6468`

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

- `risk_on_high->equity_1h` score `0.514` n `37` status `ready` deltaP `14.1002` edge `0.0142` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.514` n `37` status `ready` deltaP `14.1002` edge `0.0142` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.4998` n `37` status `ready` deltaP `12.9026` edge `0.0051` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4998` n `37` status `ready` deltaP `12.9026` edge `0.0051` maxDD `-0.1637`
- `risk_on_high->fx_1h` score `0.1546` n `37` status `ready` deltaP `6.4493` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1546` n `37` status `ready` deltaP `6.4493` edge `0.0027` maxDD `-0.0698`
- `market_context_high->commodity_24h` score `0.0953` n `72` status `ready` deltaP `12.6736` edge `0.0353` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.0921` n `37` status `ready` deltaP `11.022` edge `0.0181` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.0921` n `37` status `ready` deltaP `11.022` edge `0.0181` maxDD `-1.7154`
- `market_context_high->fx_1h` score `-0.0989` n `87` status `ready` deltaP `2.9699` edge `0.003` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.1397` n `37` status `ready` deltaP `0.6303` edge `0.0043` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1397` n `37` status `ready` deltaP `0.6303` edge `0.0043` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.1475` n `87` status `ready` deltaP `6.0047` edge `0.0083` maxDD `-0.5168`
- `risk_on_high->index_4h` score `-0.2761` n `37` status `ready` deltaP `6.9916` edge `0.0025` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2761` n `37` status `ready` deltaP `6.9916` edge `0.0025` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.4467` n `87` status `ready` deltaP `1.029` edge `0.0026` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.4563` n `87` status `ready` deltaP `2.8684` edge `-0.0035` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.4943` n `37` status `ready` deltaP `-3.0224` edge `0.005` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4943` n `37` status `ready` deltaP `-3.0224` edge `0.005` maxDD `-0.0831`
- `market_context_high->commodity_4h` score `-0.5114` n `87` status `ready` deltaP `3.825` edge `0.0121` maxDD `-2.9203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

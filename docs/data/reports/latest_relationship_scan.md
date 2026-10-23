# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T22:07:28.192270+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6410`

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

- `risk_on_high->equity_1h` score `0.648` n `37` status `ready` deltaP `15.5972` edge `0.0214` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.648` n `37` status `ready` deltaP `15.5972` edge `0.0214` maxDD `-0.7172`
- `market_context_high->commodity_24h` score `0.527` n `82` status `ready` deltaP `16.3702` edge `0.066` maxDD `-3.6055`
- `risk_on_high->index_1h` score `0.5231` n `37` status `ready` deltaP `13.3517` edge `0.0051` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5231` n `37` status `ready` deltaP `13.3517` edge `0.0051` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2025` n `37` status `ready` deltaP `11.1956` edge `0.0311` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2025` n `37` status `ready` deltaP `11.1956` edge `0.0311` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1134` n `37` status `ready` deltaP `5.7008` edge `0.0024` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1134` n `37` status `ready` deltaP `5.7008` edge `0.0024` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1104` n `37` status `ready` deltaP `1.0876` edge `0.005` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1104` n `37` status `ready` deltaP `1.0876` edge `0.005` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.158` n `82` status `ready` deltaP `2.8662` edge `0.0032` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.1584` n `82` status `ready` deltaP `4.878` edge `0.0078` maxDD `-0.5168`
- `market_context_high->index_1h` score `-0.2403` n `82` status `ready` deltaP `3.8922` edge `-0.0031` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.265` n `37` status `ready` deltaP `7.1441` edge `0.0029` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.265` n `37` status `ready` deltaP `7.1441` edge `0.0029` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.4331` n `37` status `ready` deltaP `-2.5733` edge `0.0071` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4331` n `37` status `ready` deltaP `-2.5733` edge `0.0071` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.5685` n `82` status `ready` deltaP `-0.5331` edge `-0.0026` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.7445` n `82` status `ready` deltaP `0.0` edge `0.0033` maxDD `-2.8998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T20:52:27.096180+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6270`

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

- `market_context_high->commodity_24h` score `1.2196` n `86` status `ready` deltaP `18.0152` edge `0.0891` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.6504` n `37` status `ready` deltaP `15.5972` edge `0.0217` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.6504` n `37` status `ready` deltaP `15.5972` edge `0.0217` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5317` n `37` status `ready` deltaP `13.5014` edge `0.0052` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5317` n `37` status `ready` deltaP `13.5014` edge `0.0052` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1986` n `37` status `ready` deltaP `11.1956` edge `0.0306` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1986` n `37` status `ready` deltaP `11.1956` edge `0.0306` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1383` n `37` status `ready` deltaP `6.1499` edge `0.0026` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1383` n `37` status `ready` deltaP `6.1499` edge `0.0026` maxDD `-0.0698`
- `market_context_high->fx_4h` score `-0.0743` n `86` status `ready` deltaP `6.7853` edge `0.0092` maxDD `-0.5168`
- `market_context_high->fx_1h` score `-0.123` n `86` status `ready` deltaP `3.2586` edge `0.0035` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.1278` n `37` status `ready` deltaP `0.7827` edge `0.0048` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1278` n `37` status `ready` deltaP `0.7827` edge `0.0048` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.2255` n `86` status `ready` deltaP `4.0419` edge `-0.0022` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.2548` n `37` status `ready` deltaP `7.2965` edge `0.0032` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2548` n `37` status `ready` deltaP `7.2965` edge `0.0032` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.4379` n `37` status `ready` deltaP `-2.5733` edge `0.0067` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4379` n `37` status `ready` deltaP `-2.5733` edge `0.0067` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.4873` n `86` status `ready` deltaP `0.4596` edge `0.0012` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6311` n `86` status `ready` deltaP `-4.7417` edge `-0.0033` maxDD `-1.3465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

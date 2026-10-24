# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T16:22:31.951148+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7380`

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

- `market_context_high->unknown_4h` score `16.3831` n `103` status `ready` deltaP `-2.7616` edge `1.4172` maxDD `-1.016`
- `risk_on_high->index_1h` score `0.4678` n `37` status `ready` deltaP `12.7529` edge `0.002` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4678` n `37` status `ready` deltaP `12.7529` edge `0.002` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4524` n `37` status `ready` deltaP `14.699` edge `0.0023` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4524` n `37` status `ready` deltaP `14.699` edge `0.0023` maxDD `-0.7172`
- `market_context_high->commodity_24h` score `0.3762` n `82` status `ready` deltaP `14.4605` edge `0.0594` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.2107` n `37` status `ready` deltaP `7.4972` edge `0.0029` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.2107` n `37` status `ready` deltaP `7.4972` edge `0.0029` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.0517` n `37` status `ready` deltaP `9.2859` edge `0.0245` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.0517` n `37` status `ready` deltaP `9.2859` edge `0.0245` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `0.0091` n `37` status `ready` deltaP `3.2218` edge `0.0061` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0091` n `37` status `ready` deltaP `3.2218` edge `0.0061` maxDD `-0.1126`
- `market_context_high->commodity_4h` score `-0.1274` n `103` status `ready` deltaP `7.9964` edge `0.0291` maxDD `-2.8998`
- `market_context_high->fx_1h` score `-0.2192` n `110` status `ready` deltaP `0.7158` edge `0.0026` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.2943` n `110` status `ready` deltaP `3.6908` edge `0.0044` maxDD `-1.0053`
- `market_context_high->fx_4h` score `-0.3619` n `103` status `ready` deltaP `1.1751` edge `0.0064` maxDD `-0.5168`
- `risk_on_high->metal_1h` score `-0.4379` n `37` status `ready` deltaP `-2.5733` edge `0.0067` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4379` n `37` status `ready` deltaP `-2.5733` edge `0.0067` maxDD `-0.0831`
- `risk_on_high->index_4h` score `-0.4488` n `37` status `ready` deltaP `5.6197` edge `-0.0105` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4488` n `37` status `ready` deltaP `5.6197` edge `-0.0105` maxDD `-0.7604`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T18:22:29.599309+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7580`

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

- `market_context_high->unknown_4h` score `12.5711` n `109` status `ready` deltaP `-1.5859` edge `1.0917` maxDD `-1.016`
- `risk_on_high->index_1h` score `0.4826` n `37` status `ready` deltaP `13.0523` edge `0.0019` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4826` n `37` status `ready` deltaP `13.0523` edge `0.0019` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4508` n `37` status `ready` deltaP `14.8487` edge `0.0011` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4508` n `37` status `ready` deltaP `14.8487` edge `0.0011` maxDD `-0.7172`
- `market_context_high->commodity_24h` score `0.3523` n `81` status `ready` deltaP `13.8696` edge `0.0561` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.2262` n `37` status `ready` deltaP `7.7966` edge `0.0029` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.2262` n `37` status `ready` deltaP `7.7966` edge `0.0029` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `0.0432` n `37` status `ready` deltaP `3.8315` edge `0.0064` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0432` n `37` status `ready` deltaP `3.8315` edge `0.0064` maxDD `-0.1126`
- `risk_on_high->commodity_24h` score `-0.0579` n `37` status `ready` deltaP `7.897` edge `0.0197` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.0579` n `37` status `ready` deltaP `7.897` edge `0.0197` maxDD `-1.7154`
- `market_context_high->commodity_4h` score `-0.0909` n `109` status `ready` deltaP `7.6737` edge `0.0289` maxDD `-2.6698`
- `market_context_high->fx_1h` score `-0.245` n `114` status `ready` deltaP `0.2337` edge `0.0025` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.2866` n `114` status `ready` deltaP `3.7031` edge `0.0053` maxDD `-1.0053`
- `risk_on_high->index_4h` score `-0.3847` n `37` status `ready` deltaP `6.6868` edge `-0.0094` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3847` n `37` status `ready` deltaP `6.6868` edge `-0.0094` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.4379` n `37` status `ready` deltaP `-2.5733` edge `0.0067` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4379` n `37` status `ready` deltaP `-2.5733` edge `0.0067` maxDD `-0.0831`
- `market_context_high->fx_4h` score `-0.4729` n `109` status `ready` deltaP `-0.7804` edge `0.0052` maxDD `-0.5168`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

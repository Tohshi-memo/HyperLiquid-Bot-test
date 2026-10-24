# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T01:22:28.630280+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6504`

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

- `risk_on_high->equity_1h` score `0.6434` n `37` status `ready` deltaP `15.5972` edge `0.0208` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.6434` n `37` status `ready` deltaP `15.5972` edge `0.0208` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5239` n `37` status `ready` deltaP `13.3517` edge `0.0052` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5239` n `37` status `ready` deltaP `13.3517` edge `0.0052` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.5028` n `82` status `ready` deltaP `16.3702` edge `0.0629` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.1783` n `37` status `ready` deltaP `11.1956` edge `0.028` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1783` n `37` status `ready` deltaP `11.1956` edge `0.028` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1624` n `37` status `ready` deltaP `6.599` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1624` n `37` status `ready` deltaP `6.599` edge `0.0027` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.0825` n `82` status `ready` deltaP `3.7644` edge `0.0035` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.0994` n `37` status `ready` deltaP `1.2401` edge `0.0054` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0994` n `37` status `ready` deltaP `1.2401` edge `0.0054` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.1473` n `82` status `ready` deltaP `5.0305` edge `0.0082` maxDD `-0.5168`
- `market_context_high->index_1h` score `-0.2395` n `82` status `ready` deltaP `3.8922` edge `-0.003` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.2792` n `37` status `ready` deltaP `6.9916` edge `0.0021` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2792` n `37` status `ready` deltaP `6.9916` edge `0.0021` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.3948` n `37` status `ready` deltaP `-2.1242` edge `0.0073` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.3948` n `37` status `ready` deltaP `-2.1242` edge `0.0073` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.588` n `82` status `ready` deltaP `-0.8325` edge `-0.0031` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.8352` n `82` status `ready` deltaP `-1.2195` edge `-0.0002` maxDD `-2.8998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

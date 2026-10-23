# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T23:37:30.564015+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6486`

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

- `risk_on_high->equity_1h` score `0.6847` n `37` status `ready` deltaP `16.0463` edge `0.0231` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.6847` n `37` status `ready` deltaP `16.0463` edge `0.0231` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.541` n `37` status `ready` deltaP `13.6511` edge `0.0054` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.541` n `37` status `ready` deltaP `13.6511` edge `0.0054` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.5099` n `82` status `ready` deltaP `16.3702` edge `0.0638` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.1853` n `37` status `ready` deltaP `11.1956` edge `0.0289` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1853` n `37` status `ready` deltaP `11.1956` edge `0.0289` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1297` n `37` status `ready` deltaP `6.0002` edge `0.0025` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1297` n `37` status `ready` deltaP `6.0002` edge `0.0025` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1089` n `37` status `ready` deltaP `1.0876` edge `0.0052` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1089` n `37` status `ready` deltaP `1.0876` edge `0.0052` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1328` n `82` status `ready` deltaP `3.1656` edge `0.0033` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.1568` n `82` status `ready` deltaP `4.878` edge `0.008` maxDD `-0.5168`
- `market_context_high->index_1h` score `-0.2224` n `82` status `ready` deltaP `4.1916` edge `-0.0028` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.265` n `37` status `ready` deltaP `7.1441` edge `0.0029` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.265` n `37` status `ready` deltaP `7.1441` edge `0.0029` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.3912` n `37` status `ready` deltaP `-2.1242` edge `0.0076` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.3912` n `37` status `ready` deltaP `-2.1242` edge `0.0076` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.6168` n `82` status `ready` deltaP `-1.2816` edge `-0.0038` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.761` n `82` status `ready` deltaP `-0.1524` edge `0.0022` maxDD `-2.8998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

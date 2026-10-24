# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T09:07:34.255488+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7778`

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

- `market_context_high->commodity_24h` score `0.5879` n `82` status `ready` deltaP `16.3702` edge `0.0738` maxDD `-3.6055`
- `risk_on_high->index_1h` score `0.4273` n `37` status `ready` deltaP `12.0044` edge `0.0018` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4273` n `37` status `ready` deltaP `12.0044` edge `0.0018` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4103` n `37` status `ready` deltaP `14.1002` edge `0.0009` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4103` n `37` status `ready` deltaP `14.1002` edge `0.0009` maxDD `-0.7172`
- `risk_on_high->commodity_24h` score `0.2633` n `37` status `ready` deltaP `11.1956` edge `0.0389` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2633` n `37` status `ready` deltaP `11.1956` edge `0.0389` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1624` n `37` status `ready` deltaP `6.599` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1624` n `37` status `ready` deltaP `6.599` edge `0.0027` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.0495` n `37` status `ready` deltaP `2.1547` edge `0.0057` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0495` n `37` status `ready` deltaP `2.1547` edge `0.0057` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.0974` n `82` status `ready` deltaP `5.9451` edge `0.0085` maxDD `-0.5168`
- `market_context_high->fx_1h` score `-0.2091` n `87` status `ready` deltaP `0.8208` edge `0.0032` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.4485` n `87` status `ready` deltaP `1.2802` edge `0.0007` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.4871` n `37` status `ready` deltaP `-3.0224` edge `0.0056` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4871` n `37` status `ready` deltaP `-3.0224` edge `0.0056` maxDD `-0.0831`
- `market_context_high->index_1h` score `-0.4905` n `87` status `ready` deltaP `-0.3287` edge `-0.0065` maxDD `-1.0018`
- `risk_on_high->index_4h` score `-0.52` n `37` status `ready` deltaP `4.4002` edge `-0.0115` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.52` n `37` status `ready` deltaP `4.4002` edge `-0.0115` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.5946` n `82` status `ready` deltaP `1.0671` edge `0.0154` maxDD `-2.8998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

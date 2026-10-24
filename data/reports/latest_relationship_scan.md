# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T15:37:26.284503+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7370`

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

- `market_context_high->unknown_4h` score `18.5182` n `100` status `ready` deltaP `-3.4024` edge `1.5994` maxDD `-1.016`
- `risk_on_high->index_1h` score `0.4592` n `37` status `ready` deltaP `12.6032` edge `0.0019` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4592` n `37` status `ready` deltaP `12.6032` edge `0.0019` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4267` n `37` status `ready` deltaP `14.3996` edge `0.001` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4267` n `37` status `ready` deltaP `14.3996` edge `0.001` maxDD `-0.7172`
- `market_context_high->commodity_24h` score `0.4181` n `82` status `ready` deltaP `14.9813` edge `0.0613` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.2021` n `37` status `ready` deltaP `7.3475` edge `0.0028` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.2021` n `37` status `ready` deltaP `7.3475` edge `0.0028` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.0936` n `37` status `ready` deltaP `9.8067` edge `0.0264` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.0936` n `37` status `ready` deltaP `9.8067` edge `0.0264` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `0.0004` n `37` status `ready` deltaP `3.0693` edge `0.006` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0004` n `37` status `ready` deltaP `3.0693` edge `0.006` maxDD `-0.1126`
- `market_context_high->commodity_4h` score `-0.1317` n `100` status `ready` deltaP `7.8537` edge `0.0295` maxDD `-2.8998`
- `market_context_high->fx_1h` score `-0.2278` n `110` status `ready` deltaP `0.5661` edge `0.0025` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.2924` n `100` status `ready` deltaP `2.4207` edge `0.007` maxDD `-0.5168`
- `market_context_high->commodity_1h` score `-0.3028` n `110` status `ready` deltaP `3.5411` edge `0.0043` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.4403` n `37` status `ready` deltaP `-2.5733` edge `0.0065` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4403` n `37` status `ready` deltaP `-2.5733` edge `0.0065` maxDD `-0.0831`
- `risk_on_high->index_4h` score `-0.4765` n `37` status `ready` deltaP `5.1624` edge `-0.011` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4765` n `37` status `ready` deltaP `5.1624` edge `-0.011` maxDD `-0.7604`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T15:07:26.836743+00:00`
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

- `market_context_high->unknown_4h` score `18.8831` n `98` status `ready` deltaP `-3.8514` edge `1.6328` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.4494` n `82` status `ready` deltaP `15.3285` edge `0.063` maxDD `-3.6055`
- `risk_on_high->index_1h` score `0.4429` n `37` status `ready` deltaP `12.3038` edge `0.0018` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4429` n `37` status `ready` deltaP `12.3038` edge `0.0018` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4017` n `37` status `ready` deltaP `14.1002` edge `-0.0002` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4017` n `37` status `ready` deltaP `14.1002` edge `-0.0002` maxDD `-0.7172`
- `risk_on_high->fx_1h` score `0.2099` n `37` status `ready` deltaP `7.4972` edge `0.0028` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.2099` n `37` status `ready` deltaP `7.4972` edge `0.0028` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.1249` n `37` status `ready` deltaP `10.1539` edge `0.0281` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1249` n `37` status `ready` deltaP `10.1539` edge `0.0281` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `0.0084` n `37` status `ready` deltaP `3.2218` edge `0.006` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0084` n `37` status `ready` deltaP `3.2218` edge `0.006` maxDD `-0.1126`
- `market_context_high->commodity_4h` score `-0.1643` n `98` status `ready` deltaP `7.3326` edge `0.0288` maxDD `-2.8998`
- `market_context_high->fx_1h` score `-0.22` n `110` status `ready` deltaP `0.7158` edge `0.0025` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.2843` n `98` status `ready` deltaP `2.5324` edge `0.0073` maxDD `-0.5168`
- `market_context_high->commodity_1h` score `-0.3028` n `110` status `ready` deltaP `3.5411` edge `0.0043` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.4415` n `37` status `ready` deltaP `-2.5733` edge `0.0064` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4415` n `37` status `ready` deltaP `-2.5733` edge `0.0064` maxDD `-0.0831`
- `risk_on_high->index_4h` score `-0.4939` n `37` status `ready` deltaP `4.8575` edge `-0.0112` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4939` n `37` status `ready` deltaP `4.8575` edge `-0.0112` maxDD `-0.7604`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T12:37:28.635758+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7738`

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

- `market_context_high->unknown_4h` score `25.6831` n `89` status `ready` deltaP `-6.1215` edge `2.2146` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.5233` n `82` status `ready` deltaP `15.8494` edge `0.069` maxDD `-3.6055`
- `risk_on_high->index_1h` score `0.425` n `37` status `ready` deltaP `12.0044` edge `0.0015` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.425` n `37` status `ready` deltaP `12.0044` edge `0.0015` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.3651` n `37` status `ready` deltaP `13.6511` edge `-0.0019` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.3651` n `37` status `ready` deltaP `13.6511` edge `-0.0019` maxDD `-0.7172`
- `risk_on_high->commodity_24h` score `0.1988` n `37` status `ready` deltaP `10.6748` edge `0.0341` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1988` n `37` status `ready` deltaP `10.6748` edge `0.0341` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1702` n `37` status `ready` deltaP `6.7487` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1702` n `37` status `ready` deltaP `6.7487` edge `0.0027` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.0495` n `37` status `ready` deltaP `2.1547` edge `0.0057` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0495` n `37` status `ready` deltaP `2.1547` edge `0.0057` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.079` n `89` status `ready` deltaP `6.3151` edge `0.0084` maxDD `-0.5168`
- `market_context_high->fx_1h` score `-0.114` n `100` status `ready` deltaP `2.6946` edge `0.0029` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.3224` n `100` status `ready` deltaP `3.2096` edge `0.004` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.4077` n `89` status `ready` deltaP `3.9274` edge `0.0203` maxDD `-2.8998`
- `risk_on_high->metal_1h` score `-0.4212` n `37` status `ready` deltaP `-2.2739` edge `0.0061` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4212` n `37` status `ready` deltaP `-2.2739` edge `0.0061` maxDD `-0.0831`
- `risk_on_high->index_4h` score `-0.5137` n `37` status `ready` deltaP `4.5526` edge `-0.0117` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.5137` n `37` status `ready` deltaP `4.5526` edge `-0.0117` maxDD `-0.7604`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

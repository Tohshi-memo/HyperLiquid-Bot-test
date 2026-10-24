# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T05:07:24.777317+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7140`

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

- `market_context_high->commodity_24h` score `0.5446` n `82` status `ready` deltaP `16.5438` edge `0.0671` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.4992` n `37` status `ready` deltaP `14.2499` edge `0.0113` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4992` n `37` status `ready` deltaP `14.2499` edge `0.0113` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.4686` n `37` status `ready` deltaP `12.4535` edge `0.0041` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4686` n `37` status `ready` deltaP `12.4535` edge `0.0041` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2201` n `37` status `ready` deltaP `11.3692` edge `0.0322` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2201` n `37` status `ready` deltaP `11.3692` edge `0.0322` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1951` n `37` status `ready` deltaP `7.1978` edge `0.0029` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1951` n `37` status `ready` deltaP `7.1978` edge `0.0029` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.0321` n `37` status `ready` deltaP `2.4596` edge `0.0059` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0321` n `37` status `ready` deltaP `2.4596` edge `0.0059` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.0322` n `82` status `ready` deltaP `4.3632` edge `0.0037` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.08` n `82` status `ready` deltaP `6.25` edge `0.0087` maxDD `-0.5168`
- `market_context_high->index_1h` score `-0.2948` n `82` status `ready` deltaP `2.994` edge `-0.0041` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.4131` n `37` status `ready` deltaP `5.4673` edge `-0.0049` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4131` n `37` status `ready` deltaP `5.4673` edge `-0.0049` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.4439` n `37` status `ready` deltaP `-2.723` edge `0.0072` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4439` n `37` status `ready` deltaP `-2.723` edge `0.0072` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.5872` n `82` status `ready` deltaP `-0.6828` edge `-0.004` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.751` n `82` status `ready` deltaP `-0.3049` edge `0.0045` maxDD `-2.8998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

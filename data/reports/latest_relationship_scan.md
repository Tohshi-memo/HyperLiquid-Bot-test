# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T14:52:32.120893+00:00`
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

- `market_context_high->unknown_4h` score `19.6482` n `97` status `ready` deltaP `-4.0828` edge `1.6981` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.4647` n `82` status `ready` deltaP `15.5022` edge `0.0638` maxDD `-3.6055`
- `risk_on_high->index_1h` score `0.4343` n `37` status `ready` deltaP `12.1541` edge `0.0017` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4343` n `37` status `ready` deltaP `12.1541` edge `0.0017` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.3885` n `37` status `ready` deltaP `13.9505` edge `-0.0009` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.3885` n `37` status `ready` deltaP `13.9505` edge `-0.0009` maxDD `-0.7172`
- `risk_on_high->fx_1h` score `0.2185` n `37` status `ready` deltaP `7.6469` edge `0.0029` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.2185` n `37` status `ready` deltaP `7.6469` edge `0.0029` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.1402` n `37` status `ready` deltaP `10.3276` edge `0.0289` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1402` n `37` status `ready` deltaP `10.3276` edge `0.0289` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `0.0004` n `37` status `ready` deltaP `3.0693` edge `0.006` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0004` n `37` status `ready` deltaP `3.0693` edge `0.006` maxDD `-0.1126`
- `market_context_high->commodity_4h` score `-0.1878` n `97` status `ready` deltaP `6.9855` edge `0.0281` maxDD `-2.8998`
- `market_context_high->fx_1h` score `-0.2366` n `109` status `ready` deltaP `0.3818` edge `0.0026` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.2657` n `97` status `ready` deltaP `2.8743` edge `0.0074` maxDD `-0.5168`
- `market_context_high->commodity_1h` score `-0.3243` n `109` status `ready` deltaP `3.1575` edge `0.0041` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.4427` n `37` status `ready` deltaP `-2.5733` edge `0.0063` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4427` n `37` status `ready` deltaP `-2.5733` edge `0.0063` maxDD `-0.0831`
- `risk_on_high->index_4h` score `-0.5026` n `37` status `ready` deltaP `4.7051` edge `-0.0113` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.5026` n `37` status `ready` deltaP `4.7051` edge `-0.0113` maxDD `-0.7604`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

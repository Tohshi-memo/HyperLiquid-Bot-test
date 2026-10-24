# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T11:52:28.111572+00:00`
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

- `market_context_high->commodity_24h` score `0.5546` n `82` status `ready` deltaP `16.1966` edge `0.0707` maxDD `-3.6055`
- `risk_on_high->index_1h` score `0.4421` n `37` status `ready` deltaP `12.3038` edge `0.0017` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4421` n `37` status `ready` deltaP `12.3038` edge `0.0017` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.3939` n `37` status `ready` deltaP `13.9505` edge `-0.0002` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.3939` n `37` status `ready` deltaP `13.9505` edge `-0.0002` maxDD `-0.7172`
- `risk_on_high->commodity_24h` score `0.2301` n `37` status `ready` deltaP `11.022` edge `0.0358` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2301` n `37` status `ready` deltaP `11.022` edge `0.0358` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.178` n `37` status `ready` deltaP `6.8984` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.178` n `37` status `ready` deltaP `6.8984` edge `0.0027` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.0328` n `37` status `ready` deltaP `2.4596` edge `0.0058` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0328` n `37` status `ready` deltaP `2.4596` edge `0.0058` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.0786` n `97` status `ready` deltaP `3.3598` edge `0.003` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.0875` n `86` status `ready` deltaP `6.1366` edge `0.0085` maxDD `-0.5168`
- `market_context_high->commodity_1h` score `-0.39` n `97` status `ready` deltaP `2.21` edge `0.002` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.4344` n `37` status `ready` deltaP `-2.4236` edge `0.006` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4344` n `37` status `ready` deltaP `-2.4236` edge `0.006` maxDD `-0.0831`
- `market_context_high->commodity_4h` score `-0.4999` n `86` status `ready` deltaP `2.634` edge `0.0171` maxDD `-2.8998`
- `risk_on_high->index_4h` score `-0.5129` n `37` status `ready` deltaP `4.5526` edge `-0.0116` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.5129` n `37` status `ready` deltaP `4.5526` edge `-0.0116` maxDD `-0.7604`
- `market_context_high->index_1h` score `-0.6387` n `97` status `ready` deltaP `-1.7949` edge `-0.0066` maxDD `-1.0653`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

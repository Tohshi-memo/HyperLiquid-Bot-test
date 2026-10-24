# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T13:52:27.161771+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7354`

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

- `market_context_high->unknown_4h` score `22.2413` n `93` status `ready` deltaP `-5.0583` edge `1.9207` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.4976` n `82` status `ready` deltaP `15.8494` edge `0.0657` maxDD `-3.6055`
- `risk_on_high->index_1h` score `0.4086` n `37` status `ready` deltaP `11.705` edge `0.0014` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4086` n `37` status `ready` deltaP `11.705` edge `0.0014` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.3386` n `37` status `ready` deltaP `13.3517` edge `-0.0033` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.3386` n `37` status `ready` deltaP `13.3517` edge `-0.0033` maxDD `-0.7172`
- `risk_on_high->fx_1h` score `0.1865` n `37` status `ready` deltaP `7.0481` edge `0.0028` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1865` n `37` status `ready` deltaP `7.0481` edge `0.0028` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.1731` n `37` status `ready` deltaP `10.6748` edge `0.0308` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1731` n `37` status `ready` deltaP `10.6748` edge `0.0308` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.0328` n `37` status `ready` deltaP `2.4596` edge `0.0058` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0328` n `37` status `ready` deltaP `2.4596` edge `0.0058` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1735` n `105` status `ready` deltaP `1.5654` edge `0.0028` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.1828` n `93` status `ready` deltaP `4.3486` edge `0.0082` maxDD `-0.5168`
- `market_context_high->commodity_4h` score `-0.2935` n `93` status `ready` deltaP `5.5222` edge `0.0243` maxDD `-2.8998`
- `market_context_high->commodity_1h` score `-0.326` n `105` status `ready` deltaP `3.1551` edge `0.0039` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.4715` n `37` status `ready` deltaP `-2.8727` edge `0.0059` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4715` n `37` status `ready` deltaP `-2.8727` edge `0.0059` maxDD `-0.0831`
- `risk_on_high->index_4h` score `-0.5295` n `37` status `ready` deltaP `4.2477` edge `-0.0117` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.5295` n `37` status `ready` deltaP `4.2477` edge `-0.0117` maxDD `-0.7604`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

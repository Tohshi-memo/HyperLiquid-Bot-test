# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T01:37:27.829289+00:00`
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

- `risk_on_high->equity_1h` score `0.6426` n `37` status `ready` deltaP `15.5972` edge `0.0207` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.6426` n `37` status `ready` deltaP `15.5972` edge `0.0207` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5325` n `37` status `ready` deltaP `13.5014` edge `0.0053` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5325` n `37` status `ready` deltaP `13.5014` edge `0.0053` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.5021` n `82` status `ready` deltaP `16.3702` edge `0.0628` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.1775` n `37` status `ready` deltaP `11.1956` edge `0.0279` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1775` n `37` status `ready` deltaP `11.1956` edge `0.0279` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.171` n `37` status `ready` deltaP `6.7487` edge `0.0028` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.171` n `37` status `ready` deltaP `6.7487` edge `0.0028` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.0694` n `82` status `ready` deltaP `3.9141` edge `0.0036` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.0907` n `37` status `ready` deltaP `1.3925` edge `0.0055` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0907` n `37` status `ready` deltaP `1.3925` edge `0.0055` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.1386` n `82` status `ready` deltaP `5.1829` edge `0.0083` maxDD `-0.5168`
- `market_context_high->index_1h` score `-0.2309` n `82` status `ready` deltaP `4.0419` edge `-0.0029` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.28` n `37` status `ready` deltaP `6.9916` edge `0.002` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.28` n `37` status `ready` deltaP `6.9916` edge `0.002` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.3936` n `37` status `ready` deltaP `-2.1242` edge `0.0074` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.3936` n `37` status `ready` deltaP `-2.1242` edge `0.0074` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.5794` n `82` status `ready` deltaP `-0.6828` edge `-0.003` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.8486` n `82` status `ready` deltaP `-1.3719` edge `-0.0009` maxDD `-2.8998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

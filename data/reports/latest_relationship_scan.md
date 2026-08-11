# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T10:52:26.436708+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `47.0698` n `127` status `ready` deltaP `-18.7803` edge `4.2931` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.8662` n `32` status `ready` deltaP `18.6738` edge `0.1326` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8662` n `32` status `ready` deltaP `18.6738` edge `0.1326` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `1.7021` n `127` status `ready` deltaP `12.1249` edge `0.1497` maxDD `-3.0953`
- `risk_on_high->commodity_1h` score `1.3163` n `32` status `ready` deltaP `13.5105` edge `0.0429` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3163` n `32` status `ready` deltaP `13.5105` edge `0.0429` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9585` n `32` status `ready` deltaP `11.0518` edge `0.0203` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9585` n `32` status `ready` deltaP `11.0518` edge `0.0203` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.9316` n `181` status `ready` deltaP `11.8195` edge `0.0703` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.857` n `181` status `ready` deltaP `11.0588` edge `0.0314` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.4496` n `127` status `ready` deltaP `16.0209` edge `0.0316` maxDD `-1.4613`
- `risk_on_high->index_1h` score `0.2104` n `32` status `ready` deltaP `8.6078` edge `0.0071` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2104` n `32` status `ready` deltaP `8.6078` edge `0.0071` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.173` n `32` status `ready` deltaP `5.2021` edge `0.0025` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.173` n `32` status `ready` deltaP `5.2021` edge `0.0025` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.0777` n `181` status `ready` deltaP `4.7532` edge `0.0007` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1343` n `181` status `ready` deltaP `5.6478` edge `0.0056` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.5022` n `32` status `ready` deltaP `-1.4482` edge `0.0035` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5022` n `32` status `ready` deltaP `-1.4482` edge `0.0035` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.8175` n `32` status `ready` deltaP `-4.9588` edge `-0.0174` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

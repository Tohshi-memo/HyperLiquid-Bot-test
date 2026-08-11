# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T10:37:28.368641+00:00`
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

- `market_context_high->unknown_24h` score `47.065` n `127` status `ready` deltaP `-18.7803` edge `4.2927` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.8492` n `32` status `ready` deltaP `18.5213` edge `0.1322` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8492` n `32` status `ready` deltaP `18.5213` edge `0.1322` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `1.7604` n `127` status `ready` deltaP `12.2982` edge `0.1534` maxDD `-3.0953`
- `risk_on_high->commodity_1h` score `1.2995` n `32` status `ready` deltaP `13.3608` edge `0.0425` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2995` n `32` status `ready` deltaP `13.3608` edge `0.0425` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9451` n `32` status `ready` deltaP `10.8994` edge `0.0202` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9451` n `32` status `ready` deltaP `10.8994` edge `0.0202` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.9146` n `181` status `ready` deltaP `11.667` edge `0.0699` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8403` n `181` status `ready` deltaP `10.9091` edge `0.031` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.4496` n `127` status `ready` deltaP `16.0209` edge `0.0316` maxDD `-1.4613`
- `risk_on_high->index_1h` score `0.2096` n `32` status `ready` deltaP `8.6078` edge `0.007` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2096` n `32` status `ready` deltaP `8.6078` edge `0.007` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.173` n `32` status `ready` deltaP `5.2021` edge `0.0025` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.173` n `32` status `ready` deltaP `5.2021` edge `0.0025` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.0777` n `181` status `ready` deltaP `4.7532` edge `0.0007` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.143` n `181` status `ready` deltaP `5.4954` edge `0.0055` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.5029` n `32` status `ready` deltaP `-1.4482` edge `0.0034` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5029` n `32` status `ready` deltaP `-1.4482` edge `0.0034` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.819` n `32` status `ready` deltaP `-4.9588` edge `-0.0176` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

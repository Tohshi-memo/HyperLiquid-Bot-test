# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T00:22:26.633248+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11856`

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

- `risk_on_high->commodity_4h` score `2.2879` n `32` status `ready` deltaP `15.9299` edge `0.1027` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2879` n `32` status `ready` deltaP `15.9299` edge `0.1027` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.0969` n `32` status `ready` deltaP `12.0135` edge `0.0346` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0969` n `32` status `ready` deltaP `12.0135` edge `0.0346` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.052` n `32` status `ready` deltaP `11.9665` edge `0.022` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.052` n `32` status `ready` deltaP `11.9665` edge `0.022` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6901` n `180` status `ready` deltaP `9.9302` edge `0.0235` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.5544` n `180` status `ready` deltaP `9.4716` edge `0.0469` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.4027` n `32` status `ready` deltaP `11.6018` edge `0.0118` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.4027` n `32` status `ready` deltaP `11.6018` edge `0.0118` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.2029` n `32` status `ready` deltaP `5.5015` edge `0.003` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2029` n `32` status `ready` deltaP `5.5015` edge `0.003` maxDD `-0.1547`
- `market_context_high->commodity_24h` score `0.0651` n `156` status `ready` deltaP `7.6134` edge `0.035` maxDD `-2.4263`
- `market_context_high->fx_1h` score `-0.0725` n `180` status `ready` deltaP `4.8071` edge `0.001` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0857` n `180` status `ready` deltaP `6.3415` edge `0.0072` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.2457` n `32` status `ready` deltaP `1.1433` edge `0.0191` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.2457` n `32` status `ready` deltaP `1.1433` edge `0.0191` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.6079` n `32` status `ready` deltaP `-3.0127` edge `-0.0035` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.6079` n `32` status `ready` deltaP `-3.0127` edge `-0.0035` maxDD `-1.6811`
- `market_context_high->fx_24h` score `-0.6975` n `156` status `ready` deltaP `7.138` edge `0.0151` maxDD `-1.8358`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T13:52:27.428746+00:00`
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

- `market_context_high->unknown_24h` score `36.6853` n `130` status `ready` deltaP `-19.0175` edge `3.4293` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `3.0538` n `32` status `ready` deltaP `19.8933` edge `0.1401` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0538` n `32` status `ready` deltaP `19.8933` edge `0.1401` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.3343` n `32` status `ready` deltaP `13.5105` edge `0.0444` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3343` n `32` status `ready` deltaP `13.5105` edge `0.0444` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.1192` n `181` status `ready` deltaP `13.039` edge `0.0778` maxDD `-2.7169`
- `risk_on_high->fx_4h` score `1.1032` n `32` status `ready` deltaP `12.5762` edge `0.0222` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.1032` n `32` status `ready` deltaP `12.5762` edge `0.0222` maxDD `-0.1285`
- `market_context_high->commodity_24h` score `1.099` n `130` status `ready` deltaP `10.4813` edge `0.1104` maxDD `-3.0953`
- `market_context_high->commodity_1h` score `0.8195` n `182` status `ready` deltaP `10.6946` edge `0.0307` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.4044` n `130` status `ready` deltaP `15.4073` edge `0.0299` maxDD `-1.4613`
- `risk_on_high->fx_1h` score `0.2412` n `32` status `ready` deltaP `5.9506` edge `0.0032` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2412` n `32` status `ready` deltaP `5.9506` edge `0.0032` maxDD `-0.1547`
- `risk_on_high->index_1h` score `0.2306` n `32` status `ready` deltaP `8.9072` edge `0.0077` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2306` n `32` status `ready` deltaP `8.9072` edge `0.0077` maxDD `-0.3343`
- `market_context_high->fx_4h` score `-0.0402` n `181` status `ready` deltaP `7.1722` edge `0.0075` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.0508` n `182` status `ready` deltaP `5.1951` edge `0.0012` maxDD `-0.3878`
- `risk_on_high->index_4h` score `-0.5337` n `32` status `ready` deltaP `-1.9055` edge `0.0025` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5337` n `32` status `ready` deltaP `-1.9055` edge `0.0025` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.7676` n `32` status `ready` deltaP `-4.5097` edge `-0.014` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

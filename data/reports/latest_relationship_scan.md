# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T12:52:28.029069+00:00`
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

- `market_context_high->unknown_24h` score `47.1485` n `127` status `ready` deltaP `-18.607` edge `4.2985` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `3.0346` n `32` status `ready` deltaP `19.8933` edge `0.1385` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0346` n `32` status `ready` deltaP `19.8933` edge `0.1385` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.2732` n `32` status `ready` deltaP `12.9117` edge `0.0433` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2732` n `32` status `ready` deltaP `12.9117` edge `0.0433` maxDD `-0.1957`
- `market_context_high->commodity_24h` score `1.26` n `127` status `ready` deltaP `10.7384` edge `0.1221` maxDD `-3.0953`
- `market_context_high->commodity_4h` score `1.1` n `181` status `ready` deltaP `13.039` edge `0.0762` maxDD `-2.7169`
- `risk_on_high->fx_4h` score `1.0752` n `32` status `ready` deltaP `12.2713` edge `0.0219` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0752` n `32` status `ready` deltaP `12.2713` edge `0.0219` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.7584` n `182` status `ready` deltaP `10.0958` edge `0.0296` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.4993` n `127` status `ready` deltaP `16.8875` edge `0.0322` maxDD `-1.4613`
- `risk_on_high->fx_1h` score `0.2269` n `32` status `ready` deltaP `5.8009` edge `0.003` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2269` n `32` status `ready` deltaP `5.8009` edge `0.003` maxDD `-0.1547`
- `risk_on_high->index_1h` score `0.2127` n `32` status `ready` deltaP `8.6078` edge `0.0074` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2127` n `32` status `ready` deltaP `8.6078` edge `0.0074` maxDD `-0.3343`
- `market_context_high->fx_4h` score `-0.0584` n `181` status `ready` deltaP `6.8673` edge `0.0072` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.0601` n `182` status `ready` deltaP `5.0454` edge `0.001` maxDD `-0.3878`
- `risk_on_high->index_4h` score `-0.5337` n `32` status `ready` deltaP `-1.9055` edge `0.0025` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5337` n `32` status `ready` deltaP `-1.9055` edge `0.0025` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.7879` n `32` status `ready` deltaP `-4.6594` edge `-0.0156` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

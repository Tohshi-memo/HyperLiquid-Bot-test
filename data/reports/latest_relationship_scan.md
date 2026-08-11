# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T13:07:34.454404+00:00`
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

- `market_context_high->unknown_24h` score `43.6477` n `128` status `ready` deltaP `-18.3425` edge `4.005` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `3.0418` n `32` status `ready` deltaP `19.8933` edge `0.1391` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0418` n `32` status `ready` deltaP `19.8933` edge `0.1391` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.2864` n `32` status `ready` deltaP `13.0614` edge `0.0434` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2864` n `32` status `ready` deltaP `13.0614` edge `0.0434` maxDD `-0.1957`
- `market_context_high->commodity_24h` score `1.2291` n `128` status `ready` deltaP `10.7127` edge `0.1197` maxDD `-3.0953`
- `market_context_high->commodity_4h` score `1.1072` n `181` status `ready` deltaP `13.039` edge `0.0768` maxDD `-2.7169`
- `risk_on_high->fx_4h` score `1.0764` n `32` status `ready` deltaP `12.2713` edge `0.022` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0764` n `32` status `ready` deltaP `12.2713` edge `0.022` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.7716` n `182` status `ready` deltaP `10.2455` edge `0.0297` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.4648` n `128` status `ready` deltaP `16.3278` edge `0.0315` maxDD `-1.4613`
- `risk_on_high->fx_1h` score `0.2149` n `32` status `ready` deltaP `5.6512` edge `0.003` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2149` n `32` status `ready` deltaP `5.6512` edge `0.003` maxDD `-0.1547`
- `risk_on_high->index_1h` score `0.2135` n `32` status `ready` deltaP `8.6078` edge `0.0075` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2135` n `32` status `ready` deltaP `8.6078` edge `0.0075` maxDD `-0.3343`
- `market_context_high->fx_4h` score `-0.0576` n `181` status `ready` deltaP `6.8673` edge `0.0073` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.0679` n `182` status `ready` deltaP `4.8957` edge `0.001` maxDD `-0.3878`
- `risk_on_high->index_4h` score `-0.5345` n `32` status `ready` deltaP `-1.9055` edge `0.0024` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5345` n `32` status `ready` deltaP `-1.9055` edge `0.0024` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.7871` n `32` status `ready` deltaP `-4.6594` edge `-0.0155` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

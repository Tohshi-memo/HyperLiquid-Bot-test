# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T14:22:35.757355+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `33.2927` n `131` status `ready` deltaP `-19.17` edge `3.1476` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `3.037` n `32` status `ready` deltaP `19.8933` edge `0.1387` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.037` n `32` status `ready` deltaP `19.8933` edge `0.1387` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.3535` n `32` status `ready` deltaP `13.6602` edge `0.045` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3535` n `32` status `ready` deltaP `13.6602` edge `0.045` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.102` n `32` status `ready` deltaP `12.5762` edge `0.0221` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.102` n `32` status `ready` deltaP `12.5762` edge `0.0221` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `1.0435` n `182` status `ready` deltaP `12.6474` edge `0.0741` maxDD `-2.7169`
- `market_context_high->commodity_24h` score `1.0142` n `131` status `ready` deltaP `10.2756` edge `0.1047` maxDD `-3.0953`
- `market_context_high->commodity_1h` score `0.8387` n `182` status `ready` deltaP `10.8443` edge `0.0313` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.381` n `131` status `ready` deltaP `15.0462` edge `0.0293` maxDD `-1.4613`
- `risk_on_high->fx_1h` score `0.2532` n `32` status `ready` deltaP `6.1003` edge `0.0032` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2532` n `32` status `ready` deltaP `6.1003` edge `0.0032` maxDD `-0.1547`
- `risk_on_high->index_1h` score `0.2213` n `32` status `ready` deltaP `8.7575` edge `0.0075` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2213` n `32` status `ready` deltaP `8.7575` edge `0.0075` maxDD `-0.3343`
- `market_context_high->fx_1h` score `-0.043` n `182` status `ready` deltaP `5.3448` edge `0.0012` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0597` n `182` status `ready` deltaP `6.8413` edge `0.0072` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.533` n `32` status `ready` deltaP `-1.9055` edge `0.0026` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.533` n `32` status `ready` deltaP `-1.9055` edge `0.0026` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.7894` n `32` status `ready` deltaP `-4.6594` edge `-0.0158` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T12:07:37.073066+00:00`
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

- `market_context_high->unknown_24h` score `47.1034` n `127` status `ready` deltaP `-18.7803` edge `4.2959` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.9764` n `32` status `ready` deltaP `19.436` edge `0.1367` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9764` n `32` status `ready` deltaP `19.436` edge `0.1367` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `1.4252` n `127` status `ready` deltaP `11.2584` edge `0.1324` maxDD `-3.0953`
- `risk_on_high->commodity_1h` score `1.3211` n `32` status `ready` deltaP `13.3608` edge `0.0443` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3211` n `32` status `ready` deltaP `13.3608` edge `0.0443` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.0418` n `181` status `ready` deltaP `12.5817` edge `0.0744` maxDD `-2.7169`
- `risk_on_high->fx_4h` score `1.0338` n `32` status `ready` deltaP `11.814` edge `0.0215` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0338` n `32` status `ready` deltaP `11.814` edge `0.0215` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.8063` n `182` status `ready` deltaP `10.5449` edge `0.0306` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.4993` n `127` status `ready` deltaP `16.8875` edge `0.0322` maxDD `-1.4613`
- `risk_on_high->fx_1h` score `0.2281` n `32` status `ready` deltaP `5.8009` edge `0.0031` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2281` n `32` status `ready` deltaP `5.8009` edge `0.0031` maxDD `-0.1547`
- `risk_on_high->index_1h` score `0.2205` n `32` status `ready` deltaP `8.7575` edge `0.0074` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2205` n `32` status `ready` deltaP `8.7575` edge `0.0074` maxDD `-0.3343`
- `market_context_high->fx_1h` score `-0.0594` n `182` status `ready` deltaP `5.0454` edge `0.0011` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0853` n `181` status `ready` deltaP `6.41` edge `0.0068` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.5132` n `32` status `ready` deltaP `-1.6006` edge `0.0031` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5132` n `32` status `ready` deltaP `-1.6006` edge `0.0031` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.8011` n `32` status `ready` deltaP `-4.8091` edge `-0.0163` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

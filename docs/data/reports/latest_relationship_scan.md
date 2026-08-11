# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T12:22:33.880189+00:00`
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

- `market_context_high->unknown_24h` score `47.1281` n `127` status `ready` deltaP `-18.607` edge `4.2968` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.9982` n `32` status `ready` deltaP `19.5884` edge `0.1375` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9982` n `32` status `ready` deltaP `19.5884` edge `0.1375` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `1.3705` n `127` status `ready` deltaP `11.0851` edge `0.129` maxDD `-3.0953`
- `risk_on_high->commodity_1h` score `1.3055` n `32` status `ready` deltaP `13.2111` edge `0.044` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3055` n `32` status `ready` deltaP `13.2111` edge `0.044` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.0636` n `181` status `ready` deltaP `12.7341` edge `0.0752` maxDD `-2.7169`
- `risk_on_high->fx_4h` score `1.0472` n `32` status `ready` deltaP `11.9665` edge `0.0216` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0472` n `32` status `ready` deltaP `11.9665` edge `0.0216` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.7907` n `182` status `ready` deltaP `10.3952` edge `0.0303` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.4993` n `127` status `ready` deltaP `16.8875` edge `0.0322` maxDD `-1.4613`
- `risk_on_high->fx_1h` score `0.2281` n `32` status `ready` deltaP `5.8009` edge `0.0031` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2281` n `32` status `ready` deltaP `5.8009` edge `0.0031` maxDD `-0.1547`
- `risk_on_high->index_1h` score `0.2205` n `32` status `ready` deltaP `8.7575` edge `0.0074` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2205` n `32` status `ready` deltaP `8.7575` edge `0.0074` maxDD `-0.3343`
- `market_context_high->fx_1h` score `-0.0594` n `182` status `ready` deltaP `5.0454` edge `0.0011` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0766` n `181` status `ready` deltaP `6.5625` edge `0.0069` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.5227` n `32` status `ready` deltaP `-1.753` edge `0.0029` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5227` n `32` status `ready` deltaP `-1.753` edge `0.0029` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.8003` n `32` status `ready` deltaP `-4.8091` edge `-0.0162` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T13:22:35.173711+00:00`
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

- `market_context_high->unknown_24h` score `40.144` n `129` status `ready` deltaP `-18.6839` edge `3.7153` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `3.049` n `32` status `ready` deltaP `19.8933` edge `0.1397` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.049` n `32` status `ready` deltaP `19.8933` edge `0.1397` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.3019` n `32` status `ready` deltaP `13.2111` edge `0.0437` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3019` n `32` status `ready` deltaP `13.2111` edge `0.0437` maxDD `-0.1957`
- `market_context_high->commodity_24h` score `1.1945` n `129` status `ready` deltaP `10.6847` edge `0.117` maxDD `-3.0953`
- `market_context_high->commodity_4h` score `1.1144` n `181` status `ready` deltaP `13.039` edge `0.0774` maxDD `-2.7169`
- `risk_on_high->fx_4h` score `1.0886` n `32` status `ready` deltaP `12.4238` edge `0.022` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0886` n `32` status `ready` deltaP `12.4238` edge `0.022` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.7871` n `182` status `ready` deltaP `10.3952` edge `0.03` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.4397` n `129` status `ready` deltaP `15.9499` edge `0.0308` maxDD `-1.4613`
- `risk_on_high->index_1h` score `0.2213` n `32` status `ready` deltaP `8.7575` edge `0.0075` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2213` n `32` status `ready` deltaP `8.7575` edge `0.0075` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.2149` n `32` status `ready` deltaP `5.6512` edge `0.003` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2149` n `32` status `ready` deltaP `5.6512` edge `0.003` maxDD `-0.1547`
- `market_context_high->fx_4h` score `-0.0497` n `181` status `ready` deltaP `7.0198` edge `0.0073` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.0679` n `182` status `ready` deltaP `4.8957` edge `0.001` maxDD `-0.3878`
- `risk_on_high->index_4h` score `-0.5353` n `32` status `ready` deltaP `-1.9055` edge `0.0023` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5353` n `32` status `ready` deltaP `-1.9055` edge `0.0023` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.7832` n `32` status `ready` deltaP `-4.6594` edge `-0.015` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

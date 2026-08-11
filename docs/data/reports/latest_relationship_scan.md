# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T17:22:30.607016+00:00`
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

- `market_context_high->unknown_24h` score `10.7854` n `138` status `ready` deltaP `-21.1061` edge `1.2849` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.6548` n `32` status `ready` deltaP `18.5213` edge `0.116` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6548` n `32` status `ready` deltaP `18.5213` edge `0.116` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.2048` n `32` status `ready` deltaP `12.6123` edge `0.0396` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2048` n `32` status `ready` deltaP `12.6123` edge `0.0396` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0085` n `32` status `ready` deltaP `11.6616` edge `0.0204` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0085` n `32` status `ready` deltaP `11.6616` edge `0.0204` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.88` n `181` status `ready` deltaP `11.667` edge `0.0594` maxDD `-2.1077`
- `market_context_high->commodity_1h` score `0.765` n `181` status `ready` deltaP `10.1606` edge `0.0282` maxDD `-0.5752`
- `market_context_high->commodity_24h` score `0.7552` n `138` status `ready` deltaP `9.8498` edge `0.0776` maxDD `-2.4263`
- `risk_on_high->index_1h` score `0.2851` n `32` status `ready` deltaP `9.8054` edge `0.0087` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2851` n `32` status `ready` deltaP `9.8054` edge `0.0087` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.2005` n `32` status `ready` deltaP `5.5015` edge `0.0028` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2005` n `32` status `ready` deltaP `5.5015` edge `0.0028` maxDD `-0.1547`
- `market_context_high->fx_24h` score `0.1352` n `138` status `ready` deltaP `11.1446` edge `0.0238` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.0606` n `181` status `ready` deltaP `5.0526` edge `0.0009` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0994` n `181` status `ready` deltaP `6.2576` edge `0.006` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.4108` n `32` status `ready` deltaP `-0.3811` edge `0.0081` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.4108` n `32` status `ready` deltaP `-0.3811` edge `0.0081` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.6936` n `32` status `ready` deltaP `-3.6115` edge `-0.0105` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

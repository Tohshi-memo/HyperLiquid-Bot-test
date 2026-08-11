# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T11:52:23.638715+00:00`
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

- `market_context_high->unknown_24h` score `47.0962` n `127` status `ready` deltaP `-18.7803` edge `4.2953` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.9534` n `32` status `ready` deltaP `19.2835` edge `0.1358` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9534` n `32` status `ready` deltaP `19.2835` edge `0.1358` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `1.481` n `127` status `ready` deltaP `11.4317` edge `0.1359` maxDD `-3.0953`
- `risk_on_high->commodity_1h` score `1.3367` n `32` status `ready` deltaP `13.5105` edge `0.0446` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3367` n `32` status `ready` deltaP `13.5105` edge `0.0446` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0193` n `32` status `ready` deltaP `11.6616` edge `0.0213` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0193` n `32` status `ready` deltaP `11.6616` edge `0.0213` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `1.0188` n `181` status `ready` deltaP `12.4292` edge `0.0735` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8219` n `182` status `ready` deltaP `10.6946` edge `0.0309` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.4903` n `127` status `ready` deltaP `16.7142` edge `0.0322` maxDD `-1.4613`
- `risk_on_high->fx_1h` score `0.2269` n `32` status `ready` deltaP `5.8009` edge `0.003` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2269` n `32` status `ready` deltaP `5.8009` edge `0.003` maxDD `-0.1547`
- `risk_on_high->index_1h` score `0.2127` n `32` status `ready` deltaP `8.6078` edge `0.0074` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2127` n `32` status `ready` deltaP `8.6078` edge `0.0074` maxDD `-0.3343`
- `market_context_high->fx_1h` score `-0.0601` n `182` status `ready` deltaP `5.0454` edge `0.001` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0948` n `181` status `ready` deltaP `6.2576` edge `0.0066` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.5045` n `32` status `ready` deltaP `-1.4482` edge `0.0032` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5045` n `32` status `ready` deltaP `-1.4482` edge `0.0032` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.8128` n `32` status `ready` deltaP `-4.9588` edge `-0.0168` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

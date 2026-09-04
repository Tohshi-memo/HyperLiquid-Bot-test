# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T06:22:22.948493+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11478`

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

- `risk_on_high->unknown_4h` score `21.0353` n `133` status `ready` deltaP `8.846` edge `1.7558` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `21.0353` n `133` status `ready` deltaP `8.846` edge `1.7558` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `15.0822` n `172` status `ready` deltaP `11.0536` edge `1.2527` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.6164` n `133` status `ready` deltaP `-0.7542` edge `1.1141` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.6164` n `133` status `ready` deltaP `-0.7542` edge `1.1141` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.9801` n `182` status `ready` deltaP `0.8653` edge `0.9723` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.3923` n `153` status `ready` deltaP `16.7688` edge `0.4388` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `1.3263` n `131` status `ready` deltaP `13.3562` edge `0.436` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.3263` n `131` status `ready` deltaP `13.3562` edge `0.436` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.2616` n `67` status `ready` deltaP `5.0328` edge `0.0359` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.1179` n `133` status `ready` deltaP `12.4128` edge `0.0036` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1179` n `133` status `ready` deltaP `12.4128` edge `0.0036` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.1325` n `67` status `ready` deltaP `3.2778` edge `-0.0035` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1707` n `133` status `ready` deltaP `3.693` edge `-0.002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1707` n `133` status `ready` deltaP `3.693` edge `-0.002` maxDD `-0.5605`
- `news_risk_high->commodity_1h` score `-0.1729` n `67` status `ready` deltaP `4.4575` edge `0.0005` maxDD `-0.9036`
- `risk_on_high->crypto_alt_1h` score `-0.1874` n `133` status `ready` deltaP `5.0504` edge `0.0524` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.1874` n `133` status `ready` deltaP `5.0504` edge `0.0524` maxDD `-5.4685`
- `news_risk_high->commodity_24h` score `-0.1949` n `67` status `ready` deltaP `4.2781` edge `-0.0255` maxDD `-0.2074`
- `market_context_high->metal_1h` score `-0.3522` n `182` status `ready` deltaP `6.1953` edge `-0.0008` maxDD `-2.1858`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

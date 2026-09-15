# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T08:07:32.576450+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11176`

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

- `news_risk_high->unknown_4h` score `399.1632` n `78` status `ready` deltaP `-22.1505` edge `33.5006` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `21.9507` n `78` status `ready` deltaP `18.2292` edge `1.7077` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.4831` n `78` status `ready` deltaP `44.4712` edge `1.5329` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.1457` n `78` status `ready` deltaP `34.1747` edge `1.2647` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.8602` n `78` status `ready` deltaP `47.7697` edge `1.0979` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6298` n `78` status `ready` deltaP `61.4182` edge `0.3273` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.468` n `78` status `ready` deltaP `37.9674` edge `0.3313` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0286` n `52` status `ready` deltaP `38.3681` edge `0.2466` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0286` n `52` status `ready` deltaP `38.3681` edge `0.2466` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7317` n `137` status `ready` deltaP `31.0688` edge `0.2397` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.8896` n `52` status `ready` deltaP `44.6047` edge `0.031` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.8896` n `52` status `ready` deltaP `44.6047` edge `0.031` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.4926` n `137` status `ready` deltaP `41.4183` edge `0.0365` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9531` n `52` status `ready` deltaP `25.0703` edge `0.0306` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9531` n `52` status `ready` deltaP `25.0703` edge `0.0306` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8529` n `149` status `ready` deltaP `21.5726` edge `0.0524` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.827` n `149` status `ready` deltaP `13.3666` edge `0.0175` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6647` n `78` status `ready` deltaP `16.6588` edge `0.037` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2494` n `52` status `ready` deltaP `8.2105` edge `0.0078` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2494` n `52` status `ready` deltaP `8.2105` edge `0.0078` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

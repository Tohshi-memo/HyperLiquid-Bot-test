# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T08:22:29.739912+00:00`
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

- `news_risk_high->unknown_4h` score `398.8212` n `78` status `ready` deltaP `-22.1505` edge `33.4721` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `21.8823` n `78` status `ready` deltaP `18.2292` edge `1.702` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.5522` n `78` status `ready` deltaP `44.6448` edge `1.5375` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.2196` n `78` status `ready` deltaP `34.3483` edge `1.2697` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.9005` n `78` status `ready` deltaP `47.9434` edge `1.1001` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6461` n `78` status `ready` deltaP `61.5918` edge `0.3275` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4891` n `78` status `ready` deltaP `38.141` edge `0.3319` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0262` n `52` status `ready` deltaP `38.3681` edge `0.2464` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0262` n `52` status `ready` deltaP `38.3681` edge `0.2464` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7293` n `137` status `ready` deltaP `31.0688` edge `0.2395` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.8685` n `52` status `ready` deltaP `44.4311` edge `0.0304` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.8685` n `52` status `ready` deltaP `44.4311` edge `0.0304` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.4715` n `137` status `ready` deltaP `41.2447` edge `0.0359` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9519` n `52` status `ready` deltaP `25.0703` edge `0.0305` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9519` n `52` status `ready` deltaP `25.0703` edge `0.0305` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8517` n `149` status `ready` deltaP `21.5726` edge `0.0523` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.827` n `149` status `ready` deltaP `13.3666` edge `0.0175` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6742` n `78` status `ready` deltaP `16.8113` edge `0.0372` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2494` n `52` status `ready` deltaP `8.2105` edge `0.0078` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2494` n `52` status `ready` deltaP `8.2105` edge `0.0078` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

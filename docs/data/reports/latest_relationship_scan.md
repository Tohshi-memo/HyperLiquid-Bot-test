# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T15:07:29.705412+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10887`

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

- `news_risk_high->unknown_4h` score `396.4202` n `78` status `ready` deltaP `-23.2176` edge `33.2792` maxDD `-4.1517`
- `news_risk_high->crypto_alt_24h` score `22.7303` n `78` status `ready` deltaP `47.5962` edge `1.616` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `22.6446` n `78` status `ready` deltaP `21.0069` edge `1.747` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `17.8551` n `78` status `ready` deltaP `38.8622` edge `1.3759` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.2084` n `78` status `ready` deltaP `49.3322` edge `1.1159` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.4261` n `78` status `ready` deltaP `59.6821` edge `0.3219` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4522` n `78` status `ready` deltaP `37.6202` edge `0.3323` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0208` n `52` status `ready` deltaP `38.1944` edge `0.2471` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0208` n `52` status `ready` deltaP `38.1944` edge `0.2471` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7238` n `137` status `ready` deltaP `30.8951` edge `0.2402` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.3291` n `52` status `ready` deltaP `39.7436` edge `0.0167` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.3291` n `52` status `ready` deltaP `39.7436` edge `0.0167` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.9321` n `137` status `ready` deltaP `36.5572` edge `0.0222` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.675` n `52` status `ready` deltaP `23.3935` edge `0.0186` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.675` n `52` status `ready` deltaP `23.3935` edge `0.0186` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.5747` n `149` status `ready` deltaP `19.8958` edge `0.0404` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.717` n `78` status `ready` deltaP `17.5735` edge `0.0376` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.7059` n `149` status `ready` deltaP `12.3187` edge `0.0144` maxDD `-0.3491`
- `risk_on_high->metal_1h` score `0.1957` n `52` status `ready` deltaP `7.3123` edge `0.0069` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.1957` n `52` status `ready` deltaP `7.3123` edge `0.0069` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

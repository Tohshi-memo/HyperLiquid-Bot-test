# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T01:37:31.793190+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10858`

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

- `news_risk_high->unknown_4h` score `400.1552` n `78` status `ready` deltaP `-22.4554` edge `33.5853` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.4975` n `78` status `ready` deltaP `18.9236` edge `1.9153` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.1185` n `78` status `ready` deltaP `43.6031` edge `1.5083` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.5981` n `78` status `ready` deltaP `32.265` edge `1.2318` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.1443` n `78` status `ready` deltaP `43.9503` edge `1.0637` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6205` n `78` status `ready` deltaP `60.8974` edge `0.33` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4457` n `78` status `ready` deltaP `37.7938` edge `0.3306` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.06` n `52` status `ready` deltaP `38.7153` edge `0.2469` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.06` n `52` status `ready` deltaP `38.7153` edge `0.2469` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.763` n `137` status `ready` deltaP `31.416` edge `0.24` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.1819` n `52` status `ready` deltaP `47.2088` edge `0.038` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.1819` n `52` status `ready` deltaP `47.2088` edge `0.038` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.7849` n `137` status `ready` deltaP `44.0224` edge `0.0435` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9111` n `52` status `ready` deltaP `25.0703` edge `0.0271` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9111` n `52` status `ready` deltaP `25.0703` edge `0.0271` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7115` n `137` status `ready` deltaP `20.4802` edge `0.0479` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.7284` n `78` status `ready` deltaP `17.2686` edge `0.0411` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.6486` n `142` status `ready` deltaP `11.3625` edge `0.016` maxDD `-0.3491`
- `risk_on_high->metal_1h` score `0.2284` n `52` status `ready` deltaP `7.7614` edge `0.0081` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2284` n `52` status `ready` deltaP `7.7614` edge `0.0081` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

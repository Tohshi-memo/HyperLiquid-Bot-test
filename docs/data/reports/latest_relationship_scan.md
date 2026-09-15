# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T07:37:27.179320+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11166`

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

- `news_risk_high->unknown_4h` score `399.5846` n `78` status `ready` deltaP `-21.9981` edge `33.5347` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `22.1259` n `78` status `ready` deltaP `18.2292` edge `1.7223` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.3413` n `78` status `ready` deltaP `44.1239` edge `1.5234` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.9931` n `78` status `ready` deltaP `33.8275` edge `1.2543` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.7749` n `78` status `ready` deltaP `47.4225` edge `1.0931` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.596` n `78` status `ready` deltaP `61.071` edge `0.3268` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4536` n `78` status `ready` deltaP `37.9674` edge `0.3301` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.066` n `52` status `ready` deltaP `38.7153` edge `0.2474` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.066` n `52` status `ready` deltaP `38.7153` edge `0.2474` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7691` n `137` status `ready` deltaP `31.416` edge `0.2405` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.9317` n `52` status `ready` deltaP `44.9519` edge `0.0322` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.9317` n `52` status `ready` deltaP `44.9519` edge `0.0322` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.5347` n `137` status `ready` deltaP `41.7655` edge `0.0377` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9713` n `52` status `ready` deltaP `25.2228` edge `0.0311` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9713` n `52` status `ready` deltaP `25.2228` edge `0.0311` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8711` n `149` status `ready` deltaP `21.7251` edge `0.0529` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8258` n `149` status `ready` deltaP `13.3666` edge `0.0174` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6529` n `78` status `ready` deltaP `16.5064` edge `0.0365` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2471` n `52` status `ready` deltaP `8.2105` edge `0.0075` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2471` n `52` status `ready` deltaP `8.2105` edge `0.0075` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

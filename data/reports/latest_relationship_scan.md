# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T23:22:31.054541+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8098`

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

- `news_risk_high->crypto_major_24h` score `56.856` n `39` status `ready` deltaP `32.2783` edge `4.612` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `52.2529` n `39` status `ready` deltaP `33.7073` edge `4.2676` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.8783` n `149` status `ready` deltaP `-1.0732` edge `3.187` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `12.7386` n `39` status `ready` deltaP `44.9119` edge `0.7846` maxDD `-0.7969`
- `risk_on_high->unknown_4h` score `11.7569` n `52` status `ready` deltaP `-8.3138` edge `1.0577` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.7569` n `52` status `ready` deltaP `-8.3138` edge `1.0577` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `9.0503` n `75` status `ready` deltaP `28.815` edge `0.6747` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2838` n `149` status `ready` deltaP `41.2053` edge `0.3848` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `5.9687` n `75` status `ready` deltaP `25.311` edge `0.4461` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.3623` n `39` status `ready` deltaP `32.0112` edge `0.1659` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.3188` n `75` status `ready` deltaP `18.529` edge `0.1996` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.9305` n `75` status `ready` deltaP `22.3793` edge `0.1473` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.8125` n `52` status `ready` deltaP `32.6923` edge `0.0514` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8125` n `52` status `ready` deltaP `32.6923` edge `0.0514` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7122` n `149` status `ready` deltaP `29.1946` edge `0.0732` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.6132` n `75` status `ready` deltaP `13.5793` edge `0.1339` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.3677` n `75` status `ready` deltaP `14.9492` edge `0.0362` maxDD `-0.084`
- `news_risk_high->equity_1h` score `1.28` n `75` status `ready` deltaP `14.7485` edge `0.0489` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

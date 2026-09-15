# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T11:37:34.938457+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11210`

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

- `news_risk_high->unknown_4h` score `396.7592` n `78` status `ready` deltaP `-22.4554` edge `33.3023` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `22.1253` n `78` status `ready` deltaP `46.0337` edge `1.576` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `21.9934` n `78` status `ready` deltaP `19.6181` edge `1.702` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `16.9665` n `78` status `ready` deltaP `36.6053` edge `1.3169` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.1966` n `78` status `ready` deltaP `48.4642` edge `1.1213` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6322` n `78` status `ready` deltaP `61.4182` edge `0.3275` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.5384` n `78` status `ready` deltaP `38.4882` edge `0.3337` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9467` n `52` status `ready` deltaP `37.6736` edge `0.2444` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9467` n `52` status `ready` deltaP `37.6736` edge `0.2444` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6497` n `137` status `ready` deltaP `30.3743` edge `0.2375` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.6039` n `52` status `ready` deltaP `42.1741` edge `0.0234` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.6039` n `52` status `ready` deltaP `42.1741` edge `0.0234` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.2069` n `137` status `ready` deltaP `38.9877` edge `0.0289` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.8514` n `52` status `ready` deltaP `24.3082` edge `0.0272` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8514` n `52` status `ready` deltaP `24.3082` edge `0.0272` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7511` n `149` status `ready` deltaP `20.8105` edge `0.049` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8521` n `149` status `ready` deltaP `13.5163` edge `0.0186` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7232` n `78` status `ready` deltaP `17.5735` edge `0.0384` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2289` n `52` status `ready` deltaP `6.5984` edge `0.0103` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2289` n `52` status `ready` deltaP `6.5984` edge `0.0103` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

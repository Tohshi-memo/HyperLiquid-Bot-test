# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T13:22:33.329299+00:00`
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

- `news_risk_high->unknown_4h` score `396.4038` n `78` status `ready` deltaP `-22.6078` edge `33.2737` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `22.306` n `78` status `ready` deltaP `20.6597` edge `1.7211` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `22.2815` n `78` status `ready` deltaP `46.3809` edge `1.5867` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.2695` n `78` status `ready` deltaP `37.6469` edge `1.3352` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.1198` n `78` status `ready` deltaP `48.4642` edge `1.1149` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.493` n `78` status `ready` deltaP `60.203` edge `0.324` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4776` n `78` status `ready` deltaP `37.9674` edge `0.3321` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9659` n `52` status `ready` deltaP `37.6736` edge `0.246` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9659` n `52` status `ready` deltaP `37.6736` edge `0.246` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6689` n `137` status `ready` deltaP `30.3743` edge `0.2391` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.4671` n `52` status `ready` deltaP `40.9588` edge `0.0201` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.4671` n `52` status `ready` deltaP `40.9588` edge `0.0201` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.0701` n `137` status `ready` deltaP `37.7724` edge `0.0256` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.8094` n `52` status `ready` deltaP `24.3082` edge `0.0237` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8094` n `52` status `ready` deltaP `24.3082` edge `0.0237` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7091` n `149` status `ready` deltaP `20.8105` edge `0.0455` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8234` n `149` status `ready` deltaP `13.3666` edge `0.0172` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7131` n `78` status `ready` deltaP `17.5735` edge `0.0371` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2019` n `52` status `ready` deltaP `7.462` edge `0.0067` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2019` n `52` status `ready` deltaP `7.462` edge `0.0067` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

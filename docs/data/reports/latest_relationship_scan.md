# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T10:37:28.266826+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11908`

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

- `risk_on_high->crypto_alt_24h` score `16.4053` n `91` status `ready` deltaP `33.568` edge `1.1663` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.4053` n `91` status `ready` deltaP `33.568` edge `1.1663` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `11.8165` n `201` status `ready` deltaP `25.1322` edge `0.8999` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.8557` n `91` status `ready` deltaP `39.8117` edge `0.4264` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.8557` n `91` status `ready` deltaP `39.8117` edge `0.4264` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `6.0496` n `91` status `ready` deltaP `29.61` edge `0.3926` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.0496` n `91` status `ready` deltaP `29.61` edge `0.3926` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.4199` n `91` status `ready` deltaP `22.4169` edge `0.9522` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.4199` n `91` status `ready` deltaP `22.4169` edge `0.9522` maxDD `-24.5429`
- `risk_on_high->index_24h` score `3.2814` n `91` status `ready` deltaP `34.3769` edge `0.0485` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.2814` n `91` status `ready` deltaP `34.3769` edge `0.0485` maxDD `-0.0051`
- `market_context_high->equity_24h` score `3.0053` n `201` status `ready` deltaP `18.5764` edge `0.1266` maxDD `0.0`
- `market_context_high->index_24h` score `2.4096` n `201` status `ready` deltaP `28.7184` edge `0.0487` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.0152` n `91` status `ready` deltaP `26.4859` edge `0.0007` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.0152` n `91` status `ready` deltaP `26.4859` edge `0.0007` maxDD `-0.0802`
- `market_context_high->commodity_24h` score `1.8743` n `201` status `ready` deltaP `18.452` edge `0.0471` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.8581` n `91` status `ready` deltaP `18.1185` edge `0.0434` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.8581` n `91` status `ready` deltaP `18.1185` edge `0.0434` maxDD `-0.0811`
- `risk_on_high->equity_24h` score `1.3997` n `91` status `ready` deltaP `18.5764` edge `-0.0072` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.3997` n `91` status `ready` deltaP `18.5764` edge `-0.0072` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

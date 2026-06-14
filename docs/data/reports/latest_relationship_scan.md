# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T17:07:31.116398+00:00`
- Price records: `672`
- Market context records: `3912`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11374`

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

- `risk_on_high->unknown_4h` score `51.3457` n `68` status `ready` deltaP `5.8734` edge `6.7578` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `51.3457` n `68` status `ready` deltaP `5.8734` edge `6.7578` maxDD `-13.467`
- `risk_on_high->equity_24h` score `20.7191` n `40` status `ready` deltaP `42.0139` edge `1.4465` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `20.7191` n `40` status `ready` deltaP `42.0139` edge `1.4465` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `18.3426` n `40` status `ready` deltaP `7.7778` edge `1.6366` maxDD `-8.4585`
- `risk_on_and_context->crypto_major_24h` score `18.3426` n `40` status `ready` deltaP `7.7778` edge `1.6366` maxDD `-8.4585`
- `risk_on_high->index_24h` score `8.344` n `40` status `ready` deltaP `30.0347` edge `0.4951` maxDD `0.0`
- `risk_on_and_context->index_24h` score `8.344` n `40` status `ready` deltaP `30.0347` edge `0.4951` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.2894` n `204` status `ready` deltaP `-1.4795` edge `1.4853` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `7.0765` n `68` status `ready` deltaP `24.6951` edge `0.5115` maxDD `-4.2472`
- `risk_on_and_context->crypto_major_4h` score `7.0765` n `68` status `ready` deltaP `24.6951` edge `0.5115` maxDD `-4.2472`
- `market_context_high->equity_24h` score `5.8764` n `165` status `ready` deltaP `20.8018` edge `0.654` maxDD `-14.5715`
- `market_context_high->index_24h` score `4.4892` n `165` status `ready` deltaP `25.7923` edge `0.3161` maxDD `-7.1159`
- `risk_on_high->crypto_alt_24h` score `4.2876` n `40` status `ready` deltaP `5.6944` edge `0.7762` maxDD `-16.8239`
- `risk_on_and_context->crypto_alt_24h` score `4.2876` n `40` status `ready` deltaP `5.6944` edge `0.7762` maxDD `-16.8239`
- `risk_on_high->equity_4h` score `4.1743` n `68` status `ready` deltaP `29.8512` edge `0.212` maxDD `-3.0523`
- `risk_on_and_context->equity_4h` score `4.1743` n `68` status `ready` deltaP `29.8512` edge `0.212` maxDD `-3.0523`
- `market_context_high->crypto_major_4h` score `3.0853` n `204` status `ready` deltaP `18.3226` edge `0.3114` maxDD `-9.4488`
- `market_context_high->metal_24h` score `2.6517` n `165` status `ready` deltaP `18.0272` edge `0.2523` maxDD `-9.1203`
- `market_context_high->equity_4h` score `1.4673` n `204` status `ready` deltaP `15.1453` edge `0.1917` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T17:07:28.954382+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8954`

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

- `market_context_high->crypto_major_24h` score `18.6587` n `54` status `ready` deltaP `33.5648` edge `1.546` maxDD `-13.5229`
- `market_context_high->crypto_alt_24h` score `14.7904` n `54` status `ready` deltaP `21.5856` edge `1.4184` maxDD `-22.3814`
- `risk_on_high->crypto_alt_4h` score `4.1642` n `48` status `ready` deltaP `18.3435` edge `0.2695` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.1642` n `48` status `ready` deltaP `18.3435` edge `0.2695` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.6379` n `48` status `ready` deltaP `33.1301` edge `0.3308` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.6379` n `48` status `ready` deltaP `33.1301` edge `0.3308` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.4623` n `100` status `ready` deltaP `13.4268` edge `0.3439` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.2062` n `100` status `ready` deltaP `16.9634` edge `0.31` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.6017` n `100` status `ready` deltaP `12.2036` edge `0.1472` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.9802` n `48` status `ready` deltaP `6.5369` edge `0.0978` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9802` n `48` status `ready` deltaP `6.5369` edge `0.0978` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.662` n `100` status `ready` deltaP `4.3473` edge `0.1025` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4186` n `48` status `ready` deltaP `5.514` edge `0.0822` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4186` n `48` status `ready` deltaP `5.514` edge `0.0822` maxDD `-3.2233`
- `market_context_high->unknown_4h` score `0.1595` n `100` status `ready` deltaP `-3.9268` edge `0.1041` maxDD `-1.8373`
- `market_context_high->metal_24h` score `0.029` n `54` status `ready` deltaP `8.8542` edge `0.0425` maxDD `-2.1579`
- `market_context_high->index_1h` score `-0.0242` n `100` status `ready` deltaP `4.0` edge `0.0033` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1201` n `100` status `ready` deltaP `6.2515` edge `0.0044` maxDD `-0.4868`
- `risk_on_high->metal_1h` score `-0.3028` n `48` status `ready` deltaP `3.4182` edge `0.0039` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3028` n `48` status `ready` deltaP `3.4182` edge `0.0039` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

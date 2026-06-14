# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T17:53:05.669367+00:00`
- Price records: `672`
- Market context records: `3915`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11427`

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

- `risk_on_high->unknown_4h` score `54.4679` n `65` status `ready` deltaP `6.9653` edge `7.1508` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `54.4679` n `65` status `ready` deltaP `6.9653` edge `7.1508` maxDD `-13.467`
- `risk_on_high->equity_24h` score `19.4711` n `40` status `ready` deltaP `42.0139` edge `1.3425` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `19.4711` n `40` status `ready` deltaP `42.0139` edge `1.3425` maxDD `0.0`
- `market_context_high->unknown_4h` score `11.7993` n `201` status `ready` deltaP `-1.3394` edge `1.5331` maxDD `-35.6052`
- `risk_on_high->crypto_major_24h` score `9.7445` n `40` status `ready` deltaP `0.7986` edge `1.4331` maxDD `-9.7965`
- `risk_on_and_context->crypto_major_24h` score `9.7445` n `40` status `ready` deltaP `0.7986` edge `1.4331` maxDD `-9.7965`
- `risk_on_high->crypto_major_4h` score `8.3791` n `65` status `ready` deltaP `28.1566` edge `0.5771` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `8.3791` n `65` status `ready` deltaP `28.1566` edge `0.5771` maxDD `-2.6576`
- `risk_on_high->index_24h` score `7.8124` n `40` status `ready` deltaP `30.0347` edge `0.4508` maxDD `0.0`
- `risk_on_and_context->index_24h` score `7.8124` n `40` status `ready` deltaP `30.0347` edge `0.4508` maxDD `0.0`
- `market_context_high->equity_24h` score `5.6448` n `165` status `ready` deltaP `20.8018` edge `0.6347` maxDD `-14.5715`
- `risk_on_high->equity_4h` score `5.4227` n `65` status `ready` deltaP `33.9236` edge `0.2523` maxDD `-1.1253`
- `risk_on_and_context->equity_4h` score `5.4227` n `65` status `ready` deltaP `33.9236` edge `0.2523` maxDD `-1.1253`
- `market_context_high->index_24h` score `4.3896` n `165` status `ready` deltaP `25.7923` edge `0.3078` maxDD `-7.1159`
- `market_context_high->crypto_major_4h` score `3.3688` n `201` status `ready` deltaP `19.3468` edge `0.3282` maxDD `-9.4488`
- `market_context_high->metal_24h` score `2.6027` n `165` status `ready` deltaP `17.5947` edge `0.2511` maxDD `-9.1203`
- `risk_on_high->crypto_alt_4h` score `2.0716` n `65` status `ready` deltaP `1.7261` edge `0.243` maxDD `-3.8835`
- `risk_on_and_context->crypto_alt_4h` score `2.0716` n `65` status `ready` deltaP `1.7261` edge `0.243` maxDD `-3.8835`
- `risk_on_high->crypto_alt_24h` score `1.6899` n `40` status `ready` deltaP `-1.2847` edge `0.5571` maxDD `-21.2171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

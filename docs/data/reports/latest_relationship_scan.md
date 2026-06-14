# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T19:07:26.792062+00:00`
- Price records: `672`
- Market context records: `3920`
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

- `risk_on_high->unknown_4h` score `60.0965` n `60` status `ready` deltaP `6.0366` edge `7.8786` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `60.0965` n `60` status `ready` deltaP `6.0366` edge `7.8786` maxDD `-13.467`
- `risk_on_high->equity_24h` score `16.8923` n `39` status `ready` deltaP `42.0139` edge `1.1276` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `16.8923` n `39` status `ready` deltaP `42.0139` edge `1.1276` maxDD `0.0`
- `market_context_high->unknown_4h` score `12.7834` n `196` status `ready` deltaP `-1.4124` edge `1.6156` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `8.6956` n `60` status `ready` deltaP `29.8476` edge `0.5922` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `8.6956` n `60` status `ready` deltaP `29.8476` edge `0.5922` maxDD `-2.6576`
- `risk_on_high->index_24h` score `6.7024` n `39` status `ready` deltaP `30.0347` edge `0.3583` maxDD `0.0`
- `risk_on_and_context->index_24h` score `6.7024` n `39` status `ready` deltaP `30.0347` edge `0.3583` maxDD `0.0`
- `risk_on_high->equity_4h` score `6.5109` n `60` status `ready` deltaP `38.2826` edge `0.2921` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `6.5109` n `60` status `ready` deltaP `38.2826` edge `0.2921` maxDD `-0.0458`
- `risk_on_high->crypto_major_24h` score `5.8711` n `39` status `ready` deltaP `-9.6154` edge `1.0539` maxDD `-12.3012`
- `risk_on_and_context->crypto_major_24h` score `5.8711` n `39` status `ready` deltaP `-9.6154` edge `1.0539` maxDD `-12.3012`
- `market_context_high->equity_24h` score `5.1012` n `165` status `ready` deltaP `20.8018` edge `0.5894` maxDD `-14.5715`
- `market_context_high->index_24h` score `4.164` n `165` status `ready` deltaP `25.7923` edge `0.289` maxDD `-7.1159`
- `market_context_high->crypto_major_4h` score `3.4259` n `196` status `ready` deltaP `19.7456` edge `0.3303` maxDD `-9.4488`
- `risk_on_high->crypto_major_1h` score `2.8341` n `60` status `ready` deltaP `13.1836` edge `0.2025` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `2.8341` n `60` status `ready` deltaP `13.1836` edge `0.2025` maxDD `-2.3372`
- `market_context_high->metal_24h` score `2.5943` n `165` status `ready` deltaP `17.5947` edge `0.2504` maxDD `-9.1203`
- `risk_on_high->crypto_alt_4h` score `2.1802` n `60` status `ready` deltaP `1.4939` edge `0.2536` maxDD `-3.8835`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

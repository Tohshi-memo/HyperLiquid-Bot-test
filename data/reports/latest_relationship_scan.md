# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T06:07:27.434282+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9576`

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

- `market_context_high->unknown_4h` score `33.7515` n `119` status `ready` deltaP `-6.3781` edge `2.9257` maxDD `-2.3109`
- `market_context_high->crypto_major_24h` score `8.8561` n `54` status `ready` deltaP `17.1875` edge `1.2844` maxDD `-13.7531`
- `market_context_high->equity_24h` score `7.6602` n `54` status `ready` deltaP `23.4375` edge `0.5665` maxDD `-3.0855`
- `risk_on_high->crypto_major_4h` score `6.1953` n `50` status `ready` deltaP `34.8963` edge `0.3689` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.1953` n `50` status `ready` deltaP `34.8963` edge `0.3689` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `5.4841` n `50` status `ready` deltaP `22.5122` edge `0.3517` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.4841` n `50` status `ready` deltaP `22.5122` edge `0.3517` maxDD `-1.9151`
- `market_context_high->index_24h` score `4.9728` n `54` status `ready` deltaP `42.3611` edge `0.1497` maxDD `-0.083`
- `market_context_high->crypto_alt_24h` score `3.953` n `54` status `ready` deltaP `-4.5139` edge `0.9765` maxDD `-25.169`
- `risk_on_high->metal_4h` score `1.7897` n `50` status `ready` deltaP `18.4756` edge `0.067` maxDD `-0.6154`
- `risk_on_and_context->metal_4h` score `1.7897` n `50` status `ready` deltaP `18.4756` edge `0.067` maxDD `-0.6154`
- `risk_on_high->crypto_alt_1h` score `1.6614` n `60` status `ready` deltaP `9.1417` edge `0.1372` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.6614` n `60` status `ready` deltaP `9.1417` edge `0.1372` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.3642` n `60` status `ready` deltaP `9.4012` edge `0.1163` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.3642` n `60` status `ready` deltaP `9.4012` edge `0.1163` maxDD `-3.2233`
- `market_context_high->crypto_major_4h` score `0.9841` n `119` status `ready` deltaP `11.7198` edge `0.2586` maxDD `-11.1784`
- `market_context_high->crypto_alt_1h` score `0.9549` n `129` status `ready` deltaP `7.8239` edge `0.1225` maxDD `-4.9401`
- `market_context_high->crypto_alt_4h` score `0.7344` n `119` status `ready` deltaP `5.8567` edge `0.278` maxDD `-13.8008`
- `market_context_high->crypto_major_1h` score `0.5458` n `129` status `ready` deltaP `4.44` edge `0.0922` maxDD `-3.4384`
- `market_context_high->metal_4h` score `0.3095` n `119` status `ready` deltaP `10.6605` edge `0.027` maxDD `-1.1153`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

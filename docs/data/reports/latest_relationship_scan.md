# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T08:52:44.441009+00:00`
- Price records: `672`
- Market context records: `3367`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13080`

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

- `risk_on_high->crypto_major_24h` score `56.8036` n `32` status `ready` deltaP `59.8958` edge `4.3386` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.8036` n `32` status `ready` deltaP `59.8958` edge `4.3386` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.6124` n `32` status `ready` deltaP `54.8611` edge `4.1171` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.6124` n `32` status `ready` deltaP `54.8611` edge `4.1171` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.9873` n `32` status `ready` deltaP `56.7708` edge `3.4538` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.9873` n `32` status `ready` deltaP `56.7708` edge `3.4538` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1698` n `32` status `ready` deltaP `50.8681` edge `1.5917` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1698` n `32` status `ready` deltaP `50.8681` edge `1.5917` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `15.3846` n `32` status `ready` deltaP `27.8963` edge `1.2083` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.3846` n `32` status `ready` deltaP `27.8963` edge `1.2083` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `15.0194` n `32` status `ready` deltaP `32.8125` edge `1.059` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.0194` n `32` status `ready` deltaP `32.8125` edge `1.059` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `13.5117` n `158` status `ready` deltaP `18.1127` edge `2.4828` maxDD `-62.7028`
- `market_context_high->index_24h` score `11.9449` n `158` status `ready` deltaP `35.6782` edge `1.013` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.6591` n `158` status `ready` deltaP `30.8214` edge `2.0027` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.2932` n `32` status `ready` deltaP `8.3079` edge `0.7368` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.2932` n `32` status `ready` deltaP `8.3079` edge `0.7368` maxDD `-11.7537`
- `market_context_high->crypto_major_24h` score `3.935` n `158` status `ready` deltaP `21.2486` edge `2.1027` maxDD `-128.1895`
- `risk_on_high->equity_4h` score `3.5479` n `32` status `ready` deltaP `14.1006` edge `0.4743` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5479` n `32` status `ready` deltaP `14.1006` edge `0.4743` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

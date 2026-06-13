# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T01:33:35.023380+00:00`
- Price records: `672`
- Market context records: `3742`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13153`

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

- `risk_on_high->crypto_major_24h` score `28.588` n `32` status `ready` deltaP `29.3403` edge `2.191` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.588` n `32` status `ready` deltaP `29.3403` edge `2.191` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.3042` n `32` status `ready` deltaP `33.5069` edge `1.6353` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.3042` n `32` status `ready` deltaP `33.5069` edge `1.6353` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.1064` n `32` status `ready` deltaP `30.5556` edge `1.5703` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.1064` n `32` status `ready` deltaP `30.5556` edge `1.5703` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4244` n `32` status `ready` deltaP `31.25` edge `0.7437` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4244` n `32` status `ready` deltaP `31.25` edge `0.7437` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.0803` n `32` status `ready` deltaP `18.2927` edge `0.8303` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.0803` n `32` status `ready` deltaP `18.2927` edge `0.8303` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.222` n `158` status `ready` deltaP `17.6841` edge `0.64` maxDD `-12.8184`
- `market_context_high->index_24h` score `5.4318` n `158` status `ready` deltaP `26.8196` edge `0.3878` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.5963` n `158` status `ready` deltaP `27.4789` edge `0.343` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.5311` n `158` status `ready` deltaP `7.1488` edge `0.7763` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.819` n `168` status `ready` deltaP `9.0665` edge `0.2812` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3919` n `32` status `ready` deltaP `14.5833` edge `0.0449` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3919` n `32` status `ready` deltaP `14.5833` edge `0.0449` maxDD `-0.7574`
- `risk_on_high->crypto_alt_4h` score `1.3283` n `32` status `ready` deltaP `-0.8384` edge `0.3007` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.3283` n `32` status `ready` deltaP `-0.8384` edge `0.3007` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `1.2084` n `32` status `ready` deltaP `7.2409` edge `0.2201` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T18:37:29.128993+00:00`
- Price records: `672`
- Market context records: `3816`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13781`

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

- `risk_on_high->crypto_major_24h` score `31.9683` n `32` status `ready` deltaP `33.8542` edge `2.4426` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.9683` n `32` status `ready` deltaP `33.8542` edge `2.4426` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.0543` n `32` status `ready` deltaP `42.0139` edge `1.8911` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.0543` n `32` status `ready` deltaP `42.0139` edge `1.8911` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5575` n `32` status `ready` deltaP `31.9444` edge `1.7653` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5575` n `32` status `ready` deltaP `31.9444` edge `1.7653` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3908` n `32` status `ready` deltaP `31.25` edge `0.7409` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3908` n `32` status `ready` deltaP `31.25` edge `0.7409` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `8.1875` n `34` status `ready` deltaP `10.7425` edge `0.7229` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `8.1875` n `34` status `ready` deltaP `10.7425` edge `0.7229` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.7429` n `152` status `ready` deltaP `18.9876` edge `0.7383` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.3446` n `152` status `ready` deltaP `26.6447` edge `0.3817` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `5.2359` n `152` status `ready` deltaP `6.0581` edge `0.8423` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.3408` n `152` status `ready` deltaP `26.5808` edge `0.3277` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.2953` n `191` status `ready` deltaP `12.0052` edge `0.3013` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4959` n `34` status `ready` deltaP `10.0251` edge `0.2384` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4959` n `34` status `ready` deltaP `10.0251` edge `0.2384` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.3972` n `32` status `ready` deltaP `14.4097` edge `0.0465` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3972` n `32` status `ready` deltaP `14.4097` edge `0.0465` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.1603` n `191` status `ready` deltaP `11.4879` edge `0.1905` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T18:52:34.846135+00:00`
- Price records: `672`
- Market context records: `3817`
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

- `risk_on_high->crypto_major_24h` score `32.0626` n `32` status `ready` deltaP `34.0278` edge `2.4493` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.0626` n `32` status `ready` deltaP `34.0278` edge `2.4493` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.0915` n `32` status `ready` deltaP `42.0139` edge `1.8942` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.0915` n `32` status `ready` deltaP `42.0139` edge `1.8942` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5815` n `32` status `ready` deltaP `31.9444` edge `1.7673` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5815` n `32` status `ready` deltaP `31.9444` edge `1.7673` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3884` n `32` status `ready` deltaP `31.25` edge `0.7407` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3884` n `32` status `ready` deltaP `31.25` edge `0.7407` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.604` n `35` status `ready` deltaP `8.8937` edge `0.6866` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `7.604` n `35` status `ready` deltaP `8.8937` edge `0.6866` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.7127` n `151` status `ready` deltaP `18.8351` edge `0.7368` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.3662` n `151` status `ready` deltaP `26.6142` edge `0.3837` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `5.1206` n `151` status `ready` deltaP `6.027` edge `0.8329` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.3199` n `151` status `ready` deltaP `26.4544` edge `0.3268` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.2905` n `191` status `ready` deltaP `12.0052` edge `0.3009` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4824` n `35` status `ready` deltaP `10.9494` edge `0.2305` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4824` n `35` status `ready` deltaP `10.9494` edge `0.2305` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.4044` n `32` status `ready` deltaP `14.4097` edge `0.0471` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4044` n `32` status `ready` deltaP `14.4097` edge `0.0471` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.1543` n `191` status `ready` deltaP `11.4879` edge `0.19` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

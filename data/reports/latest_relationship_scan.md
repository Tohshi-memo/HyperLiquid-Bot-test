# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T21:22:27.711529+00:00`
- Price records: `672`
- Market context records: `3828`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13802`

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

- `risk_on_high->crypto_major_24h` score `32.599` n `32` status `ready` deltaP `34.0278` edge `2.494` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.599` n `32` status `ready` deltaP `34.0278` edge `2.494` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.2511` n `32` status `ready` deltaP `42.0139` edge `1.9075` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.2511` n `32` status `ready` deltaP `42.0139` edge `1.9075` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5659` n `32` status `ready` deltaP `31.9444` edge `1.766` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5659` n `32` status `ready` deltaP `31.9444` edge `1.766` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3212` n `32` status `ready` deltaP `31.25` edge `0.7351` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3212` n `32` status `ready` deltaP `31.25` edge `0.7351` maxDD `0.0`
- `market_context_high->equity_24h` score `6.6904` n `141` status `ready` deltaP `17.1912` edge `0.7459` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.6195` n `141` status `ready` deltaP `26.2855` edge `0.407` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.0124` n `45` status `ready` deltaP `6.7988` edge `0.4846` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.0124` n `45` status `ready` deltaP `6.7988` edge `0.4846` maxDD `-5.9781`
- `market_context_high->metal_24h` score `4.2169` n `141` status `ready` deltaP `25.0923` edge `0.3273` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.0632` n `141` status `ready` deltaP `3.8195` edge `0.7595` maxDD `-31.0425`
- `risk_on_high->equity_4h` score `2.3581` n `45` status `ready` deltaP `17.9336` edge `0.1904` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.3581` n `45` status `ready` deltaP `17.9336` edge `0.1904` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `1.8577` n `191` status `ready` deltaP `10.1496` edge `0.2772` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.4236` n `32` status `ready` deltaP `14.4097` edge `0.0487` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4236` n `32` status `ready` deltaP `14.4097` edge `0.0487` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.0787` n `191` status `ready` deltaP `11.4879` edge `0.1837` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

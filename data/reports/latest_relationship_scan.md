# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T00:52:33.047346+00:00`
- Price records: `672`
- Market context records: `3843`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13787`

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

- `risk_on_high->crypto_major_24h` score `33.4846` n `32` status `ready` deltaP `34.0278` edge `2.5678` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.4846` n `32` status `ready` deltaP `34.0278` edge `2.5678` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.5775` n `32` status `ready` deltaP `42.0139` edge `1.9347` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.5775` n `32` status `ready` deltaP `42.0139` edge `1.9347` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.6919` n `32` status `ready` deltaP `31.9444` edge `1.7765` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.6919` n `32` status `ready` deltaP `31.9444` edge `1.7765` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2744` n `32` status `ready` deltaP `31.25` edge `0.7312` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2744` n `32` status `ready` deltaP `31.25` edge `0.7312` maxDD `0.0`
- `market_context_high->unknown_24h` score `9.8836` n `128` status `ready` deltaP `-18.4028` edge `4.238` maxDD `-200.1879`
- `market_context_high->equity_24h` score `6.4491` n `128` status `ready` deltaP `14.6701` edge `0.7426` maxDD `-14.5715`
- `market_context_high->index_24h` score `6.0483` n `128` status `ready` deltaP `25.7812` edge `0.4461` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.6792` n `58` status `ready` deltaP `15.7643` edge `0.4804` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.6792` n `58` status `ready` deltaP `15.7643` edge `0.4804` maxDD `-5.9781`
- `market_context_high->metal_24h` score `3.9574` n `128` status `ready` deltaP `23.0035` edge `0.3196` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6164` n `58` status `ready` deltaP `23.4125` edge `0.1754` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6164` n `58` status `ready` deltaP `23.4125` edge `0.1754` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.4512` n `32` status `ready` deltaP `14.4097` edge `0.051` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4512` n `32` status `ready` deltaP `14.4097` edge `0.051` maxDD `-0.7574`
- `market_context_high->crypto_major_4h` score `1.2117` n `192` status `ready` deltaP `10.3405` edge `0.2221` maxDD `-10.5381`
- `market_context_high->crypto_major_24h` score `0.8943` n `128` status `ready` deltaP `0.434` edge `0.518` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

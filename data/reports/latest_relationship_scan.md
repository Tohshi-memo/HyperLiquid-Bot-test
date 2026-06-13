# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T21:07:29.438536+00:00`
- Price records: `672`
- Market context records: `3827`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13799`

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

- `risk_on_high->crypto_major_24h` score `32.5498` n `32` status `ready` deltaP `34.0278` edge `2.4899` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.5498` n `32` status `ready` deltaP `34.0278` edge `2.4899` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.2379` n `32` status `ready` deltaP `42.0139` edge `1.9064` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.2379` n `32` status `ready` deltaP `42.0139` edge `1.9064` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5623` n `32` status `ready` deltaP `31.9444` edge `1.7657` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5623` n `32` status `ready` deltaP `31.9444` edge `1.7657` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3284` n `32` status `ready` deltaP `31.25` edge `0.7357` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3284` n `32` status `ready` deltaP `31.25` edge `0.7357` maxDD `0.0`
- `market_context_high->equity_24h` score `6.69` n `142` status `ready` deltaP `17.366` edge `0.7447` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.5934` n `142` status `ready` deltaP `26.3204` edge `0.4046` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.0381` n `44` status `ready` deltaP `5.8897` edge `0.4928` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.0381` n `44` status `ready` deltaP `5.8897` edge `0.4928` maxDD `-5.9781`
- `market_context_high->metal_24h` score `4.2249` n `142` status `ready` deltaP `25.2372` edge `0.327` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.1732` n `142` status `ready` deltaP `4.0542` edge `0.7671` maxDD `-31.0425`
- `risk_on_high->equity_4h` score `2.3148` n `44` status `ready` deltaP `17.378` edge `0.1905` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.3148` n `44` status `ready` deltaP `17.378` edge `0.1905` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `1.8877` n `191` status `ready` deltaP `10.1496` edge `0.2797` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.4224` n `32` status `ready` deltaP `14.4097` edge `0.0486` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4224` n `32` status `ready` deltaP `14.4097` edge `0.0486` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.0835` n `191` status `ready` deltaP `11.4879` edge `0.1841` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

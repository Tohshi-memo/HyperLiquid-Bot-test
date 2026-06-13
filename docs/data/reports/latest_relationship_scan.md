# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T17:52:29.098600+00:00`
- Price records: `672`
- Market context records: `3813`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13498`

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

- `risk_on_high->crypto_major_24h` score `31.7271` n `32` status `ready` deltaP `33.8542` edge `2.4225` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.7271` n `32` status `ready` deltaP `33.8542` edge `2.4225` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `25.9415` n `32` status `ready` deltaP `42.0139` edge `1.8817` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.9415` n `32` status `ready` deltaP `42.0139` edge `1.8817` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.4735` n `32` status `ready` deltaP `31.9444` edge `1.7583` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.4735` n `32` status `ready` deltaP `31.9444` edge `1.7583` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.398` n `32` status `ready` deltaP `31.25` edge `0.7415` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.398` n `32` status `ready` deltaP `31.25` edge `0.7415` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.2882` n `32` status `ready` deltaP `14.4817` edge `0.7897` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.2882` n `32` status `ready` deltaP `14.4817` edge `0.7897` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.7776` n `154` status `ready` deltaP `19.2866` edge `0.7392` maxDD `-14.5715`
- `market_context_high->crypto_major_24h` score `5.4444` n `154` status `ready` deltaP `6.4597` edge `0.857` maxDD `-31.0425`
- `market_context_high->index_24h` score `5.311` n `154` status `ready` deltaP `26.7045` edge `0.3785` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.3623` n `154` status `ready` deltaP `26.6549` edge `0.329` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.3888` n `190` status `ready` deltaP `12.5738` edge `0.3053` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.475` n `32` status `ready` deltaP `8.003` edge `0.2492` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.475` n `32` status `ready` deltaP `8.003` edge `0.2492` maxDD `-5.7426`
- `risk_on_high->commodity_4h` score `1.4645` n `32` status `ready` deltaP `17.4543` edge `0.0924` maxDD `-3.6044`
- `risk_on_and_context->commodity_4h` score `1.4645` n `32` status `ready` deltaP `17.4543` edge `0.0924` maxDD `-3.6044`
- `risk_on_high->metal_24h` score `1.3545` n `32` status `ready` deltaP `14.2361` edge `0.0441` maxDD `-0.7574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

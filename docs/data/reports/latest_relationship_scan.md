# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T23:22:29.921471+00:00`
- Price records: `672`
- Market context records: `3837`
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

- `risk_on_high->crypto_major_24h` score `33.0466` n `32` status `ready` deltaP `34.0278` edge `2.5313` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.0466` n `32` status `ready` deltaP `34.0278` edge `2.5313` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.4071` n `32` status `ready` deltaP `42.0139` edge `1.9205` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.4071` n `32` status `ready` deltaP `42.0139` edge `1.9205` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5827` n `32` status `ready` deltaP `31.9444` edge `1.7674` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5827` n `32` status `ready` deltaP `31.9444` edge `1.7674` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2648` n `32` status `ready` deltaP `31.25` edge `0.7304` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2648` n `32` status `ready` deltaP `31.25` edge `0.7304` maxDD `0.0`
- `market_context_high->equity_24h` score `6.5337` n `133` status `ready` deltaP `15.6981` edge `0.7428` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.8824` n `133` status `ready` deltaP `25.9868` edge `0.4309` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.5116` n `52` status `ready` deltaP `12.1834` edge `0.4903` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.5116` n `52` status `ready` deltaP `12.1834` edge `0.4903` maxDD `-5.9781`
- `market_context_high->metal_24h` score `4.112` n `133` status `ready` deltaP `23.8552` edge `0.3268` maxDD `-9.1203`
- `market_context_high->unknown_24h` score `3.6822` n `133` status `ready` deltaP `-18.5359` edge `3.7512` maxDD `-223.1103`
- `risk_on_high->equity_4h` score `2.6417` n `52` status `ready` deltaP `21.2242` edge `0.1921` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6417` n `52` status `ready` deltaP `21.2242` edge `0.1921` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.356` n `133` status `ready` deltaP `1.8145` edge `0.6306` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.4557` n `191` status `ready` deltaP `10.1496` edge `0.2437` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3936` n `32` status `ready` deltaP `14.4097` edge `0.0462` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3936` n `32` status `ready` deltaP `14.4097` edge `0.0462` maxDD `-0.7574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

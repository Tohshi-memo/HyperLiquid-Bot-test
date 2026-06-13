# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T15:52:27.848148+00:00`
- Price records: `672`
- Market context records: `3805`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13344`

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

- `risk_on_high->crypto_major_24h` score `31.1002` n `32` status `ready` deltaP `32.8125` edge `2.3772` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.1002` n `32` status `ready` deltaP `32.8125` edge `2.3772` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `25.5445` n `32` status `ready` deltaP `41.1458` edge `1.8544` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.5445` n `32` status `ready` deltaP `41.1458` edge `1.8544` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.2611` n `32` status `ready` deltaP `31.9444` edge `1.7406` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.2611` n `32` status `ready` deltaP `31.9444` edge `1.7406` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4256` n `32` status `ready` deltaP `31.25` edge `0.7438` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4256` n `32` status `ready` deltaP `31.25` edge `0.7438` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.3736` n `32` status `ready` deltaP `14.6341` edge `0.7958` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.3736` n `32` status `ready` deltaP `14.6341` edge `0.7958` maxDD `-5.9781`
- `market_context_high->equity_24h` score `7.3292` n `150` status `ready` deltaP `20.4791` edge `0.749` maxDD `-13.6477`
- `market_context_high->crypto_major_24h` score `5.4997` n `150` status `ready` deltaP `7.2708` edge `0.8562` maxDD `-31.0425`
- `market_context_high->index_24h` score `5.3877` n `150` status `ready` deltaP `26.5833` edge `0.3857` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.2742` n `150` status `ready` deltaP `26.1528` edge `0.325` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.8306` n `182` status `ready` deltaP `14.016` edge `0.3325` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4411` n `32` status `ready` deltaP `7.5457` edge `0.2479` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4411` n `32` status `ready` deltaP `7.5457` edge `0.2479` maxDD `-5.7426`
- `risk_on_high->commodity_4h` score `1.3783` n `32` status `ready` deltaP `16.6921` edge `0.0903` maxDD `-3.6044`
- `risk_on_and_context->commodity_4h` score `1.3783` n `32` status `ready` deltaP `16.6921` edge `0.0903` maxDD `-3.6044`
- `risk_on_high->metal_24h` score `1.3221` n `32` status `ready` deltaP `14.2361` edge `0.0414` maxDD `-0.7574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

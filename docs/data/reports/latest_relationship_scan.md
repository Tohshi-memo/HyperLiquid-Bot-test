# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T13:07:32.724370+00:00`
- Price records: `672`
- Market context records: `3792`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13048`

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

- `risk_on_high->crypto_major_24h` score `30.6901` n `32` status `ready` deltaP `32.2917` edge `2.3465` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.6901` n `32` status `ready` deltaP `32.2917` edge `2.3465` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `25.1493` n `32` status `ready` deltaP `40.4514` edge `1.8261` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.1493` n `32` status `ready` deltaP `40.4514` edge `1.8261` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.1471` n `32` status `ready` deltaP `31.9444` edge `1.7311` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.1471` n `32` status `ready` deltaP `31.9444` edge `1.7311` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5228` n `32` status `ready` deltaP `31.25` edge `0.7519` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5228` n `32` status `ready` deltaP `31.25` edge `0.7519` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.8654` n `32` status `ready` deltaP `16.311` edge `0.8256` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.8654` n `32` status `ready` deltaP `16.311` edge `0.8256` maxDD `-5.9781`
- `market_context_high->equity_24h` score `7.1812` n `156` status `ready` deltaP `20.5796` edge `0.736` maxDD `-13.6477`
- `market_context_high->crypto_major_24h` score `5.4514` n `156` status `ready` deltaP `7.8526` edge `0.8483` maxDD `-31.0425`
- `market_context_high->index_24h` score `5.3732` n `156` status `ready` deltaP `26.7628` edge `0.3833` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.4957` n `156` status `ready` deltaP `26.8964` edge `0.3385` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.1103` n `177` status `ready` deltaP `11.4028` edge `0.2899` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.5451` n `32` status `ready` deltaP `8.7652` edge `0.2531` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5451` n `32` status `ready` deltaP `8.7652` edge `0.2531` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.4097` n `32` status `ready` deltaP `14.2361` edge `0.0487` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4097` n `32` status `ready` deltaP `14.2361` edge `0.0487` maxDD `-0.7574`
- `risk_on_high->commodity_4h` score `1.1772` n `32` status `ready` deltaP `15.1677` edge `0.0837` maxDD `-3.6044`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

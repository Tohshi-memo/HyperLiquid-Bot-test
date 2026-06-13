# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T10:37:27.257487+00:00`
- Price records: `672`
- Market context records: `3781`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13040`

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

- `risk_on_high->crypto_major_24h` score `30.1902` n `32` status `ready` deltaP `32.1181` edge `2.306` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.1902` n `32` status `ready` deltaP `32.1181` edge `2.306` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.5239` n `32` status `ready` deltaP `38.8889` edge `1.7844` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.5239` n `32` status `ready` deltaP `38.8889` edge `1.7844` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.7859` n `32` status `ready` deltaP `31.9444` edge `1.701` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.7859` n `32` status `ready` deltaP `31.9444` edge `1.701` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5444` n `32` status `ready` deltaP `31.25` edge `0.7537` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5444` n `32` status `ready` deltaP `31.25` edge `0.7537` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.0337` n `32` status `ready` deltaP `17.5305` edge `0.8315` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.0337` n `32` status `ready` deltaP `17.5305` edge `0.8315` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.5743` n `157` status `ready` deltaP `19.1437` edge `0.695` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.3743` n `157` status `ready` deltaP `26.7914` edge `0.3832` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `4.9416` n `157` status `ready` deltaP `7.8546` edge `0.8058` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.5123` n `157` status `ready` deltaP `27.0148` edge `0.3391` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `1.9789` n `168` status `ready` deltaP `10.09` edge `0.2877` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4563` n `32` status `ready` deltaP `8.003` edge `0.2468` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4563` n `32` status `ready` deltaP `8.003` edge `0.2468` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.4169` n `32` status `ready` deltaP `14.2361` edge `0.0493` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4169` n `32` status `ready` deltaP `14.2361` edge `0.0493` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.1757` n `168` status `ready` deltaP `9.6399` edge `0.2041` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

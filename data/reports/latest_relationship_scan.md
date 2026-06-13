# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T11:07:31.066019+00:00`
- Price records: `672`
- Market context records: `3783`
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

- `risk_on_high->crypto_major_24h` score `30.3553` n `32` status `ready` deltaP `32.2917` edge `2.3186` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.3553` n `32` status `ready` deltaP `32.2917` edge `2.3186` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.6705` n `32` status `ready` deltaP `39.2361` edge `1.7943` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.6705` n `32` status `ready` deltaP `39.2361` edge `1.7943` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.9191` n `32` status `ready` deltaP `31.9444` edge `1.7121` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.9191` n `32` status `ready` deltaP `31.9444` edge `1.7121` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.548` n `32` status `ready` deltaP `31.25` edge `0.754` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.548` n `32` status `ready` deltaP `31.25` edge `0.754` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.0769` n `32` status `ready` deltaP `17.5305` edge `0.8351` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.0769` n `32` status `ready` deltaP `17.5305` edge `0.8351` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.7209` n `157` status `ready` deltaP `19.4909` edge `0.7049` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.3779` n `157` status `ready` deltaP `26.7914` edge `0.3835` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `5.1067` n `157` status `ready` deltaP `8.0282` edge `0.8184` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.5219` n `157` status `ready` deltaP `27.0148` edge `0.3399` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.0465` n `170` status `ready` deltaP `10.5452` edge `0.2903` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4789` n `32` status `ready` deltaP `8.003` edge `0.2497` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4789` n `32` status `ready` deltaP `8.003` edge `0.2497` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.4265` n `32` status `ready` deltaP `14.2361` edge `0.0501` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4265` n `32` status `ready` deltaP `14.2361` edge `0.0501` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.2125` n `170` status `ready` deltaP `10.0251` edge `0.2046` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

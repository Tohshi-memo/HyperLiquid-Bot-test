# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T03:07:28.501997+00:00`
- Price records: `672`
- Market context records: `3852`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13683`

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

- `risk_on_high->unknown_4h` score `54.4047` n `67` status `ready` deltaP `12.2293` edge `7.1076` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `54.4047` n `67` status `ready` deltaP `12.2293` edge `7.1076` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `33.949` n `32` status `ready` deltaP `34.0278` edge `2.6065` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.949` n `32` status `ready` deltaP `34.0278` edge `2.6065` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8019` n `32` status `ready` deltaP `42.0139` edge `1.9534` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8019` n `32` status `ready` deltaP `42.0139` edge `1.9534` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.6823` n `32` status `ready` deltaP `31.9444` edge `1.7757` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.6823` n `32` status `ready` deltaP `31.9444` edge `1.7757` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2984` n `32` status `ready` deltaP `31.25` edge `0.7332` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2984` n `32` status `ready` deltaP `31.25` edge `0.7332` maxDD `0.0`
- `market_context_high->unknown_24h` score `9.0946` n `128` status `ready` deltaP `-19.7917` edge `4.1461` maxDD `-200.1879`
- `market_context_high->unknown_4h` score `9.0399` n `201` status `ready` deltaP `1.284` edge `1.6913` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.6735` n `128` status `ready` deltaP `14.6701` edge `0.7613` maxDD `-14.5715`
- `market_context_high->index_24h` score `6.0723` n `128` status `ready` deltaP `25.7812` edge `0.4481` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.4879` n `67` status `ready` deltaP `18.593` edge `0.4456` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.4879` n `67` status `ready` deltaP `18.593` edge `0.4456` maxDD `-5.9781`
- `market_context_high->metal_24h` score `3.8568` n `128` status `ready` deltaP `22.1355` edge `0.317` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.5318` n `67` status `ready` deltaP `24.6201` edge `0.1603` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5318` n `67` status `ready` deltaP `24.6201` edge `0.1603` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `1.4323` n `201` status `ready` deltaP `11.6278` edge `0.2319` maxDD `-10.5381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

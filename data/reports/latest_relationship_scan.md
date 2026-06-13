# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T23:52:29.118461+00:00`
- Price records: `672`
- Market context records: `3839`
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

- `risk_on_high->crypto_major_24h` score `33.1834` n `32` status `ready` deltaP `34.0278` edge `2.5427` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.1834` n `32` status `ready` deltaP `34.0278` edge `2.5427` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.4455` n `32` status `ready` deltaP `42.0139` edge `1.9237` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.4455` n `32` status `ready` deltaP `42.0139` edge `1.9237` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.6103` n `32` status `ready` deltaP `31.9444` edge `1.7697` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.6103` n `32` status `ready` deltaP `31.9444` edge `1.7697` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2552` n `32` status `ready` deltaP `31.25` edge `0.7296` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2552` n `32` status `ready` deltaP `31.25` edge `0.7296` maxDD `0.0`
- `market_context_high->equity_24h` score `6.504` n `131` status `ready` deltaP `15.2963` edge `0.743` maxDD `-14.5715`
- `market_context_high->unknown_24h` score `6.1519` n `131` status `ready` deltaP `-18.4239` edge `3.9444` maxDD `-213.9626`
- `market_context_high->index_24h` score `5.9599` n `131` status `ready` deltaP `25.9065` edge `0.4379` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.5721` n `54` status `ready` deltaP `13.4655` edge `0.4868` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.5721` n `54` status `ready` deltaP `13.4655` edge `0.4868` maxDD `-5.9781`
- `market_context_high->metal_24h` score `4.0601` n `131` status `ready` deltaP `23.5223` edge `0.3247` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6348` n `54` status `ready` deltaP `22.0076` edge `0.1863` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6348` n `54` status `ready` deltaP `22.0076` edge `0.1863` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.7536` n `131` status `ready` deltaP `1.2749` edge `0.584` maxDD `-31.0425`
- `risk_on_high->metal_24h` score `1.4032` n `32` status `ready` deltaP `14.4097` edge `0.047` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4032` n `32` status `ready` deltaP `14.4097` edge `0.047` maxDD `-0.7574`
- `market_context_high->crypto_major_4h` score `1.3177` n `191` status `ready` deltaP `10.1496` edge `0.2322` maxDD `-10.5381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

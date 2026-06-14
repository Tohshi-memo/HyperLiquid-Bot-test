# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T00:22:33.909418+00:00`
- Price records: `672`
- Market context records: `3841`
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

- `risk_on_high->crypto_major_24h` score `33.3262` n `32` status `ready` deltaP `34.0278` edge `2.5546` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.3262` n `32` status `ready` deltaP `34.0278` edge `2.5546` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.4911` n `32` status `ready` deltaP `42.0139` edge `1.9275` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.4911` n `32` status `ready` deltaP `42.0139` edge `1.9275` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.6451` n `32` status `ready` deltaP `31.9444` edge `1.7726` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.6451` n `32` status `ready` deltaP `31.9444` edge `1.7726` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2564` n `32` status `ready` deltaP `31.25` edge `0.7297` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2564` n `32` status `ready` deltaP `31.25` edge `0.7297` maxDD `0.0`
- `market_context_high->unknown_24h` score `8.6529` n `129` status `ready` deltaP `-18.2978` edge `4.1432` maxDD `-204.9499`
- `market_context_high->equity_24h` score `6.472` n `129` status `ready` deltaP `14.8821` edge `0.7431` maxDD `-14.5715`
- `market_context_high->index_24h` score `6.0241` n `129` status `ready` deltaP `25.8236` edge `0.4438` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.6158` n `56` status `ready` deltaP `14.6559` edge `0.4825` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.6158` n `56` status `ready` deltaP `14.6559` edge `0.4825` maxDD `-5.9781`
- `market_context_high->metal_24h` score `3.9883` n `129` status `ready` deltaP `23.1791` edge `0.321` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6138` n `56` status `ready` deltaP `22.7351` edge `0.1797` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6138` n `56` status `ready` deltaP `22.7351` edge `0.1797` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.4212` n `32` status `ready` deltaP `14.4097` edge `0.0485` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4212` n `32` status `ready` deltaP `14.4097` edge `0.0485` maxDD `-0.7574`
- `market_context_high->crypto_major_4h` score `1.2121` n `191` status `ready` deltaP `10.1496` edge `0.2234` maxDD `-10.5381`
- `market_context_high->crypto_major_24h` score `1.1367` n `129` status `ready` deltaP `0.7187` edge `0.5363` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T00:07:30.927551+00:00`
- Price records: `672`
- Market context records: `3840`
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

- `risk_on_high->crypto_major_24h` score `33.253` n `32` status `ready` deltaP `34.0278` edge `2.5485` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.253` n `32` status `ready` deltaP `34.0278` edge `2.5485` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.4647` n `32` status `ready` deltaP `42.0139` edge `1.9253` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.4647` n `32` status `ready` deltaP `42.0139` edge `1.9253` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.6259` n `32` status `ready` deltaP `31.9444` edge `1.771` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.6259` n `32` status `ready` deltaP `31.9444` edge `1.771` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2552` n `32` status `ready` deltaP `31.25` edge `0.7296` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2552` n `32` status `ready` deltaP `31.25` edge `0.7296` maxDD `0.0`
- `market_context_high->unknown_24h` score `7.4038` n `130` status `ready` deltaP `-18.3627` edge `4.0432` maxDD `-209.3928`
- `market_context_high->equity_24h` score `6.4983` n `130` status `ready` deltaP `15.0908` edge `0.7439` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.9926` n `130` status `ready` deltaP `25.8654` edge `0.4409` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.605` n `55` status `ready` deltaP `14.0715` edge `0.4855` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.605` n `55` status `ready` deltaP `14.0715` edge `0.4855` maxDD `-5.9781`
- `market_context_high->metal_24h` score `4.0261` n `130` status `ready` deltaP `23.352` edge `0.323` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6273` n `55` status `ready` deltaP `22.378` edge `0.1832` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6273` n `55` status `ready` deltaP `22.378` edge `0.1832` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.4495` n `130` status `ready` deltaP `0.999` edge `0.5605` maxDD `-31.0425`
- `risk_on_high->metal_24h` score `1.4128` n `32` status `ready` deltaP `14.4097` edge `0.0478` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4128` n `32` status `ready` deltaP `14.4097` edge `0.0478` maxDD `-0.7574`
- `market_context_high->crypto_major_4h` score `1.2661` n `191` status `ready` deltaP `10.1496` edge `0.2279` maxDD `-10.5381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T03:22:29.281040+00:00`
- Price records: `672`
- Market context records: `3853`
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

- `risk_on_high->unknown_4h` score `53.2149` n `68` status `ready` deltaP `11.4598` edge `6.9602` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `53.2149` n `68` status `ready` deltaP `11.4598` edge `6.9602` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `33.9862` n `32` status `ready` deltaP `34.0278` edge `2.6096` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.9862` n `32` status `ready` deltaP `34.0278` edge `2.6096` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8307` n `32` status `ready` deltaP `42.0139` edge `1.9558` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8307` n `32` status `ready` deltaP `42.0139` edge `1.9558` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.6667` n `32` status `ready` deltaP `31.9444` edge `1.7744` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.6667` n `32` status `ready` deltaP `31.9444` edge `1.7744` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3044` n `32` status `ready` deltaP `31.25` edge `0.7337` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3044` n `32` status `ready` deltaP `31.25` edge `0.7337` maxDD `0.0`
- `market_context_high->unknown_24h` score `9.047` n `128` status `ready` deltaP `-19.7917` edge `4.14` maxDD `-200.1879`
- `market_context_high->unknown_4h` score `8.8699` n `202` status `ready` deltaP `1.1802` edge `1.6702` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.7023` n `128` status `ready` deltaP `14.6701` edge `0.7637` maxDD `-14.5715`
- `market_context_high->index_24h` score `6.0783` n `128` status `ready` deltaP `25.7812` edge `0.4486` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.3366` n `68` status `ready` deltaP `17.6919` edge `0.439` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.3366` n `68` status `ready` deltaP `17.6919` edge `0.439` maxDD `-5.9781`
- `market_context_high->metal_24h` score `3.8297` n `128` status `ready` deltaP `21.9619` edge `0.3159` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.5373` n `68` status `ready` deltaP `24.8834` edge `0.159` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5373` n `68` status `ready` deltaP `24.8834` edge `0.159` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `1.4225` n `202` status `ready` deltaP `11.4601` edge `0.2322` maxDD `-10.5381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

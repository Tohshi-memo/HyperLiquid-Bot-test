# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T00:37:25.457333+00:00`
- Price records: `672`
- Market context records: `3842`
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

- `risk_on_high->crypto_major_24h` score `33.397` n `32` status `ready` deltaP `34.0278` edge `2.5605` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.397` n `32` status `ready` deltaP `34.0278` edge `2.5605` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.5283` n `32` status `ready` deltaP `42.0139` edge `1.9306` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.5283` n `32` status `ready` deltaP `42.0139` edge `1.9306` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.6607` n `32` status `ready` deltaP `31.9444` edge `1.7739` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.6607` n `32` status `ready` deltaP `31.9444` edge `1.7739` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2624` n `32` status `ready` deltaP `31.25` edge `0.7302` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2624` n `32` status `ready` deltaP `31.25` edge `0.7302` maxDD `0.0`
- `market_context_high->unknown_24h` score `9.9636` n `128` status `ready` deltaP `-18.2292` edge `4.2471` maxDD `-200.1879`
- `market_context_high->equity_24h` score `6.3999` n `128` status `ready` deltaP `14.6701` edge `0.7385` maxDD `-14.5715`
- `market_context_high->index_24h` score `6.0363` n `128` status `ready` deltaP `25.7812` edge `0.4451` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.6549` n `57` status `ready` deltaP `15.2199` edge `0.482` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.6549` n `57` status `ready` deltaP `15.2199` edge `0.482` maxDD `-5.9781`
- `market_context_high->metal_24h` score `3.943` n `128` status `ready` deltaP `23.0035` edge `0.3184` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6162` n `57` status `ready` deltaP `23.0798` edge `0.1776` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6162` n `57` status `ready` deltaP `23.0798` edge `0.1776` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.4368` n `32` status `ready` deltaP `14.4097` edge `0.0498` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4368` n `32` status `ready` deltaP `14.4097` edge `0.0498` maxDD `-0.7574`
- `market_context_high->crypto_major_4h` score `1.1749` n `191` status `ready` deltaP `10.1496` edge `0.2203` maxDD `-10.5381`
- `market_context_high->equity_4h` score `0.8375` n `191` status `ready` deltaP `11.4879` edge `0.1636` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

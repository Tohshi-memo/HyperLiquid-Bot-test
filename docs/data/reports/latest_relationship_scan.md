# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T07:52:30.168207+00:00`
- Price records: `672`
- Market context records: `3872`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13656`

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

- `risk_on_high->unknown_4h` score `48.2279` n `72` status `ready` deltaP `7.2662` edge `6.3488` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `48.2279` n `72` status `ready` deltaP `7.2662` edge `6.3488` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.3042` n `32` status `ready` deltaP `34.0278` edge `2.6361` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.3042` n `32` status `ready` deltaP `34.0278` edge `2.6361` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8655` n `32` status `ready` deltaP `42.0139` edge `1.9587` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8655` n `32` status `ready` deltaP `42.0139` edge `1.9587` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.3015` n `32` status `ready` deltaP `31.25` edge `1.7486` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.3015` n `32` status `ready` deltaP `31.25` edge `1.7486` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.1472` n `32` status `ready` deltaP `30.0347` edge `0.7287` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.1472` n `32` status `ready` deltaP `30.0347` edge `0.7287` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.5553` n `206` status `ready` deltaP `-0.5817` edge `1.5134` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.531` n `140` status `ready` deltaP `17.0139` edge `0.7338` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.66` n `72` status `ready` deltaP `19.9187` edge `0.4511` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.66` n `72` status `ready` deltaP `19.9187` edge `0.4511` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.4414` n `140` status `ready` deltaP `25.0347` edge `0.4005` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.3715` n `140` status `ready` deltaP `20.7788` edge `0.2856` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.5875` n `72` status `ready` deltaP `25.4065` edge `0.1597` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5875` n `72` status `ready` deltaP `25.4065` edge `0.1597` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.3653` n `140` status `ready` deltaP `3.5814` edge `0.6196` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.9984` n `206` status `ready` deltaP `13.6485` edge `0.2656` maxDD `-10.5381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

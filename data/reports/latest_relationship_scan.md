# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T14:22:35.674144+00:00`
- Price records: `672`
- Market context records: `4524`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `166.2705` n `39` status `ready` deltaP `20.7708` edge `13.8365` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `166.2705` n `39` status `ready` deltaP `20.7708` edge `13.8365` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `49.1651` n `186` status `ready` deltaP `6.0106` edge `4.1154` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `28.7762` n `186` status `ready` deltaP `8.612` edge `2.4972` maxDD `-7.5275`
- `risk_on_high->crypto_major_4h` score `7.1572` n `39` status `ready` deltaP `38.0668` edge `0.352` maxDD `-0.0812`
- `risk_on_and_context->crypto_major_4h` score `7.1572` n `39` status `ready` deltaP `38.0668` edge `0.352` maxDD `-0.0812`
- `risk_on_high->unknown_24h` score `5.531` n `39` status `ready` deltaP `17.8819` edge `0.3417` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.531` n `39` status `ready` deltaP `17.8819` edge `0.3417` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.3124` n `39` status `ready` deltaP `42.2256` edge `0.1612` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.3124` n `39` status `ready` deltaP `42.2256` edge `0.1612` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.8162` n `39` status `ready` deltaP `-5.3286` edge `0.6227` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `3.8162` n `39` status `ready` deltaP `-5.3286` edge `0.6227` maxDD `-4.834`
- `risk_on_high->equity_1h` score `2.3292` n `39` status `ready` deltaP `23.9483` edge `0.0541` maxDD `-0.2389`
- `risk_on_and_context->equity_1h` score `2.3292` n `39` status `ready` deltaP `23.9483` edge `0.0541` maxDD `-0.2389`
- `risk_on_high->metal_4h` score `2.2922` n `39` status `ready` deltaP `17.2765` edge `0.1094` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.2922` n `39` status `ready` deltaP `17.2765` edge `0.1094` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `2.1951` n `39` status `ready` deltaP `13.9721` edge `0.1115` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `2.1951` n `39` status `ready` deltaP `13.9721` edge `0.1115` maxDD `-0.7379`
- `risk_on_high->crypto_alt_4h` score `1.7065` n `39` status `ready` deltaP `9.5568` edge `0.1351` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `1.7065` n `39` status `ready` deltaP `9.5568` edge `0.1351` maxDD `-1.8615`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

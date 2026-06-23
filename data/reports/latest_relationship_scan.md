# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T16:38:00.231747+00:00`
- Price records: `672`
- Market context records: `4534`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9932`

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

- `risk_on_high->unknown_4h` score `136.6045` n `31` status `ready` deltaP `20.2793` edge `17.4973` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `136.6045` n `31` status `ready` deltaP `20.2793` edge `17.4973` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `52.8405` n `179` status `ready` deltaP `7.4583` edge `4.4037` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.6465` n `177` status `ready` deltaP `8.5607` edge `2.6534` maxDD `-7.5275`
- `risk_on_high->metal_24h` score `7.3913` n `31` status `ready` deltaP `-0.8456` edge `0.7195` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `7.3913` n `31` status `ready` deltaP `-0.8456` edge `0.7195` maxDD `-4.834`
- `risk_on_high->crypto_major_4h` score `6.7764` n `31` status `ready` deltaP `36.487` edge `0.3308` maxDD `-0.0812`
- `risk_on_and_context->crypto_major_4h` score `6.7764` n `31` status `ready` deltaP `36.487` edge `0.3308` maxDD `-0.0812`
- `risk_on_high->crypto_major_24h` score `5.5663` n `31` status `ready` deltaP `4.3179` edge `0.5352` maxDD `-5.0099`
- `risk_on_and_context->crypto_major_24h` score `5.5663` n `31` status `ready` deltaP `4.3179` edge `0.5352` maxDD `-5.0099`
- `risk_on_high->unknown_24h` score `5.4448` n `31` status `ready` deltaP `19.4444` edge `0.3241` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.4448` n `31` status `ready` deltaP `19.4444` edge `0.3241` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.0232` n `31` status `ready` deltaP `42.2256` edge `0.1371` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.0232` n `31` status `ready` deltaP `42.2256` edge `0.1371` maxDD `0.0`
- `risk_on_high->crypto_major_1h` score `1.9245` n `31` status `ready` deltaP `9.0448` edge `0.1218` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `1.9245` n `31` status `ready` deltaP `9.0448` edge `0.1218` maxDD `-0.7379`
- `risk_on_high->equity_1h` score `1.8876` n `31` status `ready` deltaP `19.4031` edge `0.0476` maxDD `-0.2389`
- `risk_on_and_context->equity_1h` score `1.8876` n `31` status `ready` deltaP `19.4031` edge `0.0476` maxDD `-0.2389`
- `risk_on_high->crypto_alt_4h` score `1.7433` n `31` status `ready` deltaP `9.461` edge `0.1388` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `1.7433` n `31` status `ready` deltaP `9.461` edge `0.1388` maxDD `-1.8615`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

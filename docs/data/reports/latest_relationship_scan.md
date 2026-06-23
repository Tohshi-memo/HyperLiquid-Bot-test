# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T14:37:30.239644+00:00`
- Price records: `672`
- Market context records: `4525`
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

- `risk_on_high->unknown_4h` score `171.3511` n `38` status `ready` deltaP `22.7776` edge `14.2465` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `171.3511` n `38` status `ready` deltaP `22.7776` edge `14.2465` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `49.6122` n `185` status `ready` deltaP `5.8246` edge `4.1539` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `29.0571` n `185` status `ready` deltaP `8.8374` edge `2.5191` maxDD `-7.5275`
- `risk_on_high->crypto_major_4h` score `7.1944` n `38` status `ready` deltaP `37.7969` edge `0.3569` maxDD `-0.0812`
- `risk_on_and_context->crypto_major_4h` score `7.1944` n `38` status `ready` deltaP `37.7969` edge `0.3569` maxDD `-0.0812`
- `risk_on_high->unknown_24h` score `5.4272` n `38` status `ready` deltaP `18.0556` edge `0.3319` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.4272` n `38` status `ready` deltaP `18.0556` edge `0.3319` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.2548` n `38` status `ready` deltaP `42.2256` edge `0.1564` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.2548` n `38` status `ready` deltaP `42.2256` edge `0.1564` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.9464` n `38` status `ready` deltaP `-4.2489` edge `0.6322` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `3.9464` n `38` status `ready` deltaP `-4.2489` edge `0.6322` maxDD `-4.834`
- `risk_on_high->crypto_major_1h` score `2.3739` n `38` status `ready` deltaP `15.5768` edge `0.1157` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `2.3739` n `38` status `ready` deltaP `15.5768` edge `0.1157` maxDD `-0.7379`
- `risk_on_high->equity_1h` score `2.2716` n `38` status `ready` deltaP `23.4085` edge `0.0529` maxDD `-0.2389`
- `risk_on_and_context->equity_1h` score `2.2716` n `38` status `ready` deltaP `23.4085` edge `0.0529` maxDD `-0.2389`
- `risk_on_high->metal_4h` score `2.2162` n `38` status `ready` deltaP `16.5517` edge `0.1079` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.2162` n `38` status `ready` deltaP `16.5517` edge `0.1079` maxDD `-1.3516`
- `risk_on_high->crypto_alt_4h` score `1.8455` n `38` status `ready` deltaP `11.0238` edge `0.1369` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `1.8455` n `38` status `ready` deltaP `11.0238` edge `0.1369` maxDD `-1.8615`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

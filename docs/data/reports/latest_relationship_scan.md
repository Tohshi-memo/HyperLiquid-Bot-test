# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T12:37:30.472766+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8970`

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

- `market_context_high->crypto_alt_4h` score `6.2756` n `117` status `ready` deltaP `16.612` edge `0.5571` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.1228` n `54` status `ready` deltaP `32.0` edge `0.2969` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1228` n `54` status `ready` deltaP `32.0` edge `0.2969` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.7284` n `117` status `ready` deltaP `20.8151` edge `0.4945` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `4.8644` n `54` status `ready` deltaP `18.8912` edge `0.3242` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.8644` n `54` status `ready` deltaP `18.8912` edge `0.3242` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.2632` n `54` status `ready` deltaP `33.9205` edge `0.4057` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2632` n `54` status `ready` deltaP `33.9205` edge `0.4057` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6355` n `117` status `ready` deltaP `13.4168` edge `0.1536` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.1422` n `117` status `ready` deltaP `5.8115` edge `0.137` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0176` n `117` status `ready` deltaP `12.2408` edge `0.0244` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.414` n `54` status `ready` deltaP `1.2531` edge `0.0108` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.414` n `54` status `ready` deltaP `1.2531` edge `0.0108` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.4512` n `117` status `ready` deltaP `6.6662` edge `0.0049` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.4585` n `117` status `ready` deltaP `-0.2541` edge `0.0015` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.5077` n `54` status `ready` deltaP `1.2531` edge `-0.0003` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5077` n `54` status `ready` deltaP `1.2531` edge `-0.0003` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.6701` n `54` status `ready` deltaP `3.1604` edge `-0.0044` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.6701` n `54` status `ready` deltaP `3.1604` edge `-0.0044` maxDD `-5.8734`
- `market_context_high->index_1h` score `-0.6945` n `117` status `ready` deltaP `-1.6286` edge `-0.0034` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

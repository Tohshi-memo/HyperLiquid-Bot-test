# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T10:37:28.650354+00:00`
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

- `market_context_high->crypto_alt_4h` score `6.3248` n `117` status `ready` deltaP `16.612` edge `0.5612` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.1612` n `54` status `ready` deltaP `32.0` edge `0.3001` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1612` n `54` status `ready` deltaP `32.0` edge `0.3001` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.8112` n `117` status `ready` deltaP `20.8151` edge `0.5014` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `4.9136` n `54` status `ready` deltaP `18.8912` edge `0.3283` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.9136` n `54` status `ready` deltaP `18.8912` edge `0.3283` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.3171` n `54` status `ready` deltaP `33.9205` edge `0.4126` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.3171` n `54` status `ready` deltaP `33.9205` edge `0.4126` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7267` n `117` status `ready` deltaP `13.8659` edge `0.1582` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2621` n `117` status `ready` deltaP `6.7097` edge `0.141` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0514` n `117` status `ready` deltaP `12.3932` edge `0.0262` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3361` n `54` status `ready` deltaP `2.1513` edge `0.0148` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3361` n `54` status `ready` deltaP `2.1513` edge `0.0148` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.4092` n `117` status `ready` deltaP `0.3465` edge `0.0016` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.4752` n `117` status `ready` deltaP `6.3668` edge `0.0049` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5232` n `54` status `ready` deltaP `0.9537` edge `-0.0003` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5232` n `54` status `ready` deltaP `0.9537` edge `-0.0003` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.6109` n `54` status `ready` deltaP `3.6095` edge `0.0002` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.6109` n `54` status `ready` deltaP `3.6095` edge `0.0002` maxDD `-5.8734`
- `market_context_high->index_1h` score `-0.6765` n `117` status `ready` deltaP `-1.3283` edge `-0.0031` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

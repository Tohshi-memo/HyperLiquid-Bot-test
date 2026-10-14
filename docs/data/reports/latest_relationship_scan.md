# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T05:22:23.481764+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9843`

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

- `market_context_high->crypto_alt_4h` score `6.4792` n `117` status `ready` deltaP `16.3071` edge `0.5761` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.3616` n `54` status `ready` deltaP `32.0` edge `0.3168` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3616` n `54` status `ready` deltaP `32.0` edge `0.3168` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.0164` n `117` status `ready` deltaP `20.8151` edge `0.5185` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.068` n `54` status `ready` deltaP `18.5863` edge `0.3432` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.068` n `54` status `ready` deltaP `18.5863` edge `0.3432` maxDD `-1.9151`
- `market_context_high->unknown_4h` score `4.6164` n `117` status `ready` deltaP `-3.0097` edge `0.4694` maxDD `-1.8373`
- `risk_on_high->crypto_major_4h` score `4.4504` n `54` status `ready` deltaP `33.9205` edge `0.4297` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4504` n `54` status `ready` deltaP `33.9205` edge `0.4297` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6343` n `117` status `ready` deltaP `13.4168` edge `0.1535` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2548` n `117` status `ready` deltaP `6.8594` edge `0.1394` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1442` n `117` status `ready` deltaP `12.6981` edge `0.0319` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3408` n `54` status `ready` deltaP `2.301` edge `0.0132` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3408` n `54` status `ready` deltaP `2.301` edge `0.0132` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3431` n `117` status `ready` deltaP `1.0973` edge `0.0021` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.4141` n `117` status `ready` deltaP `6.9656` edge `0.006` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4835` n `54` status `ready` deltaP `1.5525` edge `0.0008` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4835` n `54` status `ready` deltaP `1.5525` edge `0.0008` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.6195` n `117` status `ready` deltaP `-0.2772` edge `-0.0028` maxDD `-1.3154`
- `risk_on_high->crypto_alt_1h` score `-0.6709` n `54` status `ready` deltaP `3.1604` edge `-0.0045` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

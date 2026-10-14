# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T13:22:27.224514+00:00`
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

- `market_context_high->crypto_alt_4h` score `6.3729` n `117` status `ready` deltaP `16.7644` edge `0.5642` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.1252` n `54` status `ready` deltaP `32.0` edge `0.2971` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1252` n `54` status `ready` deltaP `32.0` edge `0.2971` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.7728` n `117` status `ready` deltaP `20.8151` edge `0.4982` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `4.9618` n `54` status `ready` deltaP `19.0436` edge `0.3313` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.9618` n `54` status `ready` deltaP `19.0436` edge `0.3313` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.2921` n `54` status `ready` deltaP `33.9205` edge `0.4094` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2921` n `54` status `ready` deltaP `33.9205` edge `0.4094` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7255` n `117` status `ready` deltaP `13.5665` edge `0.1601` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2154` n `117` status `ready` deltaP `5.9612` edge `0.1421` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0332` n `117` status `ready` deltaP `12.2408` edge `0.0257` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3664` n `54` status `ready` deltaP `1.4028` edge `0.0159` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3664` n `54` status `ready` deltaP `1.4028` edge `0.0159` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.4428` n `117` status `ready` deltaP `6.6662` edge `0.0056` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.4428` n `117` status `ready` deltaP `-0.1039` edge `0.0018` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.5022` n `54` status `ready` deltaP `1.2531` edge `0.0004` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5022` n `54` status `ready` deltaP `1.2531` edge `0.0004` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.6117` n `54` status `ready` deltaP `3.3101` edge `0.0021` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.6117` n `54` status `ready` deltaP `3.3101` edge `0.0021` maxDD `-5.8734`
- `market_context_high->index_1h` score `-0.6867` n `117` status `ready` deltaP `-1.6286` edge `-0.0024` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

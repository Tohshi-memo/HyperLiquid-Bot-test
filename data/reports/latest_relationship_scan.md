# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T14:37:29.504647+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9576`

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

- `market_context_high->crypto_alt_4h` score `8.2482` n `117` status `ready` deltaP `21.1851` edge `0.691` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `7.2085` n `117` status `ready` deltaP `24.931` edge `0.5904` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.8371` n `54` status `ready` deltaP `23.4643` edge `0.4581` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.8371` n `54` status `ready` deltaP `23.4643` edge `0.4581` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `6.1285` n `48` status `ready` deltaP `32.0557` edge `0.297` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1285` n `48` status `ready` deltaP `32.0557` edge `0.297` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.2253` n `54` status `ready` deltaP `38.0364` edge `0.5016` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.2253` n `54` status `ready` deltaP `38.0364` edge `0.5016` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `3.9294` n `117` status `ready` deltaP `-3.467` edge `0.4152` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.0865` n `117` status `ready` deltaP `14.7641` edge `0.1822` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5715` n `117` status `ready` deltaP `7.9073` edge `0.1588` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1468` n `117` status `ready` deltaP `12.8505` edge `0.0311` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1349` n `54` status `ready` deltaP `3.3489` edge `0.0326` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1349` n `54` status `ready` deltaP `3.3489` edge `0.0326` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3299` n `117` status `ready` deltaP `1.2474` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.377` n `54` status `ready` deltaP `4.5077` edge `0.0242` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.377` n `54` status `ready` deltaP `4.5077` edge `0.0242` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.4273` n `117` status `ready` deltaP `6.8159` edge `0.0059` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4921` n `54` status `ready` deltaP `1.4028` edge `0.0007` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4921` n `54` status `ready` deltaP `1.4028` edge `0.0007` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

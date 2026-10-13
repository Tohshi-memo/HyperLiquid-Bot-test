# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T11:07:37.006823+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9798`

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

- `market_context_high->crypto_alt_4h` score `7.998` n `117` status `ready` deltaP `20.7278` edge `0.6732` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `7.0771` n `117` status `ready` deltaP `24.4737` edge `0.5825` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.5869` n `54` status `ready` deltaP `23.007` edge `0.4403` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.5869` n `54` status `ready` deltaP `23.007` edge `0.4403` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.7047` n `48` status `ready` deltaP `31.3043` edge `0.2667` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.7047` n `48` status `ready` deltaP `31.3043` edge `0.2667` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.1399` n `54` status `ready` deltaP `37.5791` edge `0.4937` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.1399` n `54` status `ready` deltaP `37.5791` edge `0.4937` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `2.8086` n `117` status `ready` deltaP `-3.467` edge `0.3218` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.1501` n `117` status `ready` deltaP `15.0635` edge `0.1855` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.6194` n `117` status `ready` deltaP `8.2067` edge `0.1608` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0534` n `117` status `ready` deltaP `12.0883` edge `0.0284` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1038` n `54` status `ready` deltaP `3.6483` edge `0.0346` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1038` n `54` status `ready` deltaP `3.6483` edge `0.0346` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2675` n `117` status `ready` deltaP `1.9982` edge `0.0024` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.3357` n `54` status `ready` deltaP `4.8071` edge `0.0275` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.3357` n `54` status `ready` deltaP `4.8071` edge `0.0275` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.486` n `117` status `ready` deltaP `6.2171` edge `0.005` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5303` n `54` status `ready` deltaP `0.804` edge `-0.0002` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5303` n `54` status `ready` deltaP `0.804` edge `-0.0002` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

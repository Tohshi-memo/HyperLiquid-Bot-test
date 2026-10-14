# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T13:37:34.378909+00:00`
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

- `market_context_high->crypto_alt_4h` score `6.4007` n `117` status `ready` deltaP `16.9169` edge `0.5655` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.13` n `54` status `ready` deltaP `32.0` edge `0.2975` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.13` n `54` status `ready` deltaP `32.0` edge `0.2975` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.7788` n `117` status `ready` deltaP `20.8151` edge `0.4987` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `4.9896` n `54` status `ready` deltaP `19.1961` edge `0.3326` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.9896` n `54` status `ready` deltaP `19.1961` edge `0.3326` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.296` n `54` status `ready` deltaP `33.9205` edge `0.4099` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.296` n `54` status `ready` deltaP `33.9205` edge `0.4099` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7219` n `117` status `ready` deltaP `13.5665` edge `0.1598` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2106` n `117` status `ready` deltaP `5.9612` edge `0.1417` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.038` n `117` status `ready` deltaP `12.2408` edge `0.0261` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3695` n `54` status `ready` deltaP `1.4028` edge `0.0155` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3695` n `54` status `ready` deltaP `1.4028` edge `0.0155` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.4308` n `117` status `ready` deltaP `0.0462` edge `0.0018` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.4428` n `117` status `ready` deltaP `6.6662` edge `0.0056` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5022` n `54` status `ready` deltaP `1.2531` edge `0.0004` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5022` n `54` status `ready` deltaP `1.2531` edge `0.0004` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.614` n `54` status `ready` deltaP `3.3101` edge `0.0018` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.614` n `54` status `ready` deltaP `3.3101` edge `0.0018` maxDD `-5.8734`
- `market_context_high->index_1h` score `-0.6867` n `117` status `ready` deltaP `-1.6286` edge `-0.0024` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

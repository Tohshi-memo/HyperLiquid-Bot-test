# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T09:07:27.772651+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8508`

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

- `risk_on_high->commodity_24h` score `8.1199` n `54` status `ready` deltaP `43.554` edge `0.3863` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.1199` n `54` status `ready` deltaP `43.554` edge `0.3863` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.1998` n `122` status `ready` deltaP `18.1103` edge `0.5707` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.8534` n `122` status `ready` deltaP `21.0816` edge `0.4794` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.0062` n `54` status `ready` deltaP `20.8729` edge `0.3227` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.0062` n `54` status `ready` deltaP `20.8729` edge `0.3227` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.0149` n `54` status `ready` deltaP `34.5303` edge `0.3698` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.0149` n `54` status `ready` deltaP `34.5303` edge `0.3698` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.4627` n `127` status `ready` deltaP `13.3693` edge `0.1392` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9037` n `127` status `ready` deltaP `6.0552` edge `0.1155` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1544` n `122` status `ready` deltaP `10.7707` edge `0.0456` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.1944` n `127` status `ready` deltaP `9.4264` edge `0.0079` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3535` n `54` status `ready` deltaP `3.798` edge `0.0025` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3535` n `54` status `ready` deltaP `3.798` edge `0.0025` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.4135` n `127` status `ready` deltaP `3.4369` edge `-0.0011` maxDD `-1.3195`
- `market_context_high->fx_1h` score `-0.4174` n `127` status `ready` deltaP `-0.0201` edge `-0.0016` maxDD `-0.4757`
- `risk_on_high->index_1h` score `-0.424` n `54` status `ready` deltaP `-2.002` edge `-0.0026` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.424` n `54` status `ready` deltaP `-2.002` edge `-0.0026` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.4593` n `54` status `ready` deltaP `2.0016` edge `0.0` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4593` n `54` status `ready` deltaP `2.0016` edge `0.0` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T16:37:28.104589+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7188`

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

- `risk_on_high->commodity_24h` score `7.9588` n `54` status `ready` deltaP `42.3345` edge `0.381` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9588` n `54` status `ready` deltaP `42.3345` edge `0.381` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.2222` n `127` status `ready` deltaP `19.2145` edge `0.5652` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.7279` n `127` status `ready` deltaP `20.9681` edge `0.4697` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.2412` n `54` status `ready` deltaP `21.6351` edge `0.3372` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.2412` n `54` status `ready` deltaP `21.6351` edge `0.3372` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.9748` n `54` status `ready` deltaP `33.1583` edge `0.3738` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.9748` n `54` status `ready` deltaP `33.1583` edge `0.3738` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.5778` n `127` status `ready` deltaP `13.6687` edge `0.1468` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9925` n `127` status `ready` deltaP `6.2049` edge `0.1219` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4749` n `127` status `ready` deltaP `14.2368` edge `0.0492` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.1657` n `127` status `ready` deltaP `9.5761` edge `0.0093` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3348` n `54` status `ready` deltaP `3.9477` edge `0.0039` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3348` n `54` status `ready` deltaP `3.9477` edge `0.0039` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.401` n `127` status `ready` deltaP `3.4369` edge `0.0005` maxDD `-1.3195`
- `risk_on_high->crypto_major_1h` score `-0.4016` n `54` status `ready` deltaP `2.1513` edge `0.0064` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4016` n `54` status `ready` deltaP `2.1513` edge `0.0064` maxDD `-3.7781`
- `risk_on_high->index_1h` score `-0.4115` n `54` status `ready` deltaP `-2.002` edge `-0.001` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.4115` n `54` status `ready` deltaP `-2.002` edge `-0.001` maxDD `-0.7394`
- `market_context_high->fx_1h` score `-0.4596` n `127` status `ready` deltaP `-0.7709` edge `-0.002` maxDD `-0.4757`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

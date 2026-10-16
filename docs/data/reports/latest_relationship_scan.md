# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T08:37:27.629047+00:00`
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

- `risk_on_high->commodity_24h` score `8.0812` n `54` status `ready` deltaP `43.2056` edge `0.3854` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.0812` n `54` status `ready` deltaP `43.2056` edge `0.3854` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.2566` n `122` status `ready` deltaP `18.4152` edge `0.5734` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.8654` n `122` status `ready` deltaP `21.0816` edge `0.4804` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.063` n `54` status `ready` deltaP `21.1778` edge `0.3254` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.063` n `54` status `ready` deltaP `21.1778` edge `0.3254` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.0227` n `54` status `ready` deltaP `34.5303` edge `0.3708` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.0227` n `54` status `ready` deltaP `34.5303` edge `0.3708` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.4962` n `127` status `ready` deltaP `13.6687` edge `0.14` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9241` n `127` status `ready` deltaP `6.2049` edge `0.1162` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1836` n `122` status `ready` deltaP `11.0756` edge `0.046` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.1789` n `127` status `ready` deltaP `9.5761` edge `0.0082` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3434` n `54` status `ready` deltaP `3.9477` edge `0.0028` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3434` n `54` status `ready` deltaP `3.9477` edge `0.0028` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.4002` n `127` status `ready` deltaP `0.2802` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->index_1h` score `-0.4049` n `127` status `ready` deltaP `3.5871` edge `-0.001` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.4154` n `54` status `ready` deltaP `-1.8518` edge `-0.0025` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.4154` n `54` status `ready` deltaP `-1.8518` edge `-0.0025` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.446` n `54` status `ready` deltaP `2.1513` edge `0.0007` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.446` n `54` status `ready` deltaP `2.1513` edge `0.0007` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

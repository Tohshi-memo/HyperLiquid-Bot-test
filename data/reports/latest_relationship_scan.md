# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T02:07:23.396541+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8883`

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

- `risk_on_high->commodity_24h` score `7.9693` n `54` status `ready` deltaP `41.9861` edge `0.3842` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9693` n `54` status `ready` deltaP `41.9861` edge `0.3842` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.247` n `122` status `ready` deltaP `18.4152` edge `0.5726` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.7964` n `122` status `ready` deltaP `20.6243` edge `0.4777` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.0534` n `54` status `ready` deltaP `21.1778` edge `0.3246` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.0534` n `54` status `ready` deltaP `21.1778` edge `0.3246` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.9779` n `54` status `ready` deltaP `34.073` edge `0.3681` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.9779` n `54` status `ready` deltaP `34.073` edge `0.3681` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.4273` n `122` status `ready` deltaP `13.4068` edge `0.136` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9535` n `122` status `ready` deltaP `6.5574` edge `0.1163` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.277` n `122` status `ready` deltaP `11.8378` edge `0.0487` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2439` n `115` status `ready` deltaP `14.16` edge `0.1525` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3079` n `122` status `ready` deltaP `0.1378` edge `-0.002` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.3413` n `122` status `ready` deltaP `7.755` edge `0.0068` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.387` n `54` status `ready` deltaP `3.0495` edge `0.0032` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.387` n `54` status `ready` deltaP `3.0495` edge `0.0032` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.4733` n `54` status `ready` deltaP `1.8519` edge `-0.0008` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4733` n `54` status `ready` deltaP `1.8519` edge `-0.0008` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.4842` n `122` status `ready` deltaP `2.1145` edge `-0.0014` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.5145` n `54` status `ready` deltaP `-3.6536` edge `-0.0032` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

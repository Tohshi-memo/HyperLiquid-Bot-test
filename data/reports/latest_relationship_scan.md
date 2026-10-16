# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T01:52:27.458268+00:00`
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

- `risk_on_high->commodity_24h` score `7.9705` n `54` status `ready` deltaP `41.9861` edge `0.3843` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9705` n `54` status `ready` deltaP `41.9861` edge `0.3843` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.1988` n `122` status `ready` deltaP `18.2627` edge `0.5696` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.753` n `122` status `ready` deltaP `20.4718` edge `0.4751` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.0052` n `54` status `ready` deltaP `21.0253` edge `0.3216` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.0052` n `54` status `ready` deltaP `21.0253` edge `0.3216` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.9497` n `54` status `ready` deltaP `33.9205` edge `0.3655` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.9497` n `54` status `ready` deltaP `33.9205` edge `0.3655` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.4165` n `122` status `ready` deltaP `13.4068` edge `0.1351` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9331` n `122` status `ready` deltaP `6.4077` edge `0.1156` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.26` n `122` status `ready` deltaP `11.6853` edge `0.0483` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2431` n `115` status `ready` deltaP `14.16` edge `0.1526` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3157` n `122` status `ready` deltaP `-0.0124` edge `-0.002` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.3413` n `122` status `ready` deltaP `7.755` edge `0.0068` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.387` n `54` status `ready` deltaP `3.0495` edge `0.0032` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.387` n `54` status `ready` deltaP `3.0495` edge `0.0032` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.4866` n `54` status `ready` deltaP `1.7022` edge `-0.0015` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4866` n `54` status `ready` deltaP `1.7022` edge `-0.0015` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.4928` n `122` status `ready` deltaP `1.9643` edge `-0.0015` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.5231` n `54` status `ready` deltaP `-3.8038` edge `-0.0033` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

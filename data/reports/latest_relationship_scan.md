# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T14:22:27.578463+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8978`

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

- `market_context_high->crypto_alt_4h` score `7.9872` n `122` status `ready` deltaP `18.2627` edge `0.6353` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.8931` n `54` status `ready` deltaP `41.2892` edge `0.3825` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.8931` n `54` status `ready` deltaP `41.2892` edge `0.3825` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.1231` n `122` status `ready` deltaP `19.8621` edge `0.51` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.7936` n `54` status `ready` deltaP `21.0253` edge `0.3873` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.7936` n `54` status `ready` deltaP `21.0253` edge `0.3873` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.1902` n `54` status `ready` deltaP `33.3108` edge `0.4004` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.1902` n `54` status `ready` deltaP `33.3108` edge `0.4004` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.9096` n `122` status `ready` deltaP `13.8559` edge `0.1732` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1864` n `122` status `ready` deltaP `5.8089` edge `0.1407` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0157` n `122` status `ready` deltaP `10.161` edge `0.0381` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2934` n `115` status `ready` deltaP `13.4631` edge `0.1508` maxDD `-11.5869`
- `risk_on_high->crypto_major_1h` score `-0.3219` n `54` status `ready` deltaP `1.1034` edge `0.0236` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3219` n `54` status `ready` deltaP `1.1034` edge `0.0236` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.334` n `54` status `ready` deltaP `4.6574` edge `0.0284` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.334` n `54` status `ready` deltaP `4.6574` edge `0.0284` maxDD `-5.8485`
- `market_context_high->fx_1h` score `-0.3454` n `122` status `ready` deltaP `-0.613` edge `-0.0018` maxDD `-0.4047`
- `market_context_high->index_1h` score `-0.4733` n `122` status `ready` deltaP `1.9643` edge `0.001` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.5036` n `54` status `ready` deltaP `-3.8038` edge `-0.0008` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.5036` n `54` status `ready` deltaP `-3.8038` edge `-0.0008` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

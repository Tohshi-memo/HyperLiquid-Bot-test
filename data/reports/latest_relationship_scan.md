# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T16:52:29.824958+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9192`

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

- `risk_on_high->commodity_24h` score `7.8883` n `54` status `ready` deltaP `41.2892` edge `0.3821` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.8883` n `54` status `ready` deltaP `41.2892` edge `0.3821` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.0597` n `122` status `ready` deltaP `17.3481` edge `0.5641` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.5099` n `122` status `ready` deltaP `18.9474` edge `0.465` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.866` n `54` status `ready` deltaP `20.1107` edge `0.3161` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.866` n `54` status `ready` deltaP `20.1107` edge `0.3161` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.7916` n `54` status `ready` deltaP `32.3961` edge `0.3554` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.7916` n `54` status `ready` deltaP `32.3961` edge `0.3554` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.191` n `122` status `ready` deltaP `12.5086` edge `0.1223` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.673` n `122` status `ready` deltaP `4.761` edge `0.1049` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0059` n `122` status `ready` deltaP `10.0085` edge `0.0383` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2965` n `115` status `ready` deltaP `13.4631` edge `0.1504` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3789` n `122` status `ready` deltaP `-1.2136` edge `-0.0021` maxDD `-0.4047`
- `risk_on_high->metal_1h` score `-0.5069` n `54` status `ready` deltaP `1.1034` edge `0.0008` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5069` n `54` status `ready` deltaP `1.1034` edge `0.0008` maxDD `-0.8513`
- `market_context_high->metal_1h` score `-0.5258` n `122` status `ready` deltaP `5.8089` edge `0.0044` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.5397` n `122` status `ready` deltaP `1.0634` edge `-0.0015` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.57` n `54` status `ready` deltaP `-4.7047` edge `-0.0033` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.57` n `54` status `ready` deltaP `-4.7047` edge `-0.0033` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.6556` n `54` status `ready` deltaP `0.0555` edge `-0.0122` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

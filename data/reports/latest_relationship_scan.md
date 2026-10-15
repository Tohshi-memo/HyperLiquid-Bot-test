# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T15:37:35.338614+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9112`

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

- `risk_on_high->commodity_24h` score `7.8847` n `54` status `ready` deltaP `41.2892` edge `0.3818` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.8847` n `54` status `ready` deltaP `41.2892` edge `0.3818` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.3347` n `122` status `ready` deltaP `17.5005` edge `0.586` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.6661` n `122` status `ready` deltaP `19.0999` edge `0.477` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.141` n `54` status `ready` deltaP `20.2631` edge `0.338` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.141` n `54` status `ready` deltaP `20.2631` edge `0.338` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.8932` n `54` status `ready` deltaP `32.5486` edge `0.3674` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.8932` n `54` status `ready` deltaP `32.5486` edge `0.3674` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3637` n `122` status `ready` deltaP `13.1074` edge `0.1327` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.7773` n `122` status `ready` deltaP `5.0604` edge `0.1116` maxDD `-3.7781`
- `market_context_high->metal_4h` score `-0.0147` n `122` status `ready` deltaP `9.8561` edge `0.0376` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2989` n `115` status `ready` deltaP `13.4631` edge `0.1501` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3454` n `122` status `ready` deltaP `-0.613` edge `-0.0018` maxDD `-0.4047`
- `market_context_high->index_1h` score `-0.5272` n `122` status `ready` deltaP `1.2136` edge `-0.0009` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.545` n `54` status `ready` deltaP `0.5046` edge `-0.0001` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.545` n `54` status `ready` deltaP `0.5046` edge `-0.0001` maxDD `-0.8513`
- `risk_on_high->index_1h` score `-0.5575` n `54` status `ready` deltaP `-4.5545` edge `-0.0027` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.5575` n `54` status `ready` deltaP `-4.5545` edge `-0.0027` maxDD `-0.7394`
- `market_context_high->metal_1h` score `-0.5845` n `122` status `ready` deltaP `5.2101` edge `0.0035` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.5878` n `54` status `ready` deltaP `0.3549` edge `-0.0055` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

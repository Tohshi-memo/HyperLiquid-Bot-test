# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T15:52:33.817027+00:00`
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

- `risk_on_high->commodity_24h` score `7.8835` n `54` status `ready` deltaP `41.2892` edge `0.3817` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.8835` n `54` status `ready` deltaP `41.2892` edge `0.3817` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.2517` n `122` status `ready` deltaP `17.3481` edge `0.5801` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.6059` n `122` status `ready` deltaP `18.9474` edge `0.473` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.058` n `54` status `ready` deltaP `20.1107` edge `0.3321` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.058` n `54` status `ready` deltaP `20.1107` edge `0.3321` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.854` n `54` status `ready` deltaP `32.3961` edge `0.3634` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.854` n `54` status `ready` deltaP `32.3961` edge `0.3634` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3049` n `122` status `ready` deltaP `12.9577` edge `0.1288` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.7293` n `122` status `ready` deltaP `4.9107` edge `0.1086` maxDD `-3.7781`
- `market_context_high->metal_4h` score `-0.0147` n `122` status `ready` deltaP `9.8561` edge `0.0376` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2996` n `115` status `ready` deltaP `13.4631` edge `0.15` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.354` n `122` status `ready` deltaP `-0.7631` edge `-0.0019` maxDD `-0.4047`
- `market_context_high->index_1h` score `-0.5279` n `122` status `ready` deltaP `1.2136` edge `-0.001` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.5365` n `54` status `ready` deltaP `0.6543` edge `0.0` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5365` n `54` status `ready` deltaP `0.6543` edge `0.0` maxDD `-0.8513`
- `risk_on_high->index_1h` score `-0.5583` n `54` status `ready` deltaP `-4.5545` edge `-0.0028` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.5583` n `54` status `ready` deltaP `-4.5545` edge `-0.0028` maxDD `-0.7394`
- `market_context_high->metal_1h` score `-0.5714` n `122` status `ready` deltaP `5.3598` edge `0.0036` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.619` n `54` status `ready` deltaP `0.2052` edge `-0.0085` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

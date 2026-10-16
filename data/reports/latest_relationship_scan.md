# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T07:37:27.553225+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9142`

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

- `risk_on_high->commodity_24h` score `8.0836` n `54` status `ready` deltaP `43.2056` edge `0.3856` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.0836` n `54` status `ready` deltaP `43.2056` edge `0.3856` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.3786` n `122` status `ready` deltaP `19.0249` edge `0.5795` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.9282` n `122` status `ready` deltaP `21.3865` edge `0.4836` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.1849` n `54` status `ready` deltaP `21.7875` edge `0.3315` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.1849` n `54` status `ready` deltaP `21.7875` edge `0.3315` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.0635` n `54` status `ready` deltaP `34.8352` edge `0.374` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.0635` n `54` status `ready` deltaP `34.8352` edge `0.374` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.5696` n `126` status `ready` deltaP `14.1812` edge `0.1427` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9979` n `126` status `ready` deltaP `6.7983` edge `0.1184` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1958` n `122` status `ready` deltaP `11.228` edge `0.046` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2106` n `126` status `ready` deltaP `9.2387` edge `0.0078` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3426` n `54` status `ready` deltaP `3.9477` edge `0.0029` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3426` n `54` status `ready` deltaP `3.9477` edge `0.0029` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.4055` n `126` status `ready` deltaP `0.1931` edge `-0.0015` maxDD `-0.4757`
- `market_context_high->index_1h` score `-0.4171` n `126` status `ready` deltaP `3.3677` edge `-0.0011` maxDD `-1.3195`
- `risk_on_high->crypto_major_1h` score `-0.4359` n `54` status `ready` deltaP `2.301` edge `0.001` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4359` n `54` status `ready` deltaP `2.301` edge `0.001` maxDD `-3.7781`
- `risk_on_high->index_1h` score `-0.4482` n `54` status `ready` deltaP `-2.4524` edge `-0.0027` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.4482` n `54` status `ready` deltaP `-2.4524` edge `-0.0027` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

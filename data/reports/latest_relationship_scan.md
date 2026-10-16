# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T08:22:31.157883+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8532`

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

- `risk_on_high->commodity_24h` score `8.0637` n `54` status `ready` deltaP `43.0314` edge `0.3851` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.0637` n `54` status `ready` deltaP `43.0314` edge `0.3851` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.2868` n `122` status `ready` deltaP `18.5676` edge `0.5749` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.8738` n `122` status `ready` deltaP `21.0816` edge `0.4811` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.0932` n `54` status `ready` deltaP `21.3302` edge `0.3269` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.0932` n `54` status `ready` deltaP `21.3302` edge `0.3269` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.0282` n `54` status `ready` deltaP `34.5303` edge `0.3715` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.0282` n `54` status `ready` deltaP `34.5303` edge `0.3715` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.5118` n `127` status `ready` deltaP `13.8184` edge `0.1403` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9421` n `127` status `ready` deltaP `6.3546` edge `0.1167` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1848` n `122` status `ready` deltaP `11.0756` edge `0.0461` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.1777` n `127` status `ready` deltaP `9.5761` edge `0.0083` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3426` n `54` status `ready` deltaP `3.9477` edge `0.0029` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3426` n `54` status `ready` deltaP `3.9477` edge `0.0029` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.3916` n `127` status `ready` deltaP `0.4303` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->index_1h` score `-0.4135` n `127` status `ready` deltaP `3.4369` edge `-0.0011` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.424` n `54` status `ready` deltaP `-2.002` edge `-0.0026` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.424` n `54` status `ready` deltaP `-2.002` edge `-0.0026` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.4344` n `54` status `ready` deltaP `2.301` edge `0.0012` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4344` n `54` status `ready` deltaP `2.301` edge `0.0012` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

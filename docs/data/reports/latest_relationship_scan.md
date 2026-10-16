# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T16:52:33.894809+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7164`

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

- `risk_on_high->commodity_24h` score `7.9292` n `54` status `ready` deltaP `42.1603` edge `0.3797` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9292` n `54` status `ready` deltaP `42.1603` edge `0.3797` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.2522` n `127` status `ready` deltaP `19.2145` edge `0.5677` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.7483` n `127` status `ready` deltaP `20.9681` edge `0.4714` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.2712` n `54` status `ready` deltaP `21.6351` edge `0.3397` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.2712` n `54` status `ready` deltaP `21.6351` edge `0.3397` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.988` n `54` status `ready` deltaP `33.1583` edge `0.3755` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.988` n `54` status `ready` deltaP `33.1583` edge `0.3755` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.5814` n `127` status `ready` deltaP `13.6687` edge `0.1471` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9925` n `127` status `ready` deltaP `6.2049` edge `0.1219` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4907` n `127` status `ready` deltaP `14.3893` edge `0.0495` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.1525` n `127` status `ready` deltaP `9.7258` edge `0.0094` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3262` n `54` status `ready` deltaP `4.0974` edge `0.004` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3262` n `54` status `ready` deltaP `4.0974` edge `0.004` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.3995` n `127` status `ready` deltaP `3.4369` edge `0.0007` maxDD `-1.3195`
- `risk_on_high->crypto_major_1h` score `-0.4016` n `54` status `ready` deltaP `2.1513` edge `0.0064` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4016` n `54` status `ready` deltaP `2.1513` edge `0.0064` maxDD `-3.7781`
- `risk_on_high->index_1h` score `-0.4099` n `54` status `ready` deltaP `-2.002` edge `-0.0008` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.4099` n `54` status `ready` deltaP `-2.002` edge `-0.0008` maxDD `-0.7394`
- `market_context_high->fx_1h` score `-0.4518` n `127` status `ready` deltaP `-0.6207` edge `-0.002` maxDD `-0.4757`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T23:37:25.786357+00:00`
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

- `risk_on_high->commodity_24h` score `7.9928` n `54` status `ready` deltaP `42.1603` edge `0.385` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9928` n `54` status `ready` deltaP `42.1603` edge `0.385` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.8879` n `122` status `ready` deltaP `17.1956` edge `0.5508` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.4851` n `122` status `ready` deltaP `19.2523` edge `0.4609` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.6942` n `54` status `ready` deltaP `19.9582` edge `0.3028` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.6942` n `54` status `ready` deltaP `19.9582` edge `0.3028` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.7755` n `54` status `ready` deltaP `32.701` edge `0.3513` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.7755` n `54` status `ready` deltaP `32.701` edge `0.3513` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3961` n `122` status `ready` deltaP `13.4068` edge `0.1334` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9031` n `122` status `ready` deltaP `6.258` edge `0.1141` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0819` n `122` status `ready` deltaP `10.3134` edge `0.0426` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2286` n `115` status `ready` deltaP `14.3342` edge `0.1533` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.297` n `122` status `ready` deltaP `0.2879` edge `-0.0016` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.4384` n `122` status `ready` deltaP `6.8568` edge `0.0047` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4501` n `54` status `ready` deltaP `2.1513` edge `0.0011` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4501` n `54` status `ready` deltaP `2.1513` edge `0.0011` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.506` n `54` status `ready` deltaP `1.5525` edge `-0.003` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.506` n `54` status `ready` deltaP `1.5525` edge `-0.003` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.5193` n `122` status `ready` deltaP `1.5139` edge `-0.0019` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.5497` n `54` status `ready` deltaP `-4.2542` edge `-0.0037` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

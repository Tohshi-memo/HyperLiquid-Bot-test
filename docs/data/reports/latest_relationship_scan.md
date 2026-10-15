# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T23:07:39.602259+00:00`
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

- `risk_on_high->commodity_24h` score `7.9892` n `54` status `ready` deltaP `42.1603` edge `0.3847` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9892` n `54` status `ready` deltaP `42.1603` edge `0.3847` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.8179` n `122` status `ready` deltaP `16.8908` edge `0.547` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.4271` n `122` status `ready` deltaP `18.9474` edge `0.4581` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.6242` n `54` status `ready` deltaP `19.6534` edge `0.299` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.6242` n `54` status `ready` deltaP `19.6534` edge `0.299` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.7378` n `54` status `ready` deltaP `32.3961` edge `0.3485` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.7378` n `54` status `ready` deltaP `32.3961` edge `0.3485` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3877` n `122` status `ready` deltaP `13.4068` edge `0.1327` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.8911` n `122` status `ready` deltaP `6.258` edge `0.1131` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0675` n `122` status `ready` deltaP `10.3134` edge `0.0414` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2309` n `115` status `ready` deltaP `14.3342` edge `0.153` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3141` n `122` status `ready` deltaP `-0.0124` edge `-0.0018` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.4671` n `122` status `ready` deltaP `6.5574` edge `0.0043` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4687` n `54` status `ready` deltaP `1.8519` edge `0.0007` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4687` n `54` status `ready` deltaP `1.8519` edge `0.0007` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.5138` n `54` status `ready` deltaP `1.5525` edge `-0.004` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.5138` n `54` status `ready` deltaP `1.5525` edge `-0.004` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.5279` n `122` status `ready` deltaP `1.3637` edge `-0.002` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.5583` n `54` status `ready` deltaP `-4.4044` edge `-0.0038` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

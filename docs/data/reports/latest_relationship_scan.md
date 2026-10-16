# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T05:52:28.288305+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9028`

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

- `risk_on_high->commodity_24h` score `8.0546` n `54` status `ready` deltaP `42.8571` edge `0.3855` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.0546` n `54` status `ready` deltaP `42.8571` edge `0.3855` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.5848` n `122` status `ready` deltaP `19.7871` edge `0.5916` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `6.0564` n `122` status `ready` deltaP `22.1487` edge `0.4892` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.3911` n `54` status `ready` deltaP `22.5497` edge `0.3436` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.3911` n `54` status `ready` deltaP `22.5497` edge `0.3436` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.1469` n `54` status `ready` deltaP `35.5974` edge `0.3796` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.1469` n `54` status `ready` deltaP `35.5974` edge `0.3796` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.4944` n `122` status `ready` deltaP `13.7062` edge `0.1396` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9859` n `122` status `ready` deltaP `6.7071` edge `0.118` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.27` n `122` status `ready` deltaP `11.9902` edge `0.0471` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.2814` n `122` status `ready` deltaP `0.5882` edge `-0.0016` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.3102` n `122` status `ready` deltaP `8.2041` edge `0.0064` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3667` n `54` status `ready` deltaP `3.4986` edge `0.0028` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3667` n `54` status `ready` deltaP `3.4986` edge `0.0028` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.4523` n `54` status `ready` deltaP `2.0016` edge `0.0009` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4523` n `54` status `ready` deltaP `2.0016` edge `0.0009` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.4624` n `122` status `ready` deltaP `2.5649` edge `-0.0016` maxDD `-1.3154`
- `market_context_high->commodity_24h` score `-0.4696` n `120` status `ready` deltaP `12.0238` edge `0.1378` maxDD `-11.5869`
- `risk_on_high->index_1h` score `-0.4927` n `54` status `ready` deltaP `-3.2032` edge `-0.0034` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

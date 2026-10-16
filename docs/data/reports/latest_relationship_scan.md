# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T04:52:30.122691+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9012`

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

- `risk_on_high->commodity_24h` score `8.0183` n `54` status `ready` deltaP `42.5087` edge `0.3848` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.0183` n `54` status `ready` deltaP `42.5087` edge `0.3848` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.5692` n `122` status `ready` deltaP `19.7871` edge `0.5903` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `6.054` n `122` status `ready` deltaP `22.1487` edge `0.489` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.3755` n `54` status `ready` deltaP `22.5497` edge `0.3423` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.3755` n `54` status `ready` deltaP `22.5497` edge `0.3423` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.1453` n `54` status `ready` deltaP `35.5974` edge `0.3794` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.1453` n `54` status `ready` deltaP `35.5974` edge `0.3794` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.4968` n `122` status `ready` deltaP `13.7062` edge `0.1398` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9931` n `122` status `ready` deltaP `6.7071` edge `0.1186` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2808` n `122` status `ready` deltaP `11.9902` edge `0.048` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.3165` n `122` status `ready` deltaP `-0.0124` edge `-0.0021` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.3677` n `122` status `ready` deltaP `7.6053` edge `0.0056` maxDD `-0.9556`
- `market_context_high->commodity_24h` score `-0.3847` n `118` status `ready` deltaP `12.8477` edge `0.1432` maxDD `-11.5869`
- `risk_on_high->metal_1h` score `-0.4041` n `54` status `ready` deltaP `2.8998` edge `0.002` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4041` n `54` status `ready` deltaP `2.8998` edge `0.002` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.4476` n `54` status `ready` deltaP `2.0016` edge `0.0015` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4476` n `54` status `ready` deltaP `2.0016` edge `0.0015` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.4788` n `122` status `ready` deltaP `2.2646` edge `-0.0017` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.5091` n `54` status `ready` deltaP `-3.5035` edge `-0.0035` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T00:52:34.001432+00:00`
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

- `risk_on_high->commodity_24h` score `7.9952` n `54` status `ready` deltaP `42.1603` edge `0.3852` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9952` n `54` status `ready` deltaP `42.1603` edge `0.3852` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.0579` n `122` status `ready` deltaP `17.8054` edge `0.5609` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.6397` n `122` status `ready` deltaP `20.0145` edge `0.4687` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.8642` n `54` status `ready` deltaP `20.568` edge `0.3129` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.8642` n `54` status `ready` deltaP `20.568` edge `0.3129` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.876` n `54` status `ready` deltaP `33.4632` edge `0.3591` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.876` n `54` status `ready` deltaP `33.4632` edge `0.3591` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3409` n `122` status `ready` deltaP `13.1074` edge `0.1308` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.8696` n `122` status `ready` deltaP `5.9586` edge `0.1133` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1836` n `122` status `ready` deltaP `11.0756` edge `0.046` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.227` n `115` status `ready` deltaP `14.3342` edge `0.1535` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.2892` n `122` status `ready` deltaP `0.4381` edge `-0.0016` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.3665` n `122` status `ready` deltaP `7.6053` edge `0.0057` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4033` n `54` status `ready` deltaP `2.8998` edge `0.0021` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4033` n `54` status `ready` deltaP `2.8998` edge `0.0021` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.4834` n `122` status `ready` deltaP `2.1145` edge `-0.0013` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.5138` n `54` status `ready` deltaP `-3.6536` edge `-0.0031` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.5138` n `54` status `ready` deltaP `-3.6536` edge `-0.0031` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.5278` n `54` status `ready` deltaP `1.2531` edge `-0.0038` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

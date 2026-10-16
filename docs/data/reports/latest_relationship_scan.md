# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T01:07:27.337531+00:00`
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

- `risk_on_high->commodity_24h` score `7.994` n `54` status `ready` deltaP `42.1603` edge `0.3851` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.994` n `54` status `ready` deltaP `42.1603` edge `0.3851` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.0735` n `122` status `ready` deltaP `17.8054` edge `0.5622` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.6505` n `122` status `ready` deltaP `20.0145` edge `0.4696` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.8798` n `54` status `ready` deltaP `20.568` edge `0.3142` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.8798` n `54` status `ready` deltaP `20.568` edge `0.3142` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.883` n `54` status `ready` deltaP `33.4632` edge `0.36` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.883` n `54` status `ready` deltaP `33.4632` edge `0.36` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3457` n `122` status `ready` deltaP `13.1074` edge `0.1312` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.8696` n `122` status `ready` deltaP `5.9586` edge `0.1133` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2042` n `122` status `ready` deltaP `11.228` edge `0.0467` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2278` n `115` status `ready` deltaP `14.3342` edge `0.1534` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.2985` n `122` status `ready` deltaP `0.2879` edge `-0.0018` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.3497` n `122` status `ready` deltaP `7.755` edge `0.0061` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3924` n `54` status `ready` deltaP `3.0495` edge `0.0025` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3924` n `54` status `ready` deltaP `3.0495` edge `0.0025` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.4928` n `122` status `ready` deltaP `1.9643` edge `-0.0015` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.5231` n `54` status `ready` deltaP `-3.8038` edge `-0.0033` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.5231` n `54` status `ready` deltaP `-3.8038` edge `-0.0033` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.5278` n `54` status `ready` deltaP `1.2531` edge `-0.0038` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

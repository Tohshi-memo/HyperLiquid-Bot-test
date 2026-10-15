# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T14:07:34.427226+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8962`

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

- `market_context_high->crypto_alt_4h` score `8.1038` n `122` status `ready` deltaP `18.4152` edge `0.644` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.8955` n `54` status `ready` deltaP `41.2892` edge `0.3827` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.8955` n `54` status `ready` deltaP `41.2892` edge `0.3827` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.2073` n `122` status `ready` deltaP `20.0145` edge `0.516` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.9102` n `54` status `ready` deltaP `21.1778` edge `0.396` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.9102` n `54` status `ready` deltaP `21.1778` edge `0.396` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.2449` n `54` status `ready` deltaP `33.4632` edge `0.4064` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2449` n `54` status `ready` deltaP `33.4632` edge `0.4064` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.9192` n `122` status `ready` deltaP `13.8559` edge `0.174` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.196` n `122` status `ready` deltaP `5.8089` edge `0.1415` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0157` n `122` status `ready` deltaP `10.161` edge `0.0381` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2918` n `115` status `ready` deltaP `13.4631` edge `0.151` maxDD `-11.5869`
- `risk_on_high->crypto_major_1h` score `-0.3157` n `54` status `ready` deltaP `1.1034` edge `0.0244` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3157` n `54` status `ready` deltaP `1.1034` edge `0.0244` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3278` n `54` status `ready` deltaP `4.6574` edge `0.0292` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3278` n `54` status `ready` deltaP `4.6574` edge `0.0292` maxDD `-5.8485`
- `market_context_high->fx_1h` score `-0.3454` n `122` status `ready` deltaP `-0.613` edge `-0.0018` maxDD `-0.4047`
- `market_context_high->index_1h` score `-0.4639` n `122` status `ready` deltaP `2.1145` edge `0.0012` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.4943` n `54` status `ready` deltaP `-3.6536` edge `-0.0006` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.4943` n `54` status `ready` deltaP `-3.6536` edge `-0.0006` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

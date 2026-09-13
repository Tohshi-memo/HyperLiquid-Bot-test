# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T16:31:50.980306+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13440`

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

- `market_context_high->unknown_24h` score `17792.8805` n `56` status `ready` deltaP `8.596` edge `1482.7029` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `8516.6108` n `36` status `ready` deltaP `10.977` edge `709.6519` maxDD `-0.2677`
- `risk_on_and_context->unknown_24h` score `8516.6108` n `36` status `ready` deltaP `10.977` edge `709.6519` maxDD `-0.2677`
- `news_risk_high->unknown_1h` score `422.2599` n `82` status `ready` deltaP `-4.9511` edge `35.2635` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6091` n `82` status `ready` deltaP `35.8578` edge `1.3605` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.4036` n `82` status `ready` deltaP `38.0236` edge `1.4272` maxDD `-9.098`
- `news_risk_high->equity_24h` score `8.9004` n `82` status `ready` deltaP `25.8915` edge `0.7471` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.9591` n `82` status `ready` deltaP `49.6635` edge `0.2665` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.6086` n `82` status `ready` deltaP `24.7603` edge `0.2644` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.301` n `36` status `ready` deltaP `39.8276` edge `0.0929` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.301` n `36` status `ready` deltaP `39.8276` edge `0.0929` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.2554` n `56` status `ready` deltaP `39.8276` edge `0.0891` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `3.5521` n `36` status `ready` deltaP `11.2643` edge `0.4858` maxDD `-6.1069`
- `risk_on_and_context->crypto_alt_24h` score `3.5521` n `36` status `ready` deltaP `11.2643` edge `0.4858` maxDD `-6.1069`
- `market_context_high->crypto_alt_24h` score `3.108` n `56` status `ready` deltaP `8.2881` edge `0.4854` maxDD `-8.7091`
- `market_context_high->metal_24h` score `0.9576` n `56` status `ready` deltaP `12.2167` edge `0.1244` maxDD `-1.3125`
- `risk_on_high->index_24h` score `0.5566` n `36` status `ready` deltaP `26.6283` edge `-0.0007` maxDD `-3.7704`
- `risk_on_and_context->index_24h` score `0.5566` n `36` status `ready` deltaP `26.6283` edge `-0.0007` maxDD `-3.7704`
- `news_risk_high->index_4h` score `0.3974` n `82` status `ready` deltaP `12.0427` edge `0.0335` maxDD `-0.6935`
- `market_context_high->index_24h` score `0.3762` n `56` status `ready` deltaP `28.0172` edge `0.0125` maxDD `-5.0836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T16:37:27.177677+00:00`
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

- `market_context_high->unknown_24h` score `17792.8961` n `56` status `ready` deltaP `8.596` edge `1482.7042` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `8516.6481` n `36` status `ready` deltaP `10.977` edge `709.654` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `8516.6481` n `36` status `ready` deltaP `10.977` edge `709.654` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `422.2587` n `82` status `ready` deltaP `-4.9511` edge `35.2634` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6091` n `82` status `ready` deltaP `35.8578` edge `1.3605` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.4048` n `82` status `ready` deltaP `38.0236` edge `1.4273` maxDD `-9.098`
- `news_risk_high->equity_24h` score `8.9004` n `82` status `ready` deltaP `25.8915` edge `0.7471` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.9591` n `82` status `ready` deltaP `49.6635` edge `0.2665` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.6086` n `82` status `ready` deltaP `24.7603` edge `0.2644` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.2902` n `36` status `ready` deltaP `39.8276` edge `0.092` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.2902` n `36` status `ready` deltaP `39.8276` edge `0.092` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.2482` n `56` status `ready` deltaP `39.8276` edge `0.0885` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `3.5533` n `36` status `ready` deltaP `11.2643` edge `0.4859` maxDD `-6.1024`
- `risk_on_and_context->crypto_alt_24h` score `3.5533` n `36` status `ready` deltaP `11.2643` edge `0.4859` maxDD `-6.1024`
- `market_context_high->crypto_alt_24h` score `3.1084` n `56` status `ready` deltaP `8.2881` edge `0.4854` maxDD `-8.7046`
- `market_context_high->metal_24h` score `0.9563` n `56` status `ready` deltaP `12.2167` edge `0.1243` maxDD `-1.3176`
- `risk_on_high->index_24h` score `0.5565` n `36` status `ready` deltaP `26.6283` edge `-0.0007` maxDD `-3.7709`
- `risk_on_and_context->index_24h` score `0.5565` n `36` status `ready` deltaP `26.6283` edge `-0.0007` maxDD `-3.7709`
- `news_risk_high->index_4h` score `0.3974` n `82` status `ready` deltaP `12.0427` edge `0.0335` maxDD `-0.6935`
- `market_context_high->index_24h` score `0.3762` n `56` status `ready` deltaP `28.0172` edge `0.0125` maxDD `-5.0841`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

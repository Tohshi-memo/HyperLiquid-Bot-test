# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T21:37:31.243105+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `157.3398` n `83` status `ready` deltaP `-26.1713` edge `20.6146` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `6.8286` n `83` status `ready` deltaP `41.3404` edge `0.2992` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.0826` n `117` status `ready` deltaP `12.0935` edge `0.0567` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0416` n `119` status `ready` deltaP `2.8594` edge `0.0186` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.2888` n `119` status `ready` deltaP `1.5939` edge `0.0018` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.3013` n `117` status `ready` deltaP `4.4338` edge `0.0058` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.5191` n `119` status `ready` deltaP `1.5939` edge `-0.0056` maxDD `-1.7257`
- `market_context_high->metal_4h` score `-0.5258` n `117` status `ready` deltaP `11.2662` edge `-0.0018` maxDD `-4.5909`
- `market_context_high->index_1h` score `-0.7182` n `119` status `ready` deltaP `-5.5678` edge `-0.0028` maxDD `-0.5064`
- `market_context_high->index_4h` score `-1.1294` n `117` status `ready` deltaP `-8.7463` edge `-0.0056` maxDD `-0.8045`
- `market_context_high->index_24h` score `-1.7337` n `83` status `ready` deltaP `1.0772` edge `-0.0556` maxDD `-1.3511`
- `market_context_high->fx_24h` score `-1.8508` n `83` status `ready` deltaP `-12.7552` edge `0.0085` maxDD `-1.8596`
- `market_context_high->crypto_major_4h` score `-2.0096` n `117` status `ready` deltaP `0.275` edge `-0.0322` maxDD `-6.6344`
- `market_context_high->metal_24h` score `-2.0634` n `83` status `ready` deltaP `-10.8664` edge `0.0591` maxDD `-7.0954`
- `market_context_high->crypto_major_1h` score `-2.2871` n `119` status `ready` deltaP `-5.7616` edge `-0.0373` maxDD `-5.8571`
- `market_context_high->crypto_alt_1h` score `-2.354` n `119` status `ready` deltaP `-4.9212` edge `-0.0294` maxDD `-7.0497`
- `market_context_high->crypto_major_24h` score `-2.7016` n `83` status `ready` deltaP `-4.7273` edge `0.0765` maxDD `-23.3076`
- `market_context_high->equity_1h` score `-2.7165` n `119` status `ready` deltaP `-11.1747` edge `-0.0479` maxDD `-4.9846`
- `market_context_high->crypto_alt_4h` score `-6.4395` n `117` status `ready` deltaP `-9.0669` edge `-0.0696` maxDD `-19.8597`
- `market_context_high->unknown_1h` score `-6.4987` n `119` status `ready` deltaP `3.7576` edge `-0.5269` maxDD `-0.8437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

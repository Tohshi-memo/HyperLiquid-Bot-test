# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T22:37:24.627229+00:00`
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

- `market_context_high->unknown_24h` score `125.9274` n `82` status `ready` deltaP `-29.0566` edge `16.6066` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `6.0977` n `82` status `ready` deltaP `39.2192` edge `0.2566` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `0.9612` n `113` status `ready` deltaP `11.3708` edge `0.0514` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.279` n `117` status `ready` deltaP `1.0019` edge `0.0112` maxDD `-0.624`
- `market_context_high->metal_4h` score `-0.3439` n `113` status `ready` deltaP `13.505` edge `0.0066` maxDD `-4.5909`
- `market_context_high->fx_1h` score `-0.388` n `117` status `ready` deltaP `0.3839` edge `0.0016` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.4194` n `113` status `ready` deltaP `3.3469` edge `0.0032` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.4603` n `117` status `ready` deltaP `2.3492` edge `-0.0031` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.604` n `117` status `ready` deltaP `-3.5953` edge `-0.0013` maxDD `-0.5064`
- `market_context_high->crypto_major_4h` score `-0.8304` n `113` status `ready` deltaP `2.06` edge `-0.0129` maxDD `-4.2507`
- `market_context_high->index_24h` score `-1.0933` n `82` status `ready` deltaP `4.967` edge `-0.0493` maxDD `-0.9939`
- `market_context_high->index_4h` score `-1.097` n `113` status `ready` deltaP `-8.2128` edge `-0.005` maxDD `-0.8045`
- `market_context_high->crypto_major_24h` score `-1.9339` n `82` status `ready` deltaP `-4.1836` edge `0.102` maxDD `-19.0973`
- `market_context_high->fx_24h` score `-2.1228` n `82` status `ready` deltaP `-16.3363` edge `-0.0025` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-2.2784` n `82` status `ready` deltaP `-13.5459` edge `0.0494` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-2.4299` n `117` status `ready` deltaP `-5.5556` edge `-0.0353` maxDD `-6.7455`
- `market_context_high->crypto_major_1h` score `-2.4426` n `117` status `ready` deltaP `-6.4103` edge `-0.04` maxDD `-5.6654`
- `market_context_high->equity_1h` score `-2.4926` n `117` status `ready` deltaP `-10.3703` edge `-0.0433` maxDD `-4.289`
- `market_context_high->crypto_alt_4h` score `-5.7305` n `113` status `ready` deltaP `-7.6449` edge `-0.0509` maxDD `-17.3874`
- `market_context_high->equity_24h` score `-6.3855` n `82` status `ready` deltaP `-0.6225` edge `-0.3717` maxDD `-28.4238`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

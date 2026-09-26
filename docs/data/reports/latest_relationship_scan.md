# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T02:22:27.245528+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11662`

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

- `news_risk_high->unknown_24h` score `2518.0223` n `88` status `ready` deltaP `-0.7892` edge `209.8449` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.4226` n `47` status `ready` deltaP `8.3196` edge `5.9035` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.6537` n `47` status `ready` deltaP `27.2976` edge `3.9951` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.2328` n `47` status `ready` deltaP `24.782` edge `2.4755` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.25` n `47` status `ready` deltaP `33.2003` edge `1.9184` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.5391` n `47` status `ready` deltaP `34.0684` edge `0.4141` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6963` n `47` status `ready` deltaP `31.2389` edge `0.1236` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7217` n `47` status `ready` deltaP `17.2969` edge `0.1533` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5262` n `47` status `ready` deltaP `29.1483` edge `0.0316` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.1592` n `47` status `ready` deltaP `10.4502` edge `0.0937` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1069` n `47` status `ready` deltaP `12.664` edge `0.0481` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.8615` n `88` status `ready` deltaP `24.9526` edge `0.1102` maxDD `-6.9545`
- `market_context_high->index_1h` score `0.8062` n `47` status `ready` deltaP `12.8137` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5213` n `47` status `ready` deltaP `10.7083` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.2991` n `47` status `ready` deltaP `4.9019` edge `0.074` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.2872` n `47` status `ready` deltaP `3.9277` edge `0.0882` maxDD `-5.2359`
- `news_risk_high->crypto_alt_1h` score `0.2117` n `117` status `ready` deltaP `7.8152` edge `0.0661` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.1755` n `117` status `ready` deltaP `5.8307` edge `0.005` maxDD `-0.3395`
- `news_risk_high->equity_4h` score `0.1753` n `105` status `ready` deltaP `16.8917` edge `0.0708` maxDD `-9.2079`
- `market_context_high->fx_4h` score `0.0591` n `47` status `ready` deltaP `9.6264` edge `0.0075` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

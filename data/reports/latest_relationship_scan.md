# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T07:07:29.418386+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10233`

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

- `risk_on_high->crypto_alt_24h` score `8.3972` n `117` status `ready` deltaP `21.2473` edge `0.5811` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.3972` n `117` status `ready` deltaP `21.2473` edge `0.5811` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.828` n `117` status `ready` deltaP `31.5497` edge `0.3125` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.828` n `117` status `ready` deltaP `31.5497` edge `0.3125` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.0371` n `117` status `ready` deltaP `21.1005` edge `0.9119` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.0371` n `117` status `ready` deltaP `21.1005` edge `0.9119` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8595` n `117` status `ready` deltaP `26.1335` edge `0.3166` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8595` n `117` status `ready` deltaP `26.1335` edge `0.3166` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.3498` n `241` status `ready` deltaP `13.9025` edge `0.2692` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `1.0449` n `117` status `ready` deltaP `4.2467` edge `0.094` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0449` n `117` status `ready` deltaP `4.2467` edge `0.094` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.813` n `117` status `ready` deltaP `9.7623` edge `0.0069` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.813` n `117` status `ready` deltaP `9.7623` edge `0.0069` maxDD `-0.0051`
- `risk_on_high->equity_1h` score `0.6092` n `117` status `ready` deltaP `14.9714` edge `0.0041` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.6092` n `117` status `ready` deltaP `14.9714` edge `0.0041` maxDD `-2.2516`
- `risk_on_high->crypto_major_1h` score `0.3644` n `117` status `ready` deltaP `4.6331` edge `0.0722` maxDD `-3.1509`
- `risk_on_and_context->crypto_major_1h` score `0.3644` n `117` status `ready` deltaP `4.6331` edge `0.0722` maxDD `-3.1509`
- `risk_on_high->metal_1h` score `0.2941` n `117` status `ready` deltaP `9.9788` edge `0.0042` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.2941` n `117` status `ready` deltaP `9.9788` edge `0.0042` maxDD `-0.3081`
- `market_context_high->equity_24h` score `0.2662` n `241` status `ready` deltaP `7.8125` edge `-0.0299` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T06:22:31.273292+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10223`

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

- `risk_on_high->crypto_alt_24h` score `8.4778` n `117` status `ready` deltaP `21.5946` edge `0.5855` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.4778` n `117` status `ready` deltaP `21.5946` edge `0.5855` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.8424` n `117` status `ready` deltaP `31.5497` edge `0.3137` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.8424` n `117` status `ready` deltaP `31.5497` edge `0.3137` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.0527` n `117` status `ready` deltaP `21.1005` edge `0.9139` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.0527` n `117` status `ready` deltaP `21.1005` edge `0.9139` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8715` n `117` status `ready` deltaP `26.1335` edge `0.3176` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8715` n `117` status `ready` deltaP `26.1335` edge `0.3176` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.4303` n `241` status `ready` deltaP `14.2498` edge `0.2736` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `1.0293` n `117` status `ready` deltaP `4.2467` edge `0.0927` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0293` n `117` status `ready` deltaP `4.2467` edge `0.0927` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.837` n `117` status `ready` deltaP `9.7623` edge `0.0089` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.837` n `117` status `ready` deltaP `9.7623` edge `0.0089` maxDD `-0.0051`
- `risk_on_high->equity_1h` score `0.6187` n `117` status `ready` deltaP `15.1211` edge `0.0039` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.6187` n `117` status `ready` deltaP `15.1211` edge `0.0039` maxDD `-2.2516`
- `market_context_high->equity_24h` score `0.4054` n `241` status `ready` deltaP `7.8125` edge `-0.0183` maxDD `0.0`
- `risk_on_high->crypto_major_1h` score `0.3668` n `117` status `ready` deltaP `4.6331` edge `0.0724` maxDD `-3.1509`
- `risk_on_and_context->crypto_major_1h` score `0.3668` n `117` status `ready` deltaP `4.6331` edge `0.0724` maxDD `-3.1509`
- `risk_on_high->metal_1h` score `0.3027` n `117` status `ready` deltaP `10.1285` edge `0.0043` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.3027` n `117` status `ready` deltaP `10.1285` edge `0.0043` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

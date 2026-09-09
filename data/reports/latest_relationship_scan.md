# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T18:46:07.514036+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10148`

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

- `risk_on_high->crypto_alt_24h` score `10.7336` n `117` status `ready` deltaP `23.6779` edge `0.7596` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `10.7336` n `117` status `ready` deltaP `23.6779` edge `0.7596` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.8865` n `117` status `ready` deltaP `33.2265` edge `0.3062` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.8865` n `117` status `ready` deltaP `33.2265` edge `0.3062` maxDD `-1.9733`
- `market_context_high->crypto_alt_24h` score `5.6862` n `241` status `ready` deltaP `16.3331` edge `0.4477` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `5.5097` n `117` status `ready` deltaP `19.538` edge `0.9829` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.5097` n `117` status `ready` deltaP `19.538` edge `0.9829` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.103` n `117` status `ready` deltaP `23.847` edge `0.2688` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.103` n `117` status `ready` deltaP `23.847` edge `0.2688` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.3702` n `117` status `ready` deltaP `24.172` edge `0.0406` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.3702` n `117` status `ready` deltaP `24.172` edge `0.0406` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.6487` n `241` status `ready` deltaP `19.2672` edge `0.0483` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.0419` n `241` status `ready` deltaP `7.6389` edge `0.0359` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `0.889` n `117` status `ready` deltaP `3.6479` edge `0.085` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.889` n `117` status `ready` deltaP `3.6479` edge `0.085` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.7395` n `117` status `ready` deltaP `19.7383` edge `0.0788` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7395` n `117` status `ready` deltaP `19.7383` edge `0.0788` maxDD `-0.9131`
- `risk_on_high->equity_24h` score `0.3567` n `117` status `ready` deltaP `7.6389` edge `-0.0212` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.3567` n `117` status `ready` deltaP `7.6389` edge `-0.0212` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.3466` n `117` status `ready` deltaP `13.6241` edge `-0.0088` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

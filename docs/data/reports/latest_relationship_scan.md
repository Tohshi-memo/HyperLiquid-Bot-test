# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T17:23:02.696540+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10457`

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

- `risk_on_high->unknown_24h` score `264.0515` n `101` status `ready` deltaP `23.2639` edge `21.8492` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `264.0515` n `101` status `ready` deltaP `23.2639` edge `21.8492` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `18.0322` n `101` status `ready` deltaP `32.4739` edge `1.4149` maxDD `-7.6301`
- `risk_on_and_context->crypto_major_24h` score `18.0322` n `101` status `ready` deltaP `32.4739` edge `1.4149` maxDD `-7.6301`
- `risk_on_high->crypto_alt_24h` score `13.4592` n `101` status `ready` deltaP `31.4752` edge `0.9179` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `13.4592` n `101` status `ready` deltaP `31.4752` edge `0.9179` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `7.714` n `213` status `ready` deltaP `24.4841` edge `0.5371` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.6376` n `117` status `ready` deltaP `30.0253` edge `0.3068` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.6376` n `117` status `ready` deltaP `30.0253` edge `0.3068` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.9691` n `117` status `ready` deltaP `26.4384` edge `0.3237` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.9691` n `117` status `ready` deltaP `26.4384` edge `0.3237` maxDD `-3.8693`
- `market_context_high->equity_24h` score `4.359` n `213` status `ready` deltaP `16.4931` edge `0.2533` maxDD `0.0`
- `risk_on_high->equity_24h` score `3.6198` n `101` status `ready` deltaP `16.4931` edge `0.1917` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.6198` n `101` status `ready` deltaP `16.4931` edge `0.1917` maxDD `0.0`
- `risk_on_high->index_24h` score `2.0546` n `101` status `ready` deltaP `18.0366` edge `0.0552` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.0546` n `101` status `ready` deltaP `18.0366` edge `0.0552` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.3003` n `213` status `ready` deltaP `12.5562` edge `0.064` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9944` n `117` status `ready` deltaP `4.6958` edge `0.0868` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9944` n `117` status `ready` deltaP `4.6958` edge `0.0868` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6515` n `101` status `ready` deltaP `17.1015` edge `0.0851` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

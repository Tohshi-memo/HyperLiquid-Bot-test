# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T03:22:30.957202+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10385`

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

- `market_context_high->unknown_24h` score `1632.5594` n `241` status `ready` deltaP `17.7465` edge `135.9335` maxDD `-0.0819`
- `risk_on_high->unknown_24h` score `1603.2509` n `117` status `ready` deltaP `18.5764` edge `133.4804` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `1603.2509` n `117` status `ready` deltaP `18.5764` edge `133.4804` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `8.9792` n `117` status `ready` deltaP `23.6779` edge `0.6134` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.9792` n `117` status `ready` deltaP `23.6779` edge `0.6134` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.9576` n `117` status `ready` deltaP `31.5497` edge `0.3233` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.9576` n `117` status `ready` deltaP `31.5497` edge `0.3233` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.1822` n `117` status `ready` deltaP `21.1005` edge `0.9305` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.1822` n `117` status `ready` deltaP `21.1005` edge `0.9305` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.9519` n `117` status `ready` deltaP `26.1335` edge `0.3243` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.9519` n `117` status `ready` deltaP `26.1335` edge `0.3243` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.9318` n `241` status `ready` deltaP `16.3331` edge `0.3015` maxDD `-3.9523`
- `market_context_high->equity_24h` score `1.2727` n `241` status `ready` deltaP `9.5486` edge `0.0424` maxDD `0.0`
- `risk_on_high->index_24h` score `1.1235` n `117` status `ready` deltaP `11.4984` edge `0.0212` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.1235` n `117` status `ready` deltaP `11.4984` edge `0.0212` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `1.0137` n `117` status `ready` deltaP `4.2467` edge `0.0914` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0137` n `117` status `ready` deltaP `4.2467` edge `0.0914` maxDD `-1.1521`
- `risk_on_high->equity_24h` score `0.5875` n `117` status `ready` deltaP `9.5486` edge `-0.0147` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.5875` n `117` status `ready` deltaP `9.5486` edge `-0.0147` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.5204` n `117` status `ready` deltaP `14.5223` edge `-0.0003` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

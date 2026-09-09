# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T18:22:28.291616+00:00`
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

- `risk_on_high->crypto_alt_24h` score `10.5182` n `117` status `ready` deltaP `23.5043` edge `0.7428` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `10.5182` n `117` status `ready` deltaP `23.5043` edge `0.7428` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.8733` n `117` status `ready` deltaP `33.2265` edge `0.3051` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.8733` n `117` status `ready` deltaP `33.2265` edge `0.3051` maxDD `-1.9733`
- `market_context_high->crypto_alt_24h` score `5.4707` n `241` status `ready` deltaP `16.1595` edge `0.4309` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `5.3571` n `117` status `ready` deltaP `19.3643` edge `0.9645` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.3571` n `117` status `ready` deltaP `19.3643` edge `0.9645` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.0874` n `117` status `ready` deltaP `23.847` edge `0.2675` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.0874` n `117` status `ready` deltaP `23.847` edge `0.2675` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.3256` n `117` status `ready` deltaP `23.8248` edge `0.0392` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.3256` n `117` status `ready` deltaP `23.8248` edge `0.0392` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.6042` n `241` status `ready` deltaP `18.92` edge `0.0469` maxDD `-0.1483`
- `market_context_high->equity_24h` score `0.9253` n `241` status `ready` deltaP `7.2917` edge `0.0285` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `0.8974` n `117` status `ready` deltaP `3.6479` edge `0.0857` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8974` n `117` status `ready` deltaP `3.6479` edge `0.0857` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.7301` n `117` status `ready` deltaP `19.7383` edge `0.0776` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7301` n `117` status `ready` deltaP `19.7383` edge `0.0776` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.3286` n `117` status `ready` deltaP `13.4744` edge `-0.0093` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.3286` n `117` status `ready` deltaP `13.4744` edge `-0.0093` maxDD `-2.2516`
- `risk_on_high->equity_24h` score `0.2401` n `117` status `ready` deltaP `7.2917` edge `-0.0286` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

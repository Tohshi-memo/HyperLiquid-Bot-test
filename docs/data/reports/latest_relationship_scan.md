# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T04:22:24.191509+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10455`

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

- `risk_on_high->unknown_24h` score `546.7241` n `93` status `ready` deltaP `26.7361` edge `45.3821` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `546.7241` n `93` status `ready` deltaP `26.7361` edge `45.3821` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.1801` n `241` status `ready` deltaP `-2.8269` edge `2.1063` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `21.0062` n `93` status `ready` deltaP `34.2462` edge `1.5739` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `21.0062` n `93` status `ready` deltaP `34.2462` edge `1.5739` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `14.4681` n `93` status `ready` deltaP `31.0764` edge `0.9985` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.4681` n `93` status `ready` deltaP `31.0764` edge `0.9985` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.1911` n `182` status `ready` deltaP `24.483` edge `0.6602` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.6244` n `182` status `ready` deltaP `23.0903` edge `0.3981` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.4896` n `117` status `ready` deltaP `29.7204` edge `0.2965` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.4896` n `117` status `ready` deltaP `29.7204` edge `0.2965` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `5.326` n `93` status `ready` deltaP `23.0903` edge `0.2899` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.326` n `93` status `ready` deltaP `23.0903` edge `0.2899` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.9692` n `117` status `ready` deltaP `22.475` edge `0.2668` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.9692` n `117` status `ready` deltaP `22.475` edge `0.2668` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7758` n `93` status `ready` deltaP `23.8575` edge `0.0765` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7758` n `93` status `ready` deltaP `23.8575` edge `0.0765` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6715` n `182` status `ready` deltaP `22.1382` edge `0.0965` maxDD `-0.0505`
- `risk_on_high->metal_24h` score `1.0414` n `93` status `ready` deltaP `17.5348` edge `0.1322` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `1.0414` n `93` status `ready` deltaP `17.5348` edge `0.1322` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

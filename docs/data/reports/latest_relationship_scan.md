# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T14:22:34.895631+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10202`

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

- `risk_on_high->unknown_24h` score `377.0965` n `93` status `ready` deltaP `24.8264` edge `31.2592` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `377.0965` n `93` status `ready` deltaP `24.8264` edge `31.2592` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `22.4818` n `93` status `ready` deltaP `39.2809` edge `1.6633` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.4818` n `93` status `ready` deltaP `39.2809` edge `1.6633` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.227` n `93` status `ready` deltaP `32.1181` edge `1.0548` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.227` n `93` status `ready` deltaP `32.1181` edge `1.0548` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.4045` n `201` status `ready` deltaP `24.6554` edge `0.5935` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.3013` n `117` status `ready` deltaP `28.8058` edge `0.2869` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3013` n `117` status `ready` deltaP `28.8058` edge `0.2869` maxDD `-1.9733`
- `market_context_high->equity_24h` score `5.1509` n `201` status `ready` deltaP `18.5764` edge `0.3054` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.4711` n `117` status `ready` deltaP `24.6092` edge `0.2944` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.4711` n `117` status `ready` deltaP `24.6092` edge `0.2944` maxDD `-3.8693`
- `risk_on_high->equity_24h` score `4.4657` n `93` status `ready` deltaP `18.5764` edge `0.2483` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.4657` n `93` status `ready` deltaP `18.5764` edge `0.2483` maxDD `0.0`
- `risk_on_high->index_24h` score `2.3052` n `93` status `ready` deltaP `19.8645` edge `0.0639` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.3052` n `93` status `ready` deltaP `19.8645` edge `0.0639` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.5226` n `201` status `ready` deltaP `14.1351` edge `0.072` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.8446` n `117` status `ready` deltaP `3.9473` edge `0.0793` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8446` n `117` status `ready` deltaP `3.9473` edge `0.0793` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.8221` n `93` status `ready` deltaP `17.1875` edge `0.1064` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

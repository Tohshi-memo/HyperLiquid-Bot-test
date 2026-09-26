# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T03:52:26.729927+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11730`

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

- `news_risk_high->unknown_24h` score `3040.9709` n `91` status `ready` deltaP `-0.7517` edge `253.4237` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `70.9402` n `47` status `ready` deltaP `8.1698` edge `5.8643` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.1671` n `47` status `ready` deltaP `26.2559` edge `3.9615` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.639` n `47` status `ready` deltaP `23.914` edge `2.4318` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2831` n `47` status `ready` deltaP `33.3739` edge `1.92` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.4492` n `47` status `ready` deltaP `33.2003` edge `0.4124` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6167` n `47` status `ready` deltaP `30.5445` edge `0.1216` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7277` n `47` status `ready` deltaP `17.2969` edge `0.1538` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5408` n `47` status `ready` deltaP `29.3007` edge `0.0318` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.0944` n `47` status `ready` deltaP `10.4502` edge `0.0883` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0925` n `47` status `ready` deltaP `12.5143` edge `0.0479` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `1.0112` n `91` status `ready` deltaP `26.4061` edge `0.1197` maxDD `-6.9545`
- `market_context_high->index_1h` score `0.7822` n `47` status `ready` deltaP `12.5143` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4973` n `47` status `ready` deltaP `10.4089` edge `0.0077` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.3832` n `91` status `ready` deltaP `13.2097` edge `0.044` maxDD `-2.344`
- `market_context_high->crypto_major_1h` score `0.3111` n `47` status `ready` deltaP `5.0516` edge `0.074` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.3015` n `120` status `ready` deltaP `7.3902` edge `0.0051` maxDD `-0.3395`
- `market_context_high->crypto_major_4h` score `0.2776` n `47` status `ready` deltaP `3.9277` edge `0.0874` maxDD `-5.2359`
- `news_risk_high->crypto_alt_1h` score `0.0371` n `120` status `ready` deltaP `6.2126` edge `0.0544` maxDD `-4.2849`
- `market_context_high->fx_4h` score `0.0347` n `47` status `ready` deltaP `9.3215` edge `0.0075` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

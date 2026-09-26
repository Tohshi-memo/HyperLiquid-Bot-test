# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T03:22:29.757994+00:00`
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

- `news_risk_high->unknown_24h` score `2953.1649` n `89` status `ready` deltaP `-0.7764` edge `246.1067` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `70.9654` n `47` status `ready` deltaP `8.3196` edge `5.8654` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.3293` n `47` status `ready` deltaP `26.6031` edge `3.9727` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.8491` n `47` status `ready` deltaP `24.2612` edge `2.447` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2783` n `47` status `ready` deltaP `33.3739` edge `1.9196` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.4854` n `47` status `ready` deltaP `33.5476` edge `0.4131` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6541` n `47` status `ready` deltaP `30.8917` edge `0.1224` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7253` n `47` status `ready` deltaP `17.2969` edge `0.1536` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5408` n `47` status `ready` deltaP `29.3007` edge `0.0318` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.1112` n `47` status `ready` deltaP `10.4502` edge `0.0897` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0925` n `47` status `ready` deltaP `12.5143` edge `0.0479` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.9681` n `89` status `ready` deltaP `26.0865` edge `0.1163` maxDD `-6.9545`
- `market_context_high->index_1h` score `0.7942` n `47` status `ready` deltaP `12.664` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5213` n `47` status `ready` deltaP `10.7083` edge `0.0077` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.3683` n `89` status `ready` deltaP `12.9643` edge `0.0444` maxDD `-2.344`
- `market_context_high->crypto_major_1h` score `0.3171` n `47` status `ready` deltaP `5.0516` edge `0.0745` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.2776` n `47` status `ready` deltaP `3.9277` edge `0.0874` maxDD `-5.2359`
- `news_risk_high->index_1h` score `0.2616` n `118` status `ready` deltaP `6.8761` edge `0.0052` maxDD `-0.3395`
- `news_risk_high->crypto_alt_1h` score `0.1437` n `118` status `ready` deltaP `7.2719` edge `0.061` maxDD `-4.2849`
- `news_risk_high->equity_4h` score `0.1114` n `106` status `ready` deltaP `16.1729` edge `0.0674` maxDD `-9.2079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

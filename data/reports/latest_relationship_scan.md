# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T03:37:26.352567+00:00`
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

- `news_risk_high->unknown_24h` score `2997.8731` n `90` status `ready` deltaP `-0.7639` edge `249.8323` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `70.9594` n `47` status `ready` deltaP `8.3196` edge `5.8649` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.2458` n `47` status `ready` deltaP `26.4295` edge `3.9669` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.7392` n `47` status `ready` deltaP `24.0876` edge `2.439` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2807` n `47` status `ready` deltaP `33.3739` edge `1.9198` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.4667` n `47` status `ready` deltaP `33.3739` edge `0.4127` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6366` n `47` status `ready` deltaP `30.7181` edge `0.1221` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7265` n `47` status `ready` deltaP `17.2969` edge `0.1537` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5408` n `47` status `ready` deltaP `29.3007` edge `0.0318` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.0992` n `47` status `ready` deltaP `10.4502` edge `0.0887` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0925` n `47` status `ready` deltaP `12.5143` edge `0.0479` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.9898` n `90` status `ready` deltaP `26.25` edge `0.118` maxDD `-6.9545`
- `market_context_high->index_1h` score `0.7822` n `47` status `ready` deltaP `12.5143` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5093` n `47` status `ready` deltaP `10.5586` edge `0.0077` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.3748` n `90` status `ready` deltaP `13.0902` edge `0.0441` maxDD `-2.344`
- `market_context_high->crypto_major_1h` score `0.3147` n `47` status `ready` deltaP `5.0516` edge `0.0743` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.2764` n `119` status `ready` deltaP `7.0611` edge `0.0052` maxDD `-0.3395`
- `market_context_high->crypto_major_4h` score `0.2764` n `47` status `ready` deltaP `3.9277` edge `0.0873` maxDD `-5.2359`
- `news_risk_high->crypto_alt_1h` score `0.0925` n `119` status `ready` deltaP `6.7378` edge `0.058` maxDD `-4.2849`
- `news_risk_high->equity_4h` score `0.056` n `107` status `ready` deltaP `15.4676` edge `0.065` maxDD `-9.2079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

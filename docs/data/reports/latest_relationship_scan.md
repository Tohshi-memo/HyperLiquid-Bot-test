# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T03:37:30.743190+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14774`

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

- `market_context_high->unknown_1h` score `1.3918` n `133` status `ready` deltaP `9.7351` edge `0.0738` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8344` n `133` status `ready` deltaP `22.4624` edge `-0.0363` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1889` n `133` status `ready` deltaP `9.5819` edge `0.0106` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1359` n `133` status `ready` deltaP `9.8577` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1463` n `133` status `ready` deltaP `1.8797` edge `0.0046` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2085` n `133` status `ready` deltaP `6.714` edge `0.0355` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2927` n `133` status `ready` deltaP `1.4306` edge `-0.0052` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3641` n `133` status `ready` deltaP `5.2517` edge `-0.0201` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.5703` n `133` status `ready` deltaP `0.3633` edge `0.0095` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6355` n `133` status `ready` deltaP `-3.8224` edge `0.0006` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6845` n `133` status `ready` deltaP `0.9445` edge `0.0095` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-1.0663` n `133` status `ready` deltaP `-0.0292` edge `-0.0085` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.3552` n `105` status `ready` deltaP `-3.5714` edge `0.0942` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.4472` n `133` status `ready` deltaP `-1.1008` edge `-0.0757` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.862` n `133` status `ready` deltaP `-2.4299` edge `0.058` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-2.272` n `133` status `ready` deltaP `3.5932` edge `-0.0863` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.311` n `105` status `ready` deltaP `-5.0099` edge `0.0018` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.3286` n `105` status `ready` deltaP `-7.1578` edge `-0.057` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-5.0593` n `133` status `ready` deltaP `-0.8871` edge `-0.3136` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.0828` n `105` status `ready` deltaP `-20.8879` edge `-0.1816` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

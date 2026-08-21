# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T22:22:25.076728+00:00`
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

- `market_context_high->unknown_1h` score `1.3343` n `133` status `ready` deltaP `8.9866` edge `0.074` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.4056` n `133` status `ready` deltaP `22.1575` edge `-0.07` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1989` n `133` status `ready` deltaP `11.0553` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1399` n `133` status `ready` deltaP `8.8197` edge `0.0094` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1011` n `133` status `ready` deltaP `2.7779` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2077` n `133` status `ready` deltaP `6.714` edge `0.0356` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3262` n `133` status `ready` deltaP `0.8318` edge `-0.0055` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3997` n `133` status `ready` deltaP `4.6419` edge `-0.0206` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.5753` n `133` status `ready` deltaP `2.9262` edge `0.0103` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.5892` n `133` status `ready` deltaP `0.0584` edge `0.0091` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6596` n `133` status `ready` deltaP `-4.2715` edge `0.0005` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.7832` n `133` status `ready` deltaP `0.5696` edge `0.0111` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.0495` n `105` status `ready` deltaP `-0.62` edge `0.1` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.3426` n `133` status `ready` deltaP `-1.5499` edge `-0.0593` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.404` n `133` status `ready` deltaP `3.8981` edge `-0.016` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8058` n `133` status `ready` deltaP `-1.5152` edge `0.0591` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.4341` n `105` status `ready` deltaP `-6.3988` edge `0.0008` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-4.1283` n `133` status `ready` deltaP `-0.1249` edge `-0.2411` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.3302` n `105` status `ready` deltaP `-7.505` edge `-0.0549` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.848` n `105` status `ready` deltaP `-18.4574` edge `-0.1677` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

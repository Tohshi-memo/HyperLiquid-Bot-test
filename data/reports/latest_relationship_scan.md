# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T17:22:29.647196+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13790`

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

- `market_context_high->unknown_1h` score `0.5485` n `133` status `ready` deltaP `7.9387` edge `0.0155` maxDD `-0.4843`
- `market_context_high->index_1h` score `0.1491` n `133` status `ready` deltaP `10.1571` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.0764` n `126` status `ready` deltaP `7.6582` edge `0.009` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1167` n `133` status `ready` deltaP `2.4785` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2116` n `133` status `ready` deltaP `6.714` edge `0.0351` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3534` n `133` status `ready` deltaP `0.3827` edge `-0.006` maxDD `-0.6822`
- `market_context_high->unknown_4h` score `-0.5198` n `126` status `ready` deltaP `20.8648` edge `-0.1385` maxDD `-0.5133`
- `market_context_high->metal_4h` score `-0.5583` n `126` status `ready` deltaP `2.2382` edge `-0.0249` maxDD `-1.5942`
- `market_context_high->commodity_1h` score `-0.6612` n `133` status `ready` deltaP `-4.2715` edge `0.0003` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.6668` n `133` status `ready` deltaP `0.5696` edge `0.0208` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7134` n `126` status `ready` deltaP `-1.9987` edge `0.0069` maxDD `-2.4692`
- `market_context_high->commodity_24h` score `-0.7246` n `105` status `ready` deltaP `2.3314` edge `0.1074` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.7619` n `126` status `ready` deltaP `-0.2734` edge `0.0077` maxDD `-2.618`
- `market_context_high->crypto_major_1h` score `-1.1905` n `133` status `ready` deltaP `-1.1008` edge `-0.0428` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.2968` n `126` status `ready` deltaP `3.2884` edge `-0.003` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.7253` n `126` status `ready` deltaP `-2.5237` edge `0.056` maxDD `-15.4959`
- `market_context_high->fx_24h` score `-2.7575` n `105` status `ready` deltaP `-9.8711` edge `-0.003` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.7322` n `126` status `ready` deltaP `0.4767` edge `-0.2121` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2496` n `105` status `ready` deltaP `-6.4633` edge `-0.0515` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.6955` n `105` status `ready` deltaP `-18.2837` edge `-0.1493` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

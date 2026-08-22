# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T08:52:28.148568+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14742`

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

- `market_context_high->unknown_1h` score `1.3454` n `134` status `ready` deltaP `8.0302` edge `0.0813` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5111` n `133` status `ready` deltaP `20.1758` edge `-0.048` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1291` n `134` status `ready` deltaP `9.697` edge `0.005` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1034` n `133` status `ready` deltaP `8.0575` edge `0.0098` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1588` n `134` status `ready` deltaP `1.64` edge `0.0046` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2036` n `134` status `ready` deltaP `6.5533` edge `0.0372` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.2195` n `133` status `ready` deltaP `7.5382` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.2615` n `134` status `ready` deltaP `1.9394` edge `-0.0046` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6363` n `133` status `ready` deltaP `1.7067` edge `0.0106` maxDD `-2.618`
- `market_context_high->commodity_1h` score `-0.6592` n `134` status `ready` deltaP `-4.0374` edge `-0.001` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7115` n `133` status `ready` deltaP `-1.6184` edge `0.0046` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.9246` n `134` status `ready` deltaP `-0.4781` edge `0.0063` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.5206` n `134` status `ready` deltaP `-2.8577` edge `-0.0734` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.5784` n `108` status `ready` deltaP `-4.8611` edge `0.0842` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-1.6895` n `133` status `ready` deltaP `4.9652` edge `-0.0469` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.7246` n `133` status `ready` deltaP `-1.3628` edge `0.0685` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.4322` n `108` status `ready` deltaP `-6.5394` edge `0.0019` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.2153` n `108` status `ready` deltaP `-5.2084` edge `-0.0521` maxDD `-18.9552`
- `market_context_high->metal_24h` score `-5.1201` n `108` status `ready` deltaP `-20.6597` edge `-0.1879` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.2191` n `133` status `ready` deltaP `-1.9542` edge `-0.3198` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

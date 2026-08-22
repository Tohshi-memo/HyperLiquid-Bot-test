# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T03:07:34.847533+00:00`
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

- `market_context_high->unknown_1h` score `1.4314` n `133` status `ready` deltaP `9.7351` edge `0.0771` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8732` n `133` status `ready` deltaP `22.7673` edge `-0.0351` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.2063` n `133` status `ready` deltaP `9.8868` edge `0.0108` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1437` n `133` status `ready` deltaP `10.0074` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1292` n `133` status `ready` deltaP `2.1791` edge `0.0048` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2085` n `133` status `ready` deltaP `6.714` edge `0.0355` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2763` n `133` status `ready` deltaP `1.73` edge `-0.0051` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3641` n `133` status `ready` deltaP `5.2517` edge `-0.0201` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.5687` n `133` status `ready` deltaP `0.3633` edge `0.0097` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6519` n `133` status `ready` deltaP `-4.1218` edge `0.0005` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6679` n `133` status `ready` deltaP `1.2494` edge `0.0096` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-0.9799` n `133` status `ready` deltaP `0.2702` edge `-0.0033` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.3226` n `105` status `ready` deltaP `-3.2242` edge `0.0946` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.3902` n `133` status `ready` deltaP `-0.9511` edge `-0.0694` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.8525` n `133` status `ready` deltaP `-2.2774` edge `0.0582` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-2.1484` n `133` status `ready` deltaP `3.5932` edge `-0.076` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.2796` n `105` status `ready` deltaP `-4.6627` edge `0.0021` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.3474` n `105` status `ready` deltaP `-7.505` edge `-0.0571` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.9137` n `133` status `ready` deltaP `-0.5822` edge `-0.3035` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.0668` n `105` status `ready` deltaP `-20.7143` edge `-0.1807` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

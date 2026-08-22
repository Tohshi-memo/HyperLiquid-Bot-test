# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T02:52:25.627990+00:00`
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

- `market_context_high->unknown_1h` score `1.4158` n `133` status `ready` deltaP `9.5854` edge `0.0768` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8866` n `133` status `ready` deltaP `22.9197` edge `-0.035` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.2151` n `133` status `ready` deltaP `10.0392` edge `0.0109` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1437` n `133` status `ready` deltaP `10.0074` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1214` n `133` status `ready` deltaP `2.3288` edge `0.0048` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2085` n `133` status `ready` deltaP `6.714` edge `0.0355` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2686` n `133` status `ready` deltaP `1.8797` edge `-0.0051` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3641` n `133` status `ready` deltaP `5.2517` edge `-0.0201` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.5687` n `133` status `ready` deltaP `0.3633` edge `0.0097` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6519` n `133` status `ready` deltaP `-4.1218` edge `0.0005` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.66` n `133` status `ready` deltaP `1.4018` edge `0.0096` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-0.9332` n `133` status `ready` deltaP `0.4199` edge `-0.0004` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.3214` n `105` status `ready` deltaP `-3.2242` edge `0.0947` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.3668` n `133` status `ready` deltaP `-0.9511` edge `-0.0664` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.843` n `133` status `ready` deltaP `-2.125` edge `0.0584` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-2.098` n `133` status `ready` deltaP `3.5932` edge `-0.0718` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.2621` n `105` status `ready` deltaP `-4.4891` edge `0.0024` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.3564` n `105` status `ready` deltaP `-7.6786` edge `-0.0571` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.8583` n `133` status `ready` deltaP `-0.4298` edge `-0.2999` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.0546` n `105` status `ready` deltaP `-20.5407` edge `-0.1803` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

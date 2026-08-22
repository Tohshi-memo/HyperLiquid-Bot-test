# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T01:52:26.285968+00:00`
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

- `market_context_high->unknown_1h` score `1.3822` n `133` status `ready` deltaP `9.286` edge `0.076` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.4836` n `133` status `ready` deltaP `23.0722` edge `-0.0696` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.2127` n `133` status `ready` deltaP `10.0392` edge `0.0106` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1515` n `133` status `ready` deltaP `10.1571` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1253` n `133` status `ready` deltaP `2.3288` edge `0.0043` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2077` n `133` status `ready` deltaP `6.714` edge `0.0356` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2763` n `133` status `ready` deltaP `1.73` edge `-0.0051` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3641` n `133` status `ready` deltaP `5.2517` edge `-0.0201` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.6051` n `133` status `ready` deltaP `-0.2464` edge `0.0091` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.6267` n `133` status `ready` deltaP `2.0115` edge `0.0098` maxDD `-2.618`
- `market_context_high->commodity_1h` score `-0.6433` n `133` status `ready` deltaP `-3.9721` edge `0.0006` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.866` n `133` status `ready` deltaP `0.4199` edge `0.0052` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.3051` n `105` status `ready` deltaP `-3.0506` edge `0.0949` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.3161` n `133` status `ready` deltaP `-0.9511` edge `-0.0599` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.8256` n `133` status `ready` deltaP `-1.8201` edge `0.0586` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-1.9816` n `133` status `ready` deltaP `3.5932` edge `-0.0621` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.2621` n `105` status `ready` deltaP `-4.4891` edge `0.0024` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.3843` n `105` status `ready` deltaP `-8.1994` edge `-0.0572` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.7463` n `133` status `ready` deltaP `-0.1249` edge `-0.2926` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.0045` n `105` status `ready` deltaP `-19.8462` edge `-0.1785` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

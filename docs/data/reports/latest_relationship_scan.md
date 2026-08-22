# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T02:37:29.913179+00:00`
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

- `market_context_high->unknown_1h` score `1.4146` n `133` status `ready` deltaP `9.5854` edge `0.0767` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.9048` n `133` status `ready` deltaP `23.0722` edge `-0.0345` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.2151` n `133` status `ready` deltaP `10.0392` edge `0.0109` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1437` n `133` status `ready` deltaP `10.0074` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1222` n `133` status `ready` deltaP `2.3288` edge `0.0047` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2077` n `133` status `ready` deltaP `6.714` edge `0.0356` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2686` n `133` status `ready` deltaP `1.8797` edge `-0.0051` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3641` n `133` status `ready` deltaP `5.2517` edge `-0.0201` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.5774` n `133` status `ready` deltaP `0.2109` edge `0.0096` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6433` n `133` status `ready` deltaP `-3.9721` edge `0.0006` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6513` n `133` status `ready` deltaP `1.5542` edge `0.0097` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-0.9008` n `133` status `ready` deltaP `0.4199` edge `0.0023` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.3202` n `105` status `ready` deltaP `-3.2242` edge `0.0948` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.3411` n `133` status `ready` deltaP `-0.9511` edge `-0.0631` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.8343` n `133` status `ready` deltaP `-1.9726` edge `0.0585` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-2.0572` n `133` status `ready` deltaP `3.5932` edge `-0.0684` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.2621` n `105` status `ready` deltaP `-4.4891` edge `0.0024` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.3662` n `105` status `ready` deltaP `-7.8522` edge `-0.0572` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.8077` n `133` status `ready` deltaP `-0.2773` edge `-0.2967` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.0433` n `105` status `ready` deltaP `-20.3671` edge `-0.18` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

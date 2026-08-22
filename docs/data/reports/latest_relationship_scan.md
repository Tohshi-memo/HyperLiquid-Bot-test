# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T01:07:31.412289+00:00`
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

- `market_context_high->unknown_1h` score `1.4002` n `133` status `ready` deltaP `9.286` edge `0.0775` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5246` n `133` status `ready` deltaP `23.2246` edge `-0.0672` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1953` n `133` status `ready` deltaP `9.7344` edge `0.0104` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1273` n `133` status `ready` deltaP `9.708` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1089` n `133` status `ready` deltaP `2.6282` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2334` n `133` status `ready` deltaP `6.2649` edge `0.0353` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2756` n `133` status `ready` deltaP `1.73` edge `-0.005` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3633` n `133` status `ready` deltaP `5.2517` edge `-0.02` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.6014` n `133` status `ready` deltaP `2.4689` edge `0.01` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6233` n `133` status `ready` deltaP `-0.5513` edge `0.0088` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6433` n `133` status `ready` deltaP `-3.9721` edge `0.0006` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.8312` n `133` status `ready` deltaP `0.5696` edge `0.0071` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.2575` n `105` status `ready` deltaP `-2.5297` edge `0.0954` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.3005` n `133` status `ready` deltaP `-0.9511` edge `-0.0579` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.8351` n `133` status `ready` deltaP `-1.9726` edge `0.0584` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-1.906` n `133` status `ready` deltaP `3.5932` edge `-0.0558` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.2621` n `105` status `ready` deltaP `-4.4891` edge `0.0024` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.3827` n `105` status `ready` deltaP `-8.1994` edge `-0.057` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.6851` n `133` status `ready` deltaP `-0.1249` edge `-0.2875` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.9634` n `105` status `ready` deltaP `-19.3254` edge `-0.1767` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

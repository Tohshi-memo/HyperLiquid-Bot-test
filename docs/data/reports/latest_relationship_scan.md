# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T00:52:31.259118+00:00`
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

- `market_context_high->unknown_1h` score `1.405` n `133` status `ready` deltaP `9.286` edge `0.0779` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.527` n `133` status `ready` deltaP `23.2246` edge `-0.067` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1945` n `133` status `ready` deltaP `9.7344` edge `0.0103` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1195` n `133` status `ready` deltaP `9.5583` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1011` n `133` status `ready` deltaP `2.7779` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2334` n `133` status `ready` deltaP `6.2649` edge `0.0353` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2756` n `133` status `ready` deltaP `1.73` edge `-0.005` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3626` n `133` status `ready` deltaP `5.2517` edge `-0.0199` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.6014` n `133` status `ready` deltaP `2.4689` edge `0.01` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6233` n `133` status `ready` deltaP `-0.5513` edge `0.0088` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6425` n `133` status `ready` deltaP `-3.9721` edge `0.0007` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.7928` n `133` status `ready` deltaP `0.7193` edge `0.0093` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.24` n `105` status `ready` deltaP `-2.3561` edge `0.0957` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.2865` n `133` status `ready` deltaP `-0.9511` edge `-0.0561` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.8359` n `133` status `ready` deltaP `-1.9726` edge `0.0583` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-1.864` n `133` status `ready` deltaP `3.5932` edge `-0.0523` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.2772` n `105` status `ready` deltaP `-4.6627` edge `0.0023` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.3812` n `105` status `ready` deltaP `-8.1994` edge `-0.0568` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.6455` n `133` status `ready` deltaP `-0.1249` edge `-0.2842` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.9473` n `105` status `ready` deltaP `-19.1518` edge `-0.1758` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T16:52:30.307511+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13774`

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

- `market_context_high->unknown_1h` score `0.564` n `133` status `ready` deltaP `8.0884` edge `0.0158` maxDD `-0.4843`
- `market_context_high->index_1h` score `0.1491` n `133` status `ready` deltaP `10.1571` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.0377` n `124` status `ready` deltaP `6.9286` edge `0.0089` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1004` n `133` status `ready` deltaP `2.7779` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2217` n `133` status `ready` deltaP `6.5643` edge `0.0348` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3347` n `133` status `ready` deltaP `0.6821` edge `-0.0056` maxDD `-0.6822`
- `market_context_high->unknown_4h` score `-0.4823` n `124` status `ready` deltaP `20.9137` edge `-0.1357` maxDD `-0.5133`
- `market_context_high->metal_4h` score `-0.578` n `124` status `ready` deltaP `1.903` edge `-0.0252` maxDD `-1.5942`
- `market_context_high->crypto_alt_1h` score `-0.662` n `133` status `ready` deltaP `0.5696` edge `0.0212` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.662` n `133` status `ready` deltaP `-4.2715` edge `0.0002` maxDD `-1.1941`
- `market_context_high->commodity_24h` score `-0.6788` n `105` status `ready` deltaP `2.6786` edge `0.1089` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.7238` n `124` status `ready` deltaP `0.2409` edge `0.0081` maxDD `-2.5332`
- `market_context_high->commodity_4h` score `-0.7293` n `124` status `ready` deltaP `-2.321` edge `0.007` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-1.1726` n `133` status `ready` deltaP `-0.9511` edge `-0.0415` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.3405` n `124` status `ready` deltaP `3.1323` edge `-0.0056` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.4942` n `124` status `ready` deltaP `-1.9325` edge `0.0617` maxDD `-14.5636`
- `market_context_high->fx_24h` score `-2.7901` n `105` status `ready` deltaP `-10.2183` edge `-0.0034` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.7915` n `124` status `ready` deltaP `0.2311` edge `-0.2154` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.248` n `105` status `ready` deltaP `-6.4633` edge `-0.0513` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.6587` n `105` status `ready` deltaP `-17.9365` edge `-0.1469` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T15:37:36.155004+00:00`
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

- `market_context_high->index_1h` score `0.1101` n `131` status `ready` deltaP `9.5717` edge `0.0034` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.0548` n `119` status `ready` deltaP `7.2133` edge `0.0092` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1152` n `131` status `ready` deltaP `2.4923` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2911` n `131` status `ready` deltaP `5.8292` edge `0.0308` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3652` n `131` status `ready` deltaP `0.2468` edge `-0.0066` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.5521` n `119` status `ready` deltaP `2.1944` edge `-0.0254` maxDD `-1.4673`
- `market_context_high->commodity_24h` score `-0.5758` n `105` status `ready` deltaP `3.5467` edge `0.1117` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-0.6064` n `131` status `ready` deltaP `1.0388` edge `0.0227` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.6083` n `119` status `ready` deltaP `1.7998` edge `0.0095` maxDD `-2.2924`
- `market_context_high->commodity_1h` score `-0.659` n `131` status `ready` deltaP `-4.2887` edge `0.0007` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7031` n `119` status `ready` deltaP `-1.9958` edge `0.0082` maxDD `-2.4692`
- `market_context_high->unknown_1h` score `-0.75` n `131` status `ready` deltaP `8.2084` edge `-0.0945` maxDD `-0.4843`
- `market_context_high->equity_4h` score `-1.0941` n `119` status `ready` deltaP `-0.1704` edge `0.0756` maxDD `-12.5121`
- `market_context_high->crypto_major_1h` score `-1.1313` n `131` status `ready` deltaP `-0.7119` edge `-0.0378` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.7031` n `119` status `ready` deltaP `2.065` edge `-0.0287` maxDD `-5.4926`
- `market_context_high->unknown_4h` score `-2.4661` n `119` status `ready` deltaP `20.236` edge `-0.2965` maxDD `-0.5133`
- `market_context_high->fx_24h` score `-2.8727` n `105` status `ready` deltaP `-11.0863` edge `-0.0045` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-4.1339` n `119` status `ready` deltaP `-0.4638` edge `-0.2393` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2425` n `105` status `ready` deltaP `-6.4633` edge `-0.0506` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.5911` n `105` status `ready` deltaP `-17.4157` edge `-0.1417` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

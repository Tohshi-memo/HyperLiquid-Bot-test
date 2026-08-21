# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T17:07:26.628339+00:00`
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

- `market_context_high->unknown_1h` score `0.5437` n `133` status `ready` deltaP `7.9387` edge `0.0151` maxDD `-0.4843`
- `market_context_high->index_1h` score `0.1491` n `133` status `ready` deltaP `10.1571` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.056` n `125` status `ready` deltaP `7.2963` edge `0.0088` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1082` n `133` status `ready` deltaP `2.6282` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2225` n `133` status `ready` deltaP `6.5643` edge `0.0347` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3441` n `133` status `ready` deltaP `0.5324` edge `-0.0058` maxDD `-0.6822`
- `market_context_high->unknown_4h` score `-0.4962` n `125` status `ready` deltaP `20.8902` edge `-0.1367` maxDD `-0.5133`
- `market_context_high->metal_4h` score `-0.5661` n `125` status `ready` deltaP `2.0732` edge `-0.0248` maxDD `-1.5942`
- `market_context_high->commodity_1h` score `-0.6612` n `133` status `ready` deltaP `-4.2715` edge `0.0003` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.6848` n `133` status `ready` deltaP `0.4199` edge `0.0203` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-0.7011` n `105` status `ready` deltaP `2.505` edge `0.1082` maxDD `-4.666`
- `market_context_high->commodity_4h` score `-0.7208` n `125` status `ready` deltaP `-2.1573` edge `0.007` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.7445` n `125` status `ready` deltaP `-0.0195` edge `0.0078` maxDD `-2.5829`
- `market_context_high->crypto_major_1h` score `-1.1913` n `133` status `ready` deltaP `-1.1008` edge `-0.0429` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.3089` n `125` status `ready` deltaP `3.2122` edge `-0.0035` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.6096` n `125` status `ready` deltaP `-2.2317` edge `0.0588` maxDD `-15.0228`
- `market_context_high->fx_24h` score `-2.7738` n `105` status `ready` deltaP `-10.0447` edge `-0.0032` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.7455` n `125` status `ready` deltaP `0.3561` edge `-0.2124` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2488` n `105` status `ready` deltaP `-6.4633` edge `-0.0514` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.6771` n `105` status `ready` deltaP `-18.1101` edge `-0.1481` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

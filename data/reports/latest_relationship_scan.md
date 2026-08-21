# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T17:37:25.861249+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13790`

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

- `market_context_high->unknown_1h` score `0.5701` n `133` status `ready` deltaP `7.9387` edge `0.0173` maxDD `-0.4843`
- `market_context_high->index_1h` score `0.1569` n `133` status `ready` deltaP `10.3068` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.0957` n `127` status `ready` deltaP `8.0144` edge `0.0091` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1245` n `133` status `ready` deltaP `2.3288` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2202` n `133` status `ready` deltaP `6.5643` edge `0.035` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.362` n `133` status `ready` deltaP `0.233` edge `-0.0061` maxDD `-0.6822`
- `market_context_high->unknown_4h` score `-0.5436` n `127` status `ready` deltaP `20.8374` edge `-0.1403` maxDD `-0.5133`
- `market_context_high->metal_4h` score `-0.5476` n `127` status `ready` deltaP `2.3982` edge `-0.0246` maxDD `-1.5942`
- `market_context_high->crypto_alt_1h` score `-0.6512` n `133` status `ready` deltaP `0.7193` edge `0.0211` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.662` n `133` status `ready` deltaP `-4.2715` edge `0.0002` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7069` n `127` status `ready` deltaP `-1.8449` edge `0.0067` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.7386` n `127` status `ready` deltaP `0.114` edge `0.0081` maxDD `-2.618`
- `market_context_high->commodity_24h` score `-0.7469` n `105` status `ready` deltaP `2.1578` edge `0.1067` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.1913` n `133` status `ready` deltaP `-1.1008` edge `-0.0429` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.2344` n `127` status `ready` deltaP `3.5133` edge `0.0007` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.7833` n `127` status `ready` deltaP `-2.8087` edge `0.0556` maxDD `-15.574`
- `market_context_high->fx_24h` score `-2.7412` n `105` status `ready` deltaP `-9.6974` edge `-0.0028` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.7121` n `127` status `ready` deltaP `0.5929` edge `-0.2112` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2503` n `105` status `ready` deltaP `-6.4633` edge `-0.0516` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.7048` n `105` status `ready` deltaP `-18.2837` edge `-0.1505` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

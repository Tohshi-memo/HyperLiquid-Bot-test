# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T22:37:26.089986+00:00`
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

- `market_context_high->unknown_1h` score `1.3655` n `133` status `ready` deltaP `8.9866` edge `0.0766` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.3924` n `133` status `ready` deltaP `22.1575` edge `-0.0711` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1912` n `133` status `ready` deltaP `10.9056` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1399` n `133` status `ready` deltaP `8.8197` edge `0.0094` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0926` n `133` status `ready` deltaP `2.9276` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2163` n `133` status `ready` deltaP `6.5643` edge `0.0355` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3254` n `133` status `ready` deltaP `0.8318` edge `-0.0054` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.391` n `133` status `ready` deltaP `4.7943` edge `-0.0205` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.5832` n `133` status `ready` deltaP `2.7737` edge `0.0103` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.5885` n `133` status `ready` deltaP `0.0584` edge `0.0092` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6682` n `133` status `ready` deltaP `-4.4212` edge `0.0004` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.7952` n `133` status `ready` deltaP `0.5696` edge `0.0101` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.0682` n `105` status `ready` deltaP `-0.7936` edge `0.0996` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.3566` n `133` status `ready` deltaP `-1.5499` edge `-0.0611` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.434` n `133` status `ready` deltaP `3.8981` edge `-0.0185` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8161` n `133` status `ready` deltaP `-1.6677` edge `0.0588` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.419` n `105` status `ready` deltaP `-6.2252` edge `0.0009` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-4.1811` n `133` status `ready` deltaP `-0.1249` edge `-0.2455` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.3408` n `105` status `ready` deltaP `-7.6786` edge `-0.0551` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.8551` n `105` status `ready` deltaP `-18.4574` edge `-0.1686` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

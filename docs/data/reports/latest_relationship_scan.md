# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T21:11:03.924535+00:00`
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

- `market_context_high->unknown_1h` score `1.2216` n `133` status `ready` deltaP `8.5375` edge `0.0676` maxDD `-0.4843`
- `market_context_high->index_1h` score `0.2067` n `133` status `ready` deltaP `11.205` edge `0.0049` maxDD `-0.9144`
- `market_context_high->unknown_4h` score `0.1878` n `133` status `ready` deltaP `21.7002` edge `-0.0851` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1653` n `133` status `ready` deltaP `9.277` edge `0.0096` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0926` n `133` status `ready` deltaP `2.9276` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2155` n `133` status `ready` deltaP `6.5643` edge `0.0356` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3339` n `133` status `ready` deltaP `0.6821` edge `-0.0055` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.4464` n `133` status `ready` deltaP `3.8797` edge `-0.0215` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.5753` n `133` status `ready` deltaP `2.9262` edge `0.0103` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.628` n `133` status `ready` deltaP `-0.5513` edge `0.0082` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.6692` n `133` status `ready` deltaP `0.7193` edge `0.0196` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.6776` n `133` status `ready` deltaP `-4.5709` edge `0.0002` maxDD `-1.1941`
- `market_context_high->commodity_24h` score `-0.9597` n `105` status `ready` deltaP `0.248` edge `0.1017` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.2342` n `133` status `ready` deltaP `-1.5499` edge `-0.0454` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.3032` n `133` status `ready` deltaP `3.8981` edge `-0.0076` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8114` n `133` status `ready` deltaP `-1.6677` edge `0.0594` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.5132` n `105` status `ready` deltaP `-7.2669` edge `0.0` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.9435` n `133` status `ready` deltaP `-0.1249` edge `-0.2257` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2773` n `105` status `ready` deltaP `-6.6369` edge `-0.0539` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.8145` n `105` status `ready` deltaP `-18.4574` edge `-0.1634` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

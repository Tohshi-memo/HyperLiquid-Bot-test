# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T20:22:28.323570+00:00`
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

- `market_context_high->unknown_1h` score `1.2156` n `133` status `ready` deltaP `8.5375` edge `0.0671` maxDD `-0.4843`
- `market_context_high->index_1h` score `0.1989` n `133` status `ready` deltaP `11.0553` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1906` n `133` status `ready` deltaP `9.7344` edge `0.0098` maxDD `-0.3539`
- `market_context_high->unknown_4h` score `0.0444` n `133` status `ready` deltaP `21.2429` edge `-0.094` maxDD `-0.5133`
- `market_context_high->fx_1h` score `-0.1004` n `133` status `ready` deltaP `2.7779` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2147` n `133` status `ready` deltaP `6.5643` edge `0.0357` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3596` n `133` status `ready` deltaP `0.233` edge `-0.0058` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.4772` n `133` status `ready` deltaP `3.4224` edge `-0.0224` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.5768` n `133` status `ready` deltaP `2.9262` edge `0.0101` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-0.6032` n `133` status `ready` deltaP `0.869` edge `0.0241` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6564` n `133` status `ready` deltaP `-1.0086` edge `0.0076` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6682` n `133` status `ready` deltaP `-4.4212` edge `0.0004` maxDD `-1.1941`
- `market_context_high->commodity_24h` score `-0.9374` n `105` status `ready` deltaP `0.4217` edge `0.1024` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.1788` n `133` status `ready` deltaP `-1.1008` edge `-0.0413` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.3516` n `133` status `ready` deltaP `3.5932` edge `-0.0096` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8281` n `133` status `ready` deltaP `-1.9726` edge `0.0593` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.5608` n `105` status `ready` deltaP `-7.7877` edge `-0.0005` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.9653` n `133` status `ready` deltaP `-0.2773` edge `-0.2265` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2636` n `105` status `ready` deltaP `-6.4633` edge `-0.0533` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.7958` n `105` status `ready` deltaP `-18.4574` edge `-0.161` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

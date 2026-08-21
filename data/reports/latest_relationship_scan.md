# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T20:44:46.973319+00:00`
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

- `market_context_high->unknown_1h` score `1.2192` n `133` status `ready` deltaP `8.5375` edge `0.0674` maxDD `-0.4843`
- `market_context_high->index_1h` score `0.1989` n `133` status `ready` deltaP `11.0553` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1827` n `133` status `ready` deltaP `9.5819` edge `0.0098` maxDD `-0.3539`
- `market_context_high->unknown_4h` score `0.0794` n `133` status `ready` deltaP `21.3953` edge `-0.0921` maxDD `-0.5133`
- `market_context_high->fx_1h` score `-0.0918` n `133` status `ready` deltaP `2.9276` edge `0.0046` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2155` n `133` status `ready` deltaP `6.5643` edge `0.0356` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3519` n `133` status `ready` deltaP `0.3827` edge `-0.0058` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.4677` n `133` status `ready` deltaP `3.5748` edge `-0.0222` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.576` n `133` status `ready` deltaP `2.9262` edge `0.0102` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-0.6188` n `133` status `ready` deltaP `0.869` edge `0.0228` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6477` n `133` status `ready` deltaP `-0.8562` edge `0.0077` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6768` n `133` status `ready` deltaP `-4.5709` edge `0.0003` maxDD `-1.1941`
- `market_context_high->commodity_24h` score `-0.9549` n `105` status `ready` deltaP `0.248` edge `0.1021` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.1952` n `133` status `ready` deltaP `-1.2505` edge `-0.0424` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.331` n `133` status `ready` deltaP `3.7457` edge `-0.0089` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8201` n `133` status `ready` deltaP `-1.8201` edge `0.0593` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.5445` n `105` status `ready` deltaP `-7.6141` edge `-0.0003` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.9617` n `133` status `ready` deltaP `-0.2773` edge `-0.2262` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2652` n `105` status `ready` deltaP `-6.4633` edge `-0.0535` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.802` n `105` status `ready` deltaP `-18.4574` edge `-0.1618` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

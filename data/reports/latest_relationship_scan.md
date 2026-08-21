# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T20:09:46.362571+00:00`
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

- `market_context_high->unknown_1h` score `1.2168` n `133` status `ready` deltaP `8.5375` edge `0.0672` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.1985` n `133` status `ready` deltaP `9.8868` edge `0.0098` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1904` n `133` status `ready` deltaP `10.9056` edge `0.0048` maxDD `-0.9144`
- `market_context_high->unknown_4h` score `-0.0182` n `133` status `ready` deltaP `21.0904` edge `-0.0982` maxDD `-0.5133`
- `market_context_high->fx_1h` score `-0.1082` n `133` status `ready` deltaP `2.6282` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2147` n `133` status `ready` deltaP `6.5643` edge `0.0357` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3596` n `133` status `ready` deltaP `0.233` edge `-0.0058` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.4859` n `133` status `ready` deltaP `3.27` edge `-0.0225` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.5855` n `133` status `ready` deltaP `2.7737` edge `0.01` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-0.5888` n `133` status `ready` deltaP `0.869` edge `0.0253` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6572` n `133` status `ready` deltaP `-1.0086` edge `0.0075` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6768` n `133` status `ready` deltaP `-4.5709` edge `0.0003` maxDD `-1.1941`
- `market_context_high->commodity_24h` score `-0.9362` n `105` status `ready` deltaP `0.4217` edge `0.1025` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.1648` n `133` status `ready` deltaP `-0.9511` edge `-0.0405` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.3722` n `133` status `ready` deltaP `3.4408` edge `-0.0103` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8375` n `133` status `ready` deltaP `-2.125` edge `0.0591` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.5771` n `105` status `ready` deltaP `-7.9613` edge `-0.0007` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.9689` n `133` status `ready` deltaP `-0.2773` edge `-0.2268` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2628` n `105` status `ready` deltaP `-6.4633` edge `-0.0532` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.7888` n `105` status `ready` deltaP `-18.4574` edge `-0.1601` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

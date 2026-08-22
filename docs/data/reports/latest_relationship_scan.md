# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T10:44:49.155017+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `market_context_high->unknown_1h` score `1.0794` n `141` status `ready` deltaP `7.346` edge `0.0637` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.3635` n `133` status `ready` deltaP `19.2612` edge `-0.0542` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0876` n `133` status `ready` deltaP `7.7527` edge `0.0098` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0212` n `141` status `ready` deltaP `7.6676` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.058` n `141` status `ready` deltaP `3.562` edge `0.0047` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.226` n `141` status `ready` deltaP `2.5927` edge `-0.0044` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.2646` n `133` status `ready` deltaP `6.7761` edge `-0.0175` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3099` n `141` status `ready` deltaP `4.973` edge `0.0341` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.5856` n `133` status `ready` deltaP `2.6213` edge `0.011` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6672` n `133` status `ready` deltaP `-0.8562` edge `0.0052` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7665` n `141` status `ready` deltaP `-5.9965` edge `-0.0017` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.5679` n `133` status `ready` deltaP `5.2701` edge `-0.0388` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.6818` n `133` status `ready` deltaP `-0.6006` edge `0.0689` maxDD `-16.1079`
- `market_context_high->commodity_24h` score `-1.7177` n `115` status `ready` deltaP `-4.5622` edge `0.0706` maxDD `-4.666`
- `market_context_high->fx_24h` score `-2.1279` n `115` status `ready` deltaP `-3.2458` edge `0.0053` maxDD `-2.2121`
- `market_context_high->crypto_alt_1h` score `-2.263` n `141` status `ready` deltaP `-2.2837` edge `-0.0325` maxDD `-7.2689`
- `market_context_high->crypto_major_1h` score `-3.2947` n `141` status `ready` deltaP `-4.4039` edge `-0.1061` maxDD `-7.1276`
- `market_context_high->index_24h` score `-4.341` n `115` status `ready` deltaP `-6.8675` edge `-0.0483` maxDD `-19.6627`
- `market_context_high->crypto_major_4h` score `-5.0331` n `133` status `ready` deltaP `-1.0395` edge `-0.3104` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.2856` n `115` status `ready` deltaP `-22.657` edge `-0.1958` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

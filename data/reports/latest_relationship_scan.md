# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T10:37:25.035912+00:00`
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

- `market_context_high->unknown_1h` score `1.0251` n `141` status `ready` deltaP `6.7865` edge `0.0629` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.3647` n `133` status `ready` deltaP `19.2612` edge `-0.0541` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0876` n `133` status `ready` deltaP `7.7527` edge `0.0098` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0212` n `141` status `ready` deltaP `7.6676` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0588` n `141` status `ready` deltaP `3.562` edge `0.0046` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.226` n `141` status `ready` deltaP `2.5927` edge `-0.0044` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.2646` n `133` status `ready` deltaP `6.7761` edge `-0.0175` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3123` n `141` status `ready` deltaP `4.973` edge `0.0338` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.5856` n `133` status `ready` deltaP `2.6213` edge `0.011` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6672` n `133` status `ready` deltaP `-0.8562` edge `0.0052` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7673` n `141` status `ready` deltaP `-5.9965` edge `-0.0018` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.5619` n `133` status `ready` deltaP `5.2701` edge `-0.0383` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.6811` n `133` status `ready` deltaP `-0.6006` edge `0.069` maxDD `-16.1079`
- `market_context_high->commodity_24h` score `-1.7165` n `115` status `ready` deltaP `-4.5622` edge `0.0707` maxDD `-4.666`
- `market_context_high->fx_24h` score `-2.1279` n `115` status `ready` deltaP `-3.2458` edge `0.0053` maxDD `-2.2121`
- `market_context_high->crypto_alt_1h` score `-2.3409` n `141` status `ready` deltaP `-2.2837` edge `-0.0345` maxDD `-7.6283`
- `market_context_high->crypto_major_1h` score `-3.3776` n `141` status `ready` deltaP `-4.4039` edge `-0.1082` maxDD `-7.5125`
- `market_context_high->index_24h` score `-4.3408` n `115` status `ready` deltaP `-6.8675` edge `-0.0483` maxDD `-19.6613`
- `market_context_high->crypto_major_4h` score `-5.0259` n `133` status `ready` deltaP `-1.0395` edge `-0.3098` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.2856` n `115` status `ready` deltaP `-22.657` edge `-0.1958` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

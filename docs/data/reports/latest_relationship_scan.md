# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T23:10:21.072089+00:00`
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

- `market_context_high->unknown_1h` score `1.3847` n `133` status `ready` deltaP `8.9866` edge `0.0782` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.407` n `133` status `ready` deltaP `22.31` edge `-0.0709` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1748` n `133` status `ready` deltaP `10.6062` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1486` n `133` status `ready` deltaP `8.9722` edge `0.0095` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0856` n `133` status `ready` deltaP `3.0773` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2163` n `133` status `ready` deltaP `6.5643` edge `0.0355` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3098` n `133` status `ready` deltaP `1.1312` edge `-0.0054` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3728` n `133` status `ready` deltaP `5.0992` edge `-0.0202` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.5972` n `133` status `ready` deltaP `-0.094` edge `0.0091` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.5998` n `133` status `ready` deltaP `2.4689` edge `0.0102` maxDD `-2.618`
- `market_context_high->commodity_1h` score `-0.6768` n `133` status `ready` deltaP `-4.5709` edge `0.0003` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.7988` n `133` status `ready` deltaP `0.5696` edge `0.0098` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.108` n `105` status `ready` deltaP `-1.1408` edge `0.0986` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.3543` n `133` status `ready` deltaP `-1.4002` edge `-0.0618` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.5288` n `133` status `ready` deltaP `3.8981` edge `-0.0264` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8351` n `133` status `ready` deltaP `-1.9726` edge `0.0584` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.3865` n `105` status `ready` deltaP `-5.878` edge `0.0013` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-4.3143` n `133` status `ready` deltaP `-0.1249` edge `-0.2566` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.3628` n `105` status `ready` deltaP `-8.0258` edge `-0.0556` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.8668` n `105` status `ready` deltaP `-18.4574` edge `-0.1701` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

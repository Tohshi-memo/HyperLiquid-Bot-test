# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T15:07:31.079818+00:00`
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

- `market_context_high->index_1h` score `0.0912` n `129` status `ready` deltaP `9.2675` edge `0.003` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.0883` n `117` status `ready` deltaP `7.8422` edge `0.0093` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1229` n `129` status `ready` deltaP `2.3604` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3233` n `129` status `ready` deltaP `5.525` edge `0.0287` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3543` n `129` status `ready` deltaP `0.1149` edge `-0.006` maxDD `-0.5483`
- `market_context_high->metal_4h` score `-0.4606` n `117` status `ready` deltaP `3.2143` edge `-0.0229` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.5312` n `105` status `ready` deltaP `3.8939` edge `0.1131` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.5366` n `117` status `ready` deltaP `2.7192` edge `0.0107` maxDD `-2.1433`
- `market_context_high->unknown_1h` score `-0.6713` n `129` status `ready` deltaP `8.3369` edge `-0.0888` maxDD `-0.4843`
- `market_context_high->commodity_1h` score `-0.687` n `129` status `ready` deltaP `-4.7823` edge `0.0004` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.7159` n `129` status `ready` deltaP `0.4352` edge `0.0176` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7334` n `117` status `ready` deltaP `-2.5185` edge `0.0078` maxDD `-2.4692`
- `market_context_high->equity_4h` score `-0.8582` n `117` status `ready` deltaP `0.8352` edge `0.0853` maxDD `-11.4048`
- `market_context_high->crypto_major_1h` score `-1.2123` n `129` status `ready` deltaP `-1.3983` edge `-0.0436` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.9605` n `117` status `ready` deltaP `1.5479` edge `-0.0467` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.9065` n `105` status `ready` deltaP `-11.4336` edge `-0.005` maxDD `-2.2121`
- `market_context_high->unknown_4h` score `-3.1467` n `117` status `ready` deltaP `19.9487` edge `-0.3513` maxDD `-0.5133`
- `market_context_high->index_24h` score `-4.2206` n `105` status `ready` deltaP `-6.1161` edge `-0.0501` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.3055` n `117` status `ready` deltaP `-0.9289` edge `-0.2505` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.5688` n `105` status `ready` deltaP `-17.2421` edge `-0.14` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

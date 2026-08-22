# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T09:37:29.404724+00:00`
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

- `market_context_high->unknown_1h` score `1.2008` n `137` status `ready` deltaP `7.5725` edge `0.0723` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.4457` n `133` status `ready` deltaP `19.7185` edge `-0.0504` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0955` n `133` status `ready` deltaP `7.9051` edge `0.0098` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0578` n `137` status `ready` deltaP `8.357` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1199` n `137` status `ready` deltaP `2.3865` edge `0.0046` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2244` n `137` status `ready` deltaP `6.2426` edge `0.0366` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.2392` n `133` status `ready` deltaP `7.2334` edge `-0.0173` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.2521` n `137` status `ready` deltaP `2.1056` edge `-0.0045` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6197` n `133` status `ready` deltaP `2.0115` edge `0.0107` maxDD `-2.618`
- `market_context_high->commodity_1h` score `-0.7004` n `137` status `ready` deltaP `-4.8002` edge `-0.0012` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.702` n `133` status `ready` deltaP `-1.466` edge `0.0048` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-1.3069` n `137` status `ready` deltaP `-0.7561` edge `-0.007` maxDD `-3.7493`
- `market_context_high->commodity_24h` score `-1.5687` n `111` status `ready` deltaP `-4.1103` edge `0.08` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-1.6991` n `133` status `ready` deltaP `4.9652` edge `-0.0477` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.7221` n `133` status `ready` deltaP `-1.2104` edge `0.0678` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.2933` n `111` status `ready` deltaP `-5.0582` edge `0.0036` maxDD `-2.2121`
- `market_context_high->crypto_major_1h` score `-2.4628` n `137` status `ready` deltaP `-3.0213` edge `-0.0826` maxDD `-4.1996`
- `market_context_high->index_24h` score `-4.2687` n `111` status `ready` deltaP `-5.9638` edge `-0.0504` maxDD `-19.2358`
- `market_context_high->metal_24h` score `-5.2054` n `111` status `ready` deltaP `-21.5653` edge `-0.1928` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.2103` n `133` status `ready` deltaP `-1.6493` edge `-0.3211` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

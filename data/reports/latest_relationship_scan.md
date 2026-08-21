# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T23:22:28.600356+00:00`
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

- `market_context_high->unknown_1h` score `1.4015` n `133` status `ready` deltaP `9.1363` edge `0.0786` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.424` n `133` status `ready` deltaP `22.4624` edge `-0.0705` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.167` n `133` status `ready` deltaP `10.4565` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1581` n `133` status `ready` deltaP `9.1246` edge `0.0097` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0856` n `133` status `ready` deltaP `3.0773` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2155` n `133` status `ready` deltaP `6.5643` edge `0.0356` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.309` n `133` status `ready` deltaP `1.1312` edge `-0.0053` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3641` n `133` status `ready` deltaP `5.2517` edge `-0.0201` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.5972` n `133` status `ready` deltaP `-0.094` edge `0.0091` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.5998` n `133` status `ready` deltaP `2.4689` edge `0.0102` maxDD `-2.618`
- `market_context_high->commodity_1h` score `-0.6682` n `133` status `ready` deltaP `-4.4212` edge `0.0004` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.8012` n `133` status `ready` deltaP `0.5696` edge `0.0096` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.1267` n `105` status `ready` deltaP `-1.3145` edge `0.0982` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.3582` n `133` status `ready` deltaP `-1.4002` edge `-0.0623` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.5816` n `133` status `ready` deltaP `3.8981` edge `-0.0308` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8359` n `133` status `ready` deltaP `-1.9726` edge `0.0583` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.3702` n `105` status `ready` deltaP `-5.7044` edge `0.0015` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.3734` n `105` status `ready` deltaP `-8.1994` edge `-0.0558` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.3827` n `133` status `ready` deltaP `-0.1249` edge `-0.2623` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.8722` n `105` status `ready` deltaP `-18.4574` edge `-0.1708` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T19:52:42.401308+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `market_context_high->unknown_1h` score `1.464` n `149` status `ready` deltaP `6.1086` edge `0.104` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8619` n `149` status `ready` deltaP `18.7418` edge `-0.0092` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0986` n `149` status `ready` deltaP `8.0547` edge `0.0092` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0204` n `149` status `ready` deltaP `6.8973` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1277` n `149` status `ready` deltaP `2.2666` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3206` n `149` status `ready` deltaP `5.0235` edge `0.0324` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3405` n `149` status `ready` deltaP `0.4803` edge `-0.005` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3435` n `149` status `ready` deltaP `7.5401` edge `-0.0173` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.5293` n `149` status `ready` deltaP `3.6299` edge `0.0115` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8952` n `149` status `ready` deltaP `-4.3859` edge `-0.0005` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.1134` n `149` status `ready` deltaP `-8.1722` edge `-0.0025` maxDD `-1.1941`
- `market_context_high->fx_24h` score `-1.1584` n `133` status `ready` deltaP `0.2663` edge `0.0107` maxDD `-2.2121`
- `market_context_high->equity_4h` score `-1.6894` n `149` status `ready` deltaP `-0.6701` edge `0.0695` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.1008` n `133` status `ready` deltaP `-4.2058` edge `0.0363` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.5053` n `149` status `ready` deltaP `-2.3841` edge `-0.0434` maxDD `-7.9582`
- `market_context_high->crypto_alt_4h` score `-2.6713` n `149` status `ready` deltaP `2.2364` edge `-0.0907` maxDD `-7.0785`
- `market_context_high->crypto_major_1h` score `-3.64` n `149` status `ready` deltaP `-5.5077` edge `-0.1189` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.3262` n `133` status `ready` deltaP `-5.8676` edge `-0.0348` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.3612` n `133` status `ready` deltaP `-22.9415` edge `-0.2036` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.8446` n `149` status `ready` deltaP `-0.9985` edge `-0.3474` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

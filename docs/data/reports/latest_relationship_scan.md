# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T16:59:08.583528+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14818`

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

- `market_context_high->unknown_1h` score `1.5707` n `149` status `ready` deltaP `6.8571` edge `0.1079` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.9351` n `148` status `ready` deltaP `18.6511` edge `-0.0025` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1026` n `148` status `ready` deltaP `8.0875` edge `0.0095` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0437` n `149` status `ready` deltaP `6.4482` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1192` n `149` status `ready` deltaP `2.4163` edge `0.0045` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2986` n `148` status `ready` deltaP `8.071` edge `-0.0171` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3291` n `149` status `ready` deltaP `4.8738` edge `0.0323` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3717` n `149` status `ready` deltaP `-0.1185` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.4853` n `148` status `ready` deltaP `4.4455` edge `0.0117` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8483` n `148` status `ready` deltaP `-3.5432` edge `-0.0001` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-1.0505` n `133` status `ready` deltaP `2.176` edge `0.0118` maxDD `-2.2121`
- `market_context_high->commodity_1h` score `-1.1399` n `149` status `ready` deltaP `-8.6213` edge `-0.0029` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.702` n `148` status `ready` deltaP `-0.9352` edge `0.0694` maxDD `-16.1768`
- `market_context_high->commodity_24h` score `-2.2721` n `133` status `ready` deltaP `-5.9419` edge `0.0336` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-2.3673` n `148` status `ready` deltaP `3.6956` edge `-0.0751` maxDD `-7.0785`
- `market_context_high->crypto_alt_1h` score `-2.4525` n `149` status `ready` deltaP `-2.0847` edge `-0.041` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.5165` n `149` status `ready` deltaP `-4.7592` edge `-0.1136` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.447` n `133` status `ready` deltaP `-7.9509` edge `-0.0364` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.5` n `133` status `ready` deltaP `-25.0248` edge `-0.2075` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.6049` n `148` status `ready` deltaP `-0.6427` edge `-0.3298` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

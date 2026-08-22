# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T19:12:11.283737+00:00`
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

- `market_context_high->unknown_1h` score `1.5132` n `149` status `ready` deltaP `6.5577` edge `0.1051` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.9351` n `149` status `ready` deltaP `18.7418` edge `-0.0031` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1073` n `149` status `ready` deltaP `8.2071` edge `0.0093` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0126` n `149` status `ready` deltaP `7.047` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1122` n `149` status `ready` deltaP `2.566` edge `0.0044` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.3057` n `149` status `ready` deltaP `7.9974` edge `-0.0172` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3198` n `149` status `ready` deltaP `5.0235` edge `0.0325` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3483` n `149` status `ready` deltaP `0.3306` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5372` n `149` status `ready` deltaP `3.4774` edge `0.0115` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8691` n `149` status `ready` deltaP `-3.9286` edge `-0.0002` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.1289` n `149` status `ready` deltaP `-8.4716` edge `-0.0025` maxDD `-1.1941`
- `market_context_high->fx_24h` score `-1.129` n `133` status `ready` deltaP `0.7871` edge `0.011` maxDD `-2.2121`
- `market_context_high->equity_4h` score `-1.6768` n `149` status `ready` deltaP `-0.5177` edge `0.0701` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.1183` n `133` status `ready` deltaP `-4.3794` edge `0.036` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.5172` n `149` status `ready` deltaP `-2.5338` edge `-0.0434` maxDD `-7.9582`
- `market_context_high->crypto_alt_4h` score `-2.5543` n `149` status `ready` deltaP `2.6937` edge `-0.084` maxDD `-7.0785`
- `market_context_high->crypto_major_1h` score `-3.634` n `149` status `ready` deltaP `-5.5077` edge `-0.1184` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.3564` n `133` status `ready` deltaP `-6.3884` edge `-0.0352` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.3953` n `133` status `ready` deltaP `-23.4623` edge `-0.2045` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.7096` n `149` status `ready` deltaP `-0.5412` edge `-0.3392` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

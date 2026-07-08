# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T17:22:37.392313+00:00`
- Price records: `672`
- Market context records: `6108`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `8.4427` n `30` status `ready` deltaP `35.5208` edge `0.4815` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `8.0629` n `30` status `ready` deltaP `71.7014` edge `0.1939` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1861` n `32` status `ready` deltaP `43.5213` edge `0.0633` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2925` n `32` status `ready` deltaP `27.5449` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.3017` n `32` status `ready` deltaP `14.128` edge `0.1194` maxDD `-2.0691`
- `market_context_high->equity_4h` score `1.0856` n `195` status `ready` deltaP `7.4085` edge `0.1328` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.6891` n `32` status `ready` deltaP `9.2253` edge `0.073` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0633` n `30` status `ready` deltaP `9.2361` edge `0.0337` maxDD `-2.3058`
- `news_risk_high->commodity_24h` score `-0.3129` n `30` status `ready` deltaP `14.9653` edge `-0.1053` maxDD `-0.3101`
- `market_context_high->fx_1h` score `-0.34` n `195` status `ready` deltaP `0.2372` edge `-0.0006` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.606` n `195` status `ready` deltaP `3.847` edge `0.0154` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.6388` n `195` status `ready` deltaP `1.0878` edge `0.0224` maxDD `-4.2573`
- `market_context_high->commodity_1h` score `-0.708` n `195` status `ready` deltaP `-1.54` edge `-0.0041` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7131` n `32` status `ready` deltaP `-2.0958` edge `-0.0277` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7314` n `195` status `ready` deltaP `3.2888` edge `-0.003` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.8458` n `195` status `ready` deltaP `2.3085` edge `0.0226` maxDD `-1.381`
- `market_context_high->crypto_alt_1h` score `-0.8868` n `195` status `ready` deltaP `4.2093` edge `0.0335` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8962` n `195` status `ready` deltaP `4.9133` edge `0.0291` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0992` n `32` status `ready` deltaP `-9.6744` edge `-0.0201` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.2179` n `195` status `ready` deltaP `-2.6071` edge `0.0028` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

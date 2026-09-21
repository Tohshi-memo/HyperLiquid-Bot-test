# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T20:09:22.134847+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9988`

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

- `market_context_high->unknown_4h` score `28.0183` n `58` status `ready` deltaP `1.6874` edge `2.3386` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `15.1104` n `101` status `ready` deltaP `3.1095` edge `1.9243` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `9.6444` n `101` status `ready` deltaP `3.4945` edge `1.2685` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.6831` n `101` status `ready` deltaP `17.3946` edge `0.3119` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `2.9621` n `101` status `ready` deltaP `18.919` edge `0.2465` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6323` n `101` status `ready` deltaP `15.932` edge `0.1597` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `2.0551` n `101` status `ready` deltaP `28.0579` edge `0.207` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.9309` n `101` status `ready` deltaP `17.429` edge `0.097` maxDD `-2.8494`
- `market_context_high->index_24h` score `0.9303` n `42` status `ready` deltaP `-3.2986` edge `0.1784` maxDD `-1.644`
- `market_context_high->equity_1h` score `0.6329` n `58` status `ready` deltaP `4.5117` edge `0.048` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5118` n `101` status `ready` deltaP `13.5501` edge `0.0125` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.4813` n `58` status `ready` deltaP `8.0322` edge `0.0121` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4085` n `58` status `ready` deltaP `9.5241` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3537` n `101` status `ready` deltaP `10.1651` edge `0.0253` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2527` n `101` status `ready` deltaP `14.05` edge `0.0328` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2339` n `58` status `ready` deltaP `5.1002` edge `0.0163` maxDD `-0.1314`
- `market_context_high->equity_24h` score `0.2196` n `42` status `ready` deltaP `-7.2916` edge `0.3565` maxDD `-17.7117`
- `market_context_high->index_4h` score `0.077` n `58` status `ready` deltaP `11.1228` edge `-0.0006` maxDD `-1.0949`
- `market_context_high->metal_24h` score `-0.0612` n `42` status `ready` deltaP `12.8224` edge `-0.0672` maxDD `-0.2042`
- `news_risk_high->fx_1h` score `-0.1405` n `101` status `ready` deltaP `3.8907` edge `0.0067` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

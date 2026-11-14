# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T01:37:26.478127+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10332`

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

- `market_context_high->unknown_24h` score `399.9737` n `75` status `ready` deltaP `2.1944` edge `33.3306` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `35.8366` n `53` status `ready` deltaP `35.0564` edge `2.8233` maxDD `-3.6503`
- `market_context_high->equity_24h` score `27.6029` n `75` status `ready` deltaP `29.5972` edge `2.2571` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.9182` n `75` status `ready` deltaP `47.5834` edge `1.3441` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.0199` n `53` status `ready` deltaP `42.0434` edge `1.8419` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.1678` n `53` status `ready` deltaP `35.9353` edge `0.8041` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.1521` n `53` status `ready` deltaP `40.4514` edge `0.243` maxDD `0.0`
- `market_context_high->index_24h` score `5.4263` n `75` status `ready` deltaP `30.7709` edge `0.2562` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0759` n `53` status `ready` deltaP `48.3779` edge `0.1381` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.7453` n `53` status `ready` deltaP `28.7834` edge `0.2339` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.1637` n `75` status `ready` deltaP `41.3334` edge `0.3474` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.5756` n `53` status `ready` deltaP `18.7634` edge `0.2359` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.5742` n `53` status `ready` deltaP `20.8957` edge `0.3073` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1005` n `53` status `ready` deltaP `28.0833` edge `0.0965` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.314` n `53` status `ready` deltaP `27.0873` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9788` n `53` status `ready` deltaP `19.9839` edge `0.0753` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8681` n `53` status `ready` deltaP `25.5838` edge `0.2328` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.791` n `53` status `ready` deltaP `14.4261` edge `0.584` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1867` n `53` status `ready` deltaP `16.1281` edge `0.0215` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6805` n `53` status `ready` deltaP `17.594` edge `0.0679` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

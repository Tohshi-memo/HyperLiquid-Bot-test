# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T14:07:34.038980+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `372.0086` n `75` status `ready` deltaP `5.1458` edge `30.9805` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.5418` n `53` status `ready` deltaP `31.2369` edge `2.5742` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.3081` n `75` status `ready` deltaP `25.7777` edge `2.008` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `18.3434` n `75` status `ready` deltaP `51.4028` edge `1.4374` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.2201` n `53` status `ready` deltaP `42.217` edge `1.7382` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.1389` n `53` status `ready` deltaP `33.6487` edge `0.7336` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.6647` n `53` status `ready` deltaP `36.4583` edge `0.229` maxDD `0.0`
- `market_context_high->index_24h` score `4.6937` n `75` status `ready` deltaP `24.8681` edge `0.2345` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.5682` n `53` status `ready` deltaP `43.6523` edge `0.1273` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0127` n `53` status `ready` deltaP `22.8806` edge `0.2122` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.7939` n `75` status `ready` deltaP `37.6875` edge `0.3243` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.289` n `53` status `ready` deltaP `17.5658` edge `0.22` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9763` n `53` status `ready` deltaP `27.626` edge `0.0892` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.8873` n `53` status `ready` deltaP `18.6091` edge `0.2653` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.7173` n `53` status `ready` deltaP `18.2455` edge `0.6773` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.084` n `53` status `ready` deltaP `24.6921` edge `0.0345` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9088` n `53` status `ready` deltaP `19.679` edge `0.0715` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7708` n `53` status `ready` deltaP `25.8887` edge `0.2183` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1603` n `53` status `ready` deltaP `15.9784` edge `0.0203` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5372` n `53` status `ready` deltaP `16.3964` edge `0.0575` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

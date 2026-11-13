# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T14:52:28.163201+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10494`

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

- `market_context_high->unknown_24h` score `371.8675` n `75` status `ready` deltaP `4.9722` edge `30.9699` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.5411` n `53` status `ready` deltaP `31.0633` edge `2.5753` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.3075` n `75` status `ready` deltaP `25.6041` edge `2.0091` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `18.1421` n `75` status `ready` deltaP `50.882` edge `1.4241` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.2056` n `53` status `ready` deltaP `42.0434` edge `1.7375` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.0955` n `53` status `ready` deltaP `33.4963` edge `0.731` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.5997` n `53` status `ready` deltaP `36.1111` edge `0.2259` maxDD `0.0`
- `market_context_high->index_24h` score `4.7087` n `75` status `ready` deltaP `25.0417` edge `0.2346` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.5852` n `53` status `ready` deltaP `43.8047` edge `0.1277` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0278` n `53` status `ready` deltaP `23.0542` edge `0.2123` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.8342` n `75` status `ready` deltaP `38.2084` edge `0.326` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3191` n `53` status `ready` deltaP `17.4161` edge `0.2235` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9229` n `53` status `ready` deltaP `27.1687` edge `0.0878` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.8209` n `53` status `ready` deltaP `18.3042` edge `0.2618` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.5865` n `53` status `ready` deltaP `17.7247` edge `0.664` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1032` n `53` status `ready` deltaP `24.8418` edge `0.0351` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.8954` n `53` status `ready` deltaP `19.5266` edge `0.0714` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7168` n `53` status `ready` deltaP `25.5838` edge `0.2134` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1915` n `53` status `ready` deltaP `16.2778` edge `0.0209` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5714` n `53` status `ready` deltaP `16.6958` edge `0.0599` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

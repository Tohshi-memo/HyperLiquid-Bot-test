# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T20:52:30.165928+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `309.7472` n `84` status `ready` deltaP `6.4732` edge `25.7832` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `75.1374` n `94` status `ready` deltaP `8.1053` edge `6.2522` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.8935` n `53` status `ready` deltaP `23.5981` edge `2.3211` maxDD `-3.6503`
- `market_context_high->equity_24h` score `20.8761` n `84` status `ready` deltaP `21.3294` edge `1.6681` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.5652` n `53` status `ready` deltaP `37.1823` edge `1.4314` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.0939` n `53` status `ready` deltaP `31.9719` edge `0.6577` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.4184` n `84` status `ready` deltaP `41.3939` edge `1.2129` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.4003` n `53` status `ready` deltaP `43.2292` edge `0.3285` maxDD `0.0`
- `market_context_high->metal_24h` score `6.2344` n `84` status `ready` deltaP `38.6905` edge `0.3029` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.5958` n `53` status `ready` deltaP `43.6523` edge `0.1296` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.0987` n `84` status `ready` deltaP `23.2887` edge `0.1958` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.6904` n `53` status `ready` deltaP `21.4917` edge `0.1946` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.1366` n `53` status `ready` deltaP `17.5658` edge `0.2073` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9631` n `53` status `ready` deltaP `26.7114` edge `0.0942` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.7886` n `53` status `ready` deltaP `20.2859` edge `0.2459` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2409` n `53` status `ready` deltaP `26.3388` edge `0.0366` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6023` n `53` status `ready` deltaP `17.3924` edge `0.0612` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.4606` n `53` status `ready` deltaP `25.1265` edge `0.1836` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.219` n `53` status `ready` deltaP `16.8766` edge `0.0192` maxDD `-0.4103`
- `news_risk_high->crypto_alt_24h` score `0.9808` n `53` status `ready` deltaP `11.4747` edge `0.4998` maxDD `-29.0448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

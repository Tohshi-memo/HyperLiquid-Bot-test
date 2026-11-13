# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T08:07:35.069562+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11354`

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

- `market_context_high->unknown_24h` score `276.8822` n `81` status `ready` deltaP `6.2115` edge `23.0462` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `75.1684` n `91` status `ready` deltaP `6.4527` edge `6.2658` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `32.1689` n `53` status `ready` deltaP `30.7161` edge `2.5466` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.7249` n `81` status `ready` deltaP `27.8742` edge `1.9452` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.5567` n `53` status `ready` deltaP `41.1753` edge `1.6601` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.3024` n `53` status `ready` deltaP `34.8682` edge `0.7391` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `10.2976` n `81` status `ready` deltaP `48.1482` edge `1.4088` maxDD `-25.4331`
- `market_context_high->metal_24h` score `7.2662` n `81` status `ready` deltaP `44.1937` edge `0.3522` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.2361` n `53` status `ready` deltaP `39.2361` edge `0.2581` maxDD `0.0`
- `market_context_high->index_24h` score `4.5452` n `81` status `ready` deltaP `25.5402` edge `0.218` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.5234` n `53` status `ready` deltaP `43.3474` edge `0.1256` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1171` n `53` status `ready` deltaP `24.0959` edge `0.2128` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.42` n `53` status `ready` deltaP `20.4384` edge `0.2975` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.2014` n `53` status `ready` deltaP `17.5658` edge `0.2127` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1035` n `53` status `ready` deltaP `28.5406` edge `0.0937` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.9439` n `53` status `ready` deltaP `19.2872` edge `0.6994` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.096` n `53` status `ready` deltaP `24.8418` edge `0.0345` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.943` n `53` status `ready` deltaP `26.4985` edge `0.2363` maxDD `-10.1088`
- `news_risk_high->index_4h` score `1.9042` n `53` status `ready` deltaP `19.8315` edge `0.0701` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.1591` n `53` status `ready` deltaP `16.1281` edge `0.0192` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

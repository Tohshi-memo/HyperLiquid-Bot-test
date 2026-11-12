# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T21:07:27.999327+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `310.6868` n `84` status `ready` deltaP `6.4732` edge `25.8615` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `75.3894` n `94` status `ready` deltaP `8.1053` edge `6.2732` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.9962` n `53` status `ready` deltaP `23.7717` edge `2.3285` maxDD `-3.6503`
- `market_context_high->equity_24h` score `20.9788` n `84` status `ready` deltaP `21.503` edge `1.6755` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.6027` n `53` status `ready` deltaP `37.1823` edge `1.4362` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.0807` n `53` status `ready` deltaP `31.9719` edge `0.6566` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.4734` n `84` status `ready` deltaP `41.5675` edge `1.2188` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.3859` n `53` status `ready` deltaP `43.2292` edge `0.3273` maxDD `0.0`
- `market_context_high->metal_24h` score `6.2464` n `84` status `ready` deltaP `38.6905` edge `0.3039` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.5934` n `53` status `ready` deltaP `43.6523` edge `0.1294` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.1186` n `84` status `ready` deltaP `23.4623` edge `0.1963` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.7102` n `53` status `ready` deltaP `21.6653` edge `0.1951` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.1007` n `53` status `ready` deltaP `17.4161` edge `0.2053` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9535` n `53` status `ready` deltaP `26.7114` edge `0.0934` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.7573` n `53` status `ready` deltaP `20.1335` edge `0.2443` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2385` n `53` status `ready` deltaP `26.3388` edge `0.0364` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.5999` n `53` status `ready` deltaP `17.3924` edge `0.061` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.4269` n `53` status `ready` deltaP `24.9741` edge `0.1803` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2022` n `53` status `ready` deltaP `16.7269` edge `0.0188` maxDD `-0.4103`
- `news_risk_high->crypto_alt_24h` score `1.0358` n `53` status `ready` deltaP `11.6483` edge `0.5057` maxDD `-29.0448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

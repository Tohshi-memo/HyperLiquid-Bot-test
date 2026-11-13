# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T06:22:30.033702+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11828`

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

- `market_context_high->unknown_24h` score `270.1753` n `84` status `ready` deltaP `6.2996` edge `22.4867` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `56.334` n `94` status `ready` deltaP `6.7333` edge `4.6944` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.7249` n `53` status `ready` deltaP `29.5008` edge `2.5177` maxDD `-3.6503`
- `market_context_high->equity_24h` score `23.7075` n `84` status `ready` deltaP `27.2321` edge `1.8647` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.1496` n `53` status `ready` deltaP `39.9601` edge `1.616` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `10.1896` n `84` status `ready` deltaP `47.9911` edge `1.396` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `9.9303` n `53` status `ready` deltaP `33.8012` edge `0.7152` maxDD `-7.0416`
- `market_context_high->metal_24h` score `7.1009` n `84` status `ready` deltaP `43.5516` edge `0.3427` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.4665` n `53` status `ready` deltaP `40.4514` edge `0.2692` maxDD `0.0`
- `market_context_high->index_24h` score `4.5002` n `84` status `ready` deltaP `25.8929` edge `0.2119` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.3889` n `53` status `ready` deltaP `42.2803` edge `0.1215` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0919` n `53` status `ready` deltaP `24.0959` edge `0.2107` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.2959` n `53` status `ready` deltaP `19.9811` edge `0.2902` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.2122` n `53` status `ready` deltaP `17.5658` edge `0.2136` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1957` n `53` status `ready` deltaP `29.3028` edge `0.0963` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.752` n `53` status `ready` deltaP `18.0719` edge `0.6829` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0744` n `53` status `ready` deltaP `24.6921` edge `0.0337` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.9444` n `53` status `ready` deltaP `26.346` edge `0.2375` maxDD `-10.1088`
- `news_risk_high->index_4h` score `1.7804` n `53` status `ready` deltaP `18.7644` edge `0.0669` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.1735` n `53` status `ready` deltaP `16.2778` edge `0.0194` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

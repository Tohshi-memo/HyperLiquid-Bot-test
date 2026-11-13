# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T07:37:24.728688+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11824`

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

- `market_context_high->unknown_24h` score `267.215` n `83` status `ready` deltaP `6.271` edge `22.2402` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `68.6651` n `93` status `ready` deltaP `6.6417` edge `5.7226` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `32.0404` n `53` status `ready` deltaP `30.3689` edge `2.5382` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.2288` n `83` status `ready` deltaP `27.9137` edge `1.9036` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.4287` n `53` status `ready` deltaP `40.8281` edge `1.646` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `10.3198` n `83` status `ready` deltaP `48.5149` edge `1.4092` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `10.2168` n `53` status `ready` deltaP `34.5633` edge `0.734` maxDD `-7.0416`
- `market_context_high->metal_24h` score `7.237` n `83` status `ready` deltaP `44.2331` edge `0.3495` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.2963` n `53` status `ready` deltaP `39.5833` edge `0.2608` maxDD `0.0`
- `market_context_high->index_24h` score `4.5282` n `83` status `ready` deltaP `25.7781` edge `0.215` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.4846` n `53` status `ready` deltaP `43.0425` edge `0.1244` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1087` n `53` status `ready` deltaP `24.0959` edge `0.2121` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.4164` n `53` status `ready` deltaP `20.4384` edge `0.2972` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.1751` n `53` status `ready` deltaP `17.4161` edge `0.2115` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1193` n `53` status `ready` deltaP `28.6931` edge `0.094` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.8892` n `53` status `ready` deltaP `18.94` edge `0.6947` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0756` n `53` status `ready` deltaP `24.6921` edge `0.0338` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.9656` n `53` status `ready` deltaP `26.4985` edge `0.2392` maxDD `-10.1088`
- `news_risk_high->index_4h` score `1.8714` n `53` status `ready` deltaP `19.5266` edge `0.0694` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.1459` n `53` status `ready` deltaP `15.9784` edge `0.0191` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

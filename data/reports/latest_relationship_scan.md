# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T05:22:26.813628+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3552`

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

- `news_risk_high->unknown_1h` score `3218.9185` n `31` status `ready` deltaP `1.6322` edge `268.2499` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3187.1542` n `31` status `ready` deltaP `3.7864` edge `265.5766` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `23.3008` n `31` status `ready` deltaP `32.4653` edge `1.7253` maxDD `0.0`
- `news_risk_high->equity_24h` score `20.8304` n `31` status `ready` deltaP `31.9444` edge `1.5229` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.7246` n `31` status `ready` deltaP `31.5972` edge `1.2664` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.2162` n `31` status `ready` deltaP `23.4067` edge `0.699` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.3412` n `31` status `ready` deltaP `33.1088` edge `0.4391` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.9545` n `31` status `ready` deltaP `16.4732` edge `0.7953` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.7612` n `31` status `ready` deltaP `19.7077` edge `0.3762` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.7419` n `31` status `ready` deltaP `39.6282` edge `0.1438` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.691` n `31` status `ready` deltaP `33.5069` edge `0.0842` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7268` n `31` status `ready` deltaP `31.432` edge `0.0437` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.6856` n `31` status `ready` deltaP `16.5443` edge `0.1322` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3847` n `31` status `ready` deltaP `28.8488` edge `0.0149` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0823` n `31` status `ready` deltaP `6.8669` edge `0.2673` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8746` n `31` status `ready` deltaP `10.0106` edge `0.2093` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1839` n `31` status `ready` deltaP `25.5408` edge `0.0094` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4685` n `31` status `ready` deltaP `12.5098` edge `0.0324` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0019` n `31` status `ready` deltaP `6.6925` edge `-0.0046` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6276` n `31` status `ready` deltaP `-4.6069` edge `0.0046` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

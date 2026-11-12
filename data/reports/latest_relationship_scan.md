# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T22:22:37.282477+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `311.1932` n `84` status `ready` deltaP `6.4732` edge `25.9037` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `75.8226` n `94` status `ready` deltaP `8.1053` edge `6.3093` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `29.5492` n `53` status `ready` deltaP `24.6397` edge `2.3688` maxDD `-3.6503`
- `market_context_high->equity_24h` score `21.5318` n `84` status `ready` deltaP `22.371` edge `1.7158` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.7669` n `53` status `ready` deltaP `37.3559` edge `1.4561` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.2027` n `53` status `ready` deltaP `32.5816` edge `0.6627` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.7299` n `84` status `ready` deltaP `42.4355` edge `1.2459` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.3067` n `53` status `ready` deltaP `43.2292` edge `0.3207` maxDD `0.0`
- `market_context_high->metal_24h` score `6.3287` n `84` status `ready` deltaP `38.8641` edge `0.3096` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.619` n `53` status `ready` deltaP `43.9571` edge `0.1295` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.2312` n `84` status `ready` deltaP `24.3304` edge `0.1999` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.8229` n `53` status `ready` deltaP `22.5334` edge `0.1987` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.0287` n `53` status `ready` deltaP `17.1167` edge `0.2013` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9247` n `53` status `ready` deltaP `26.7114` edge `0.091` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.6823` n `53` status `ready` deltaP `19.6762` edge `0.2411` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2074` n `53` status `ready` deltaP `26.0394` edge `0.0358` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6377` n `53` status `ready` deltaP `17.8497` edge `0.0611` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.343` n `53` status `ready` deltaP `24.5168` edge `0.1726` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.2923` n `53` status `ready` deltaP `12.5163` edge `0.5328` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1543` n `53` status `ready` deltaP `16.2778` edge `0.0178` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

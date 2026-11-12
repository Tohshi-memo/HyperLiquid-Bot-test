# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T23:07:29.297732+00:00`
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

- `market_context_high->unknown_24h` score `307.9213` n `84` status `ready` deltaP `6.2996` edge `25.6322` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `75.8994` n `94` status `ready` deltaP `8.1053` edge `6.3157` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `29.8165` n `53` status `ready` deltaP `25.1606` edge `2.3876` maxDD `-3.6503`
- `market_context_high->equity_24h` score `21.7991` n `84` status `ready` deltaP `22.8919` edge `1.7346` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.8462` n `53` status `ready` deltaP `37.5295` edge `1.4651` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.2677` n `53` status `ready` deltaP `32.7341` edge `0.6671` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.8576` n `84` status `ready` deltaP `42.9564` edge `1.2588` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.2527` n `53` status `ready` deltaP `43.2292` edge `0.3162` maxDD `0.0`
- `market_context_high->metal_24h` score `6.4008` n `84` status `ready` deltaP `39.2113` edge `0.3133` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6324` n `53` status `ready` deltaP `44.1096` edge `0.1296` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.2842` n `84` status `ready` deltaP `24.6776` edge `0.202` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.8759` n `53` status `ready` deltaP `22.8806` edge `0.2008` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `2.9736` n `53` status `ready` deltaP `16.8173` edge `0.1987` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9151` n `53` status `ready` deltaP `26.7114` edge `0.0902` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.6763` n `53` status `ready` deltaP `19.6762` edge `0.2406` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.181` n `53` status `ready` deltaP `25.74` edge `0.0356` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6595` n `53` status `ready` deltaP `18.0022` edge `0.0619` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.42` n `53` status `ready` deltaP `13.0372` edge `0.5457` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.3329` n `53` status `ready` deltaP `24.5168` edge `0.1713` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1411` n `53` status `ready` deltaP `16.1281` edge `0.0177` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

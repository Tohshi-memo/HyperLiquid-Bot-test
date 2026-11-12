# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T23:22:28.486956+00:00`
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

- `market_context_high->unknown_24h` score `306.8485` n `84` status `ready` deltaP `6.2996` edge `25.5428` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `72.9714` n `94` status `ready` deltaP `8.1053` edge `6.0717` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `29.8976` n `53` status `ready` deltaP `25.3342` edge `2.3932` maxDD `-3.6503`
- `market_context_high->equity_24h` score `21.8802` n `84` status `ready` deltaP `23.0655` edge `1.7402` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.8602` n `53` status `ready` deltaP `37.5295` edge `1.4669` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.3025` n `53` status `ready` deltaP `32.7341` edge `0.67` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.8901` n `84` status `ready` deltaP `43.13` edge `1.2618` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.2335` n `53` status `ready` deltaP `43.2292` edge `0.3146` maxDD `0.0`
- `market_context_high->metal_24h` score `6.4291` n `84` status `ready` deltaP `39.3849` edge `0.3145` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6446` n `53` status `ready` deltaP `44.262` edge `0.1296` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.2914` n `84` status `ready` deltaP `24.6776` edge `0.2026` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.8831` n `53` status `ready` deltaP `22.8806` edge `0.2014` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `2.934` n `53` status `ready` deltaP `16.6676` edge `0.1964` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9151` n `53` status `ready` deltaP `26.7114` edge `0.0902` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.6751` n `53` status `ready` deltaP `19.6762` edge `0.2405` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.169` n `53` status `ready` deltaP `25.5903` edge `0.0356` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6643` n `53` status `ready` deltaP `18.0022` edge `0.0623` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.4525` n `53` status `ready` deltaP `13.2108` edge `0.5487` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.3384` n `53` status `ready` deltaP `24.5168` edge `0.172` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1267` n `53` status `ready` deltaP `15.9784` edge `0.0175` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

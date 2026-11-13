# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T02:37:24.906347+00:00`
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

- `market_context_high->unknown_24h` score `294.4129` n `84` status `ready` deltaP `6.2996` edge `24.5065` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `59.3054` n `94` status `ready` deltaP `7.8004` edge `4.9349` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `30.799` n `53` status `ready` deltaP `26.8967` edge `2.4579` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.7816` n `84` status `ready` deltaP `24.628` edge `1.8049` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.2733` n `53` status `ready` deltaP `38.9184` edge `1.5106` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.4537` n `53` status `ready` deltaP `32.7341` edge `0.6826` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `9.4201` n `84` status `ready` deltaP `45.3869` edge `1.3147` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.006` n `53` status `ready` deltaP `43.0556` edge `0.2968` maxDD `0.0`
- `market_context_high->metal_24h` score `6.6981` n `84` status `ready` deltaP `40.9474` edge `0.3265` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.4265` n `53` status `ready` deltaP `42.5852` edge `0.1226` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.3598` n `84` status `ready` deltaP `24.6776` edge `0.2083` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.9515` n `53` status `ready` deltaP `22.8806` edge `0.2071` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.1323` n `53` status `ready` deltaP `28.5406` edge `0.0961` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.1007` n `53` status `ready` deltaP `17.1167` edge `0.2073` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6159` n `53` status `ready` deltaP `19.3713` edge `0.2376` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.0995` n `53` status `ready` deltaP `24.9915` edge `0.0338` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `1.9824` n `53` status `ready` deltaP `15.4677` edge `0.6016` maxDD `-29.0448`
- `news_risk_high->index_4h` score `1.6907` n `53` status `ready` deltaP `18.0022` edge `0.0645` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.4464` n `53` status `ready` deltaP `24.9741` edge `0.1828` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1304` n `53` status `ready` deltaP `15.8287` edge `0.0188` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

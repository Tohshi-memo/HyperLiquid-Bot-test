# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T04:07:26.036511+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9408`

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

- `market_context_high->unknown_24h` score `555.4473` n `66` status `ready` deltaP `2.4263` edge `46.2711` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.4836` n `53` status `ready` deltaP `46.0646` edge `3.2205` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.7299` n `66` status `ready` deltaP `41.0903` edge `3.0244` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.518` n `66` status `ready` deltaP `57.8121` edge `2.1821` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.1006` n `53` status `ready` deltaP `43.1052` edge `2.6144` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.7752` n `53` status `ready` deltaP `38.9075` edge `0.8349` maxDD `-7.0416`
- `market_context_high->index_24h` score `7.3593` n `66` status `ready` deltaP `43.2041` edge `0.3344` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.2108` n `53` status `ready` deltaP `49.74` edge `0.2693` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.3455` n `53` status `ready` deltaP `14.473` edge `1.1676` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.0013` n `53` status `ready` deltaP `39.4591` edge `0.2674` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.7256` n `66` status `ready` deltaP `54.3459` edge `0.4609` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.6566` n `53` status `ready` deltaP `22.3256` edge `0.4713` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `5.0189` n `53` status `ready` deltaP `46.001` edge `0.1492` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.7314` n `53` status `ready` deltaP `20.0355` edge `0.2404` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.3417` n `53` status `ready` deltaP `30.9038` edge `0.0978` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.067` n `53` status `ready` deltaP `26.8602` edge `0.378` maxDD `-10.1088`
- `market_context_high->crypto_major_24h` score `2.4629` n `66` status `ready` deltaP `12.6306` edge `1.1536` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.4511` n `53` status `ready` deltaP `25.2434` edge `0.0796` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2298` n `53` status `ready` deltaP `25.6592` edge `0.0402` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3831` n `53` status `ready` deltaP `18.4477` edge `0.0224` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

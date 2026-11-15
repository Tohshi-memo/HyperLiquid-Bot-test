# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T04:22:24.099163+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9644`

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

- `market_context_high->unknown_24h` score `554.4849` n `66` status `ready` deltaP `2.4263` edge `46.1909` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.5203` n `53` status `ready` deltaP `46.2379` edge `3.2224` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.7666` n `66` status `ready` deltaP `41.2636` edge `3.0263` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.5828` n `66` status `ready` deltaP `57.8121` edge `2.1875` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.1139` n `53` status `ready` deltaP `43.1052` edge `2.6161` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.768` n `53` status `ready` deltaP `38.9075` edge `0.8343` maxDD `-7.0416`
- `market_context_high->index_24h` score `7.3756` n `66` status `ready` deltaP `43.3774` edge `0.3346` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.212` n `53` status `ready` deltaP `49.74` edge `0.2694` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.3876` n `53` status `ready` deltaP `14.473` edge `1.173` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.0176` n `53` status `ready` deltaP `39.6324` edge `0.2676` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.7455` n `66` status `ready` deltaP `54.5192` edge `0.4623` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.6036` n `53` status `ready` deltaP `22.1734` edge `0.4679` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `5.0067` n `53` status `ready` deltaP `45.8488` edge `0.1492` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.7302` n `53` status `ready` deltaP `20.0355` edge `0.2403` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.3405` n `53` status `ready` deltaP `30.9038` edge `0.0977` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.0396` n `53` status `ready` deltaP `26.708` edge `0.3755` maxDD `-10.1088`
- `market_context_high->crypto_major_24h` score `2.4833` n `66` status `ready` deltaP `12.6306` edge `1.1553` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.439` n `53` status `ready` deltaP `25.0912` edge `0.0796` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2298` n `53` status `ready` deltaP `25.6592` edge `0.0402` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3831` n `53` status `ready` deltaP `18.4477` edge `0.0224` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

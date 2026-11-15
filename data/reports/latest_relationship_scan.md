# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T04:52:23.872867+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9702`

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

- `market_context_high->unknown_24h` score `552.5745` n `66` status `ready` deltaP `2.4263` edge `46.0317` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.6068` n `53` status `ready` deltaP `46.5845` edge `3.2273` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.8531` n `66` status `ready` deltaP `41.6102` edge `3.0312` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.7256` n `66` status `ready` deltaP `57.8121` edge `2.1994` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.1498` n `53` status `ready` deltaP `43.1052` edge `2.6207` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.7512` n `53` status `ready` deltaP `38.9075` edge `0.8329` maxDD `-7.0416`
- `market_context_high->index_24h` score `7.4105` n `66` status `ready` deltaP `43.724` edge `0.3352` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.2144` n `53` status `ready` deltaP `49.74` edge `0.2696` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.4804` n `53` status `ready` deltaP `14.473` edge `1.1849` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.0525` n `53` status `ready` deltaP `39.979` edge `0.2682` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.7893` n `66` status `ready` deltaP `54.8658` edge `0.4656` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.498` n `53` status `ready` deltaP `22.1734` edge `0.4591` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `5.0189` n `53` status `ready` deltaP `46.001` edge `0.1492` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.723` n `53` status `ready` deltaP `19.961` edge `0.2402` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.3405` n `53` status `ready` deltaP `30.9038` edge `0.0977` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.9684` n `53` status `ready` deltaP `26.4036` edge `0.3684` maxDD `-10.1088`
- `market_context_high->crypto_major_24h` score `2.5385` n `66` status `ready` deltaP `12.6306` edge `1.1599` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.4268` n `53` status `ready` deltaP `24.939` edge `0.0796` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2242` n `53` status `ready` deltaP `25.5903` edge `0.0402` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3771` n `53` status `ready` deltaP `18.3736` edge `0.0224` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

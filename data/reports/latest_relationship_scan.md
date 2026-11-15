# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T03:52:28.714734+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9390`

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

- `market_context_high->unknown_24h` score `556.4265` n `66` status `ready` deltaP `2.4263` edge `46.3527` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.4446` n `53` status `ready` deltaP `45.8913` edge `3.2184` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.6909` n `66` status `ready` deltaP `40.917` edge `3.0223` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.4484` n `66` status `ready` deltaP `57.8121` edge `2.1763` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.085` n `53` status `ready` deltaP `43.1052` edge `2.6124` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.7969` n `53` status `ready` deltaP `39.0597` edge `0.8357` maxDD `-7.0416`
- `market_context_high->index_24h` score `7.3431` n `66` status `ready` deltaP `43.0308` edge `0.3342` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.2096` n `53` status `ready` deltaP `49.74` edge `0.2692` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.3003` n `53` status `ready` deltaP `14.473` edge `1.1618` maxDD `-29.0448`
- `news_risk_high->index_24h` score `5.9851` n `53` status `ready` deltaP `39.2858` edge `0.2672` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.7168` n `53` status `ready` deltaP `22.4779` edge `0.4753` maxDD `-9.2335`
- `market_context_high->metal_24h` score `5.7049` n `66` status `ready` deltaP `54.1726` edge `0.4594` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `5.0189` n `53` status `ready` deltaP `46.001` edge `0.1492` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.7446` n `53` status `ready` deltaP `20.185` edge `0.2405` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.3539` n `53` status `ready` deltaP `31.056` edge `0.0978` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.0991` n `53` status `ready` deltaP `27.0124` edge `0.3811` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4645` n `53` status `ready` deltaP `25.3956` edge `0.0797` maxDD `-0.8235`
- `market_context_high->crypto_major_24h` score `2.4389` n `66` status `ready` deltaP `12.6306` edge `1.1516` maxDD `-76.2717`
- `news_risk_high->metal_1h` score `2.2298` n `53` status `ready` deltaP `25.6592` edge `0.0402` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.395` n `53` status `ready` deltaP `18.5971` edge `0.0224` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T02:37:38.964133+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9372`

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

- `market_context_high->unknown_24h` score `560.7072` n `66` status `ready` deltaP `2.4306` edge `46.7094` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.2381` n `53` status `ready` deltaP `45.1258` edge `3.2063` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.4844` n `66` status `ready` deltaP `40.1515` edge `3.0102` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.0222` n `66` status `ready` deltaP `57.7652` edge `2.1411` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `20.9342` n `53` status `ready` deltaP `43.0851` edge `2.5932` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.8583` n `53` status `ready` deltaP `39.1365` edge `0.8403` maxDD `-7.0416`
- `market_context_high->index_24h` score `7.2639` n `66` status `ready` deltaP `42.2506` edge `0.3328` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.2443` n `53` status `ready` deltaP `50.1736` edge `0.2692` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.0436` n `53` status `ready` deltaP `22.5725` edge `0.5019` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `6.0233` n `53` status `ready` deltaP `14.4261` edge `1.1266` maxDD `-29.0448`
- `news_risk_high->index_24h` score `5.9059` n `53` status `ready` deltaP `38.5056` edge `0.2658` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.6122` n `66` status `ready` deltaP `53.4249` edge `0.4525` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `5.0529` n `53` status `ready` deltaP `46.3962` edge `0.1494` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.7794` n `53` status `ready` deltaP `20.2604` edge `0.2429` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4026` n `53` status `ready` deltaP `31.5894` edge `0.0983` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.3001` n `53` status `ready` deltaP `27.4131` edge `0.4042` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4718` n `53` status `ready` deltaP `25.4717` edge `0.0798` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2422` n `53` status `ready` deltaP `25.74` edge `0.0407` maxDD `-0.3692`
- `market_context_high->crypto_major_24h` score `2.2069` n `66` status `ready` deltaP `12.6105` edge `1.1324` maxDD `-76.2717`
- `news_risk_high->index_1h` score `1.3783` n `53` status `ready` deltaP `18.3736` edge `0.0225` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

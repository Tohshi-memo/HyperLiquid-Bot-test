# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T18:37:41.348065+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11734`

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

- `market_context_high->unknown_24h` score `304.5775` n `84` status `ready` deltaP `6.4425` edge `25.3526` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `84.441` n `94` status `ready` deltaP `8.1053` edge `7.0275` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.1108` n `53` status `ready` deltaP `22.2596` edge `2.2648` maxDD `-3.6503`
- `market_context_high->equity_24h` score `20.0934` n `84` status `ready` deltaP `19.9909` edge `1.6118` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.2794` n `53` status `ready` deltaP `37.0699` edge `1.3955` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.2939` n `53` status `ready` deltaP `32.5816` edge `0.6703` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `7.8686` n `84` status `ready` deltaP `39.9407` edge `1.1521` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.5072` n `53` status `ready` deltaP `43.4256` edge `0.3361` maxDD `0.0`
- `market_context_high->metal_24h` score `6.1727` n `84` status `ready` deltaP `38.8491` edge `0.2967` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.7256` n `53` status `ready` deltaP `44.7193` edge `0.1333` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.9435` n `84` status `ready` deltaP `21.9641` edge `0.1917` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.5352` n `53` status `ready` deltaP `20.1671` edge `0.1905` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.0243` n `53` status `ready` deltaP `26.7114` edge `0.0993` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.0082` n `53` status `ready` deltaP `21.2006` edge `0.2581` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `2.988` n `53` status `ready` deltaP `16.8173` edge `0.1999` maxDD `-3.7082`
- `news_risk_high->metal_1h` score `2.217` n `53` status `ready` deltaP `26.0394` edge `0.0366` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6943` n `53` status `ready` deltaP `18.0022` edge `0.0648` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.6038` n `53` status `ready` deltaP `25.7363` edge `0.1979` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1819` n `53` status `ready` deltaP `16.4275` edge `0.0191` maxDD `-0.4103`
- `market_context_high->fx_24h` score `0.5729` n `84` status `ready` deltaP `23.896` edge `0.0484` maxDD `-3.4642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

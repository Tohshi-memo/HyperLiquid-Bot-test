# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T19:07:27.930542+00:00`
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

- `market_context_high->unknown_24h` score `306.0703` n `84` status `ready` deltaP `6.4425` edge `25.477` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `82.3326` n `94` status `ready` deltaP `8.1053` edge `6.8518` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.3341` n `53` status `ready` deltaP `22.6056` edge `2.2811` maxDD `-3.6503`
- `market_context_high->equity_24h` score `20.3167` n `84` status `ready` deltaP `20.3369` edge `1.6281` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.3703` n `53` status `ready` deltaP `37.243` edge `1.406` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.2553` n `53` status `ready` deltaP `32.4292` edge `0.6681` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.0301` n `84` status `ready` deltaP `40.2867` edge `1.1705` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.458` n `53` status `ready` deltaP `43.0796` edge `0.3343` maxDD `0.0`
- `market_context_high->metal_24h` score `6.1943` n `84` status `ready` deltaP `38.8491` edge `0.2985` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.705` n `53` status `ready` deltaP `44.5669` edge `0.1326` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.9844` n `84` status `ready` deltaP `22.3101` edge `0.1928` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.5761` n `53` status `ready` deltaP `20.5131` edge `0.1916` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.0227` n `53` status `ready` deltaP `16.967` edge `0.2018` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0171` n `53` status `ready` deltaP `26.7114` edge `0.0987` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.9768` n `53` status `ready` deltaP `21.0481` edge `0.2565` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2289` n `53` status `ready` deltaP `26.1891` edge `0.0366` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6591` n `53` status `ready` deltaP `17.6973` edge `0.0639` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.6093` n `53` status `ready` deltaP `25.7363` edge `0.1986` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1831` n `53` status `ready` deltaP `16.4275` edge `0.0192` maxDD `-0.4103`
- `news_risk_high->crypto_alt_24h` score `0.5925` n `53` status `ready` deltaP `10.3675` edge `0.4574` maxDD `-29.0448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

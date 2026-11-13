# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T21:37:30.044999+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10308`

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

- `market_context_high->unknown_24h` score `370.2402` n `75` status `ready` deltaP `2.5416` edge `30.8505` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `34.593` n `53` status `ready` deltaP `34.3619` edge `2.7243` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.3593` n `75` status `ready` deltaP `28.9027` edge `2.1581` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.9434` n `75` status `ready` deltaP `47.5834` edge `1.3462` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.5574` n `53` status `ready` deltaP `42.0434` edge `1.7826` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.8478` n `53` status `ready` deltaP `34.4109` edge `0.7876` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.8684` n `53` status `ready` deltaP `38.1944` edge `0.2344` maxDD `0.0`
- `market_context_high->index_24h` score `5.0949` n `75` status `ready` deltaP `27.9931` edge `0.2471` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.9237` n `53` status `ready` deltaP `46.701` edge `0.1366` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.4139` n `53` status `ready` deltaP `26.0056` edge `0.2248` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.0782` n `75` status `ready` deltaP `41.1598` edge `0.3376` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.4546` n `53` status `ready` deltaP `17.8652` edge `0.2318` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2549` n `53` status `ready` deltaP `29.6077` edge `0.0992` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1079` n `53` status `ready` deltaP `19.3713` edge `0.2786` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2649` n `53` status `ready` deltaP `26.4885` edge `0.0376` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9142` n `53` status `ready` deltaP `19.2217` edge `0.075` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.8074` n `53` status `ready` deltaP `14.4261` edge `0.5861` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.7135` n `53` status `ready` deltaP `25.4314` edge `0.214` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1735` n `53` status `ready` deltaP `15.9784` edge `0.0214` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6213` n `53` status `ready` deltaP `16.8455` edge `0.0653` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T21:07:34.785303+00:00`
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

- `market_context_high->unknown_24h` score `370.3676` n `75` status `ready` deltaP `2.8889` edge `30.8588` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `34.4368` n `53` status `ready` deltaP `34.0147` edge `2.7136` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.2032` n `75` status `ready` deltaP `28.5555` edge `2.1474` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.9686` n `75` status `ready` deltaP `47.5834` edge `1.3483` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.5114` n `53` status `ready` deltaP `42.0434` edge `1.7767` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.8442` n `53` status `ready` deltaP `34.4109` edge `0.7873` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.825` n `53` status `ready` deltaP `37.8472` edge `0.2331` maxDD `0.0`
- `market_context_high->index_24h` score `5.0551` n `75` status `ready` deltaP `27.6459` edge `0.2461` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.8933` n `53` status `ready` deltaP `46.3962` edge `0.1361` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.3741` n `53` status `ready` deltaP `25.6584` edge `0.2238` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.0614` n `75` status `ready` deltaP `40.9861` edge `0.3366` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.415` n `53` status `ready` deltaP `17.7155` edge `0.2295` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2585` n `53` status `ready` deltaP `29.6077` edge `0.0995` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.0619` n `53` status `ready` deltaP `19.0664` edge `0.2768` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2637` n `53` status `ready` deltaP `26.4885` edge `0.0375` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9154` n `53` status `ready` deltaP `19.2217` edge `0.0751` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.8237` n `53` status `ready` deltaP `14.4261` edge `0.5882` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.7081` n `53` status `ready` deltaP `25.4314` edge `0.2133` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1592` n `53` status `ready` deltaP `15.8287` edge `0.0212` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5956` n `53` status `ready` deltaP `16.6958` edge `0.063` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

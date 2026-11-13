# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T12:07:32.813070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `382.4671` n `74` status `ready` deltaP `5.9779` edge `31.8465` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.7402` n `53` status `ready` deltaP `31.9314` edge `2.5861` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.1839` n `74` status `ready` deltaP `27.5713` edge `2.0615` maxDD `-8.7317`
- `market_context_high->crypto_alt_24h` score `18.8411` n `74` status `ready` deltaP `52.4493` edge `1.4719` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.2127` n `53` status `ready` deltaP `42.3906` edge `1.7361` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.4512` n `53` status `ready` deltaP `34.8682` edge `0.7515` maxDD `-7.0416`
- `market_context_high->metal_24h` score `6.0051` n `74` status `ready` deltaP `38.0021` edge `0.3283` maxDD `-3.4976`
- `news_risk_high->commodity_24h` score `5.8668` n `53` status `ready` deltaP `37.5` edge `0.2389` maxDD `0.0`
- `market_context_high->index_24h` score `4.8456` n `74` status `ready` deltaP `25.9572` edge `0.2399` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.6266` n `53` status `ready` deltaP `44.262` edge `0.1281` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1315` n `53` status `ready` deltaP `24.0959` edge `0.214` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.3142` n `53` status `ready` deltaP `17.5658` edge `0.2221` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.1427` n `53` status `ready` deltaP `19.3713` edge `0.2815` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.0841` n `53` status `ready` deltaP `28.3882` edge `0.0931` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `3.0399` n `53` status `ready` deltaP `19.6344` edge `0.7094` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1199` n `53` status `ready` deltaP `24.9915` edge `0.0355` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9502` n `53` status `ready` deltaP `20.1363` edge `0.0719` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.886` n `53` status `ready` deltaP `26.4985` edge `0.229` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1484` n `53` status `ready` deltaP `15.8287` edge `0.0203` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6291` n `53` status `ready` deltaP `17.1449` edge `0.0643` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

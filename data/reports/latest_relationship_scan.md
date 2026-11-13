# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T11:37:27.952592+00:00`
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

- `market_context_high->unknown_24h` score `384.1699` n `74` status `ready` deltaP `5.9779` edge `31.9884` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.7294` n `53` status `ready` deltaP `31.9314` edge `2.5852` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.4605` n `74` status `ready` deltaP `27.5713` edge `2.0673` maxDD `-8.0189`
- `market_context_high->crypto_alt_24h` score `17.8102` n `74` status `ready` deltaP `50.0938` edge `1.4411` maxDD `-18.9364`
- `news_risk_high->crypto_major_24h` score `14.1854` n `53` status `ready` deltaP `42.3906` edge `1.7326` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.5068` n `53` status `ready` deltaP `35.1731` edge `0.7541` maxDD `-7.0416`
- `market_context_high->metal_24h` score `6.3912` n `74` status `ready` deltaP `40.3576` edge `0.3375` maxDD `-2.9161`
- `news_risk_high->commodity_24h` score `5.9306` n `53` status `ready` deltaP `37.8472` edge `0.2419` maxDD `0.0`
- `market_context_high->index_24h` score `4.8264` n `74` status `ready` deltaP `25.9572` edge `0.2383` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.6254` n `53` status `ready` deltaP `44.262` edge `0.128` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1339` n `53` status `ready` deltaP `24.0959` edge `0.2142` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.2962` n `53` status `ready` deltaP `17.5658` edge `0.2206` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.1969` n `53` status `ready` deltaP `19.5237` edge `0.285` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1193` n `53` status `ready` deltaP `28.6931` edge `0.094` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `3.0931` n `53` status `ready` deltaP `19.9816` edge `0.7139` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1211` n `53` status `ready` deltaP `24.9915` edge `0.0356` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9502` n `53` status `ready` deltaP `20.1363` edge `0.0719` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8782` n `53` status `ready` deltaP `26.4985` edge `0.228` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1472` n `53` status `ready` deltaP `15.8287` edge `0.0202` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6268` n `53` status `ready` deltaP `17.1449` edge `0.064` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

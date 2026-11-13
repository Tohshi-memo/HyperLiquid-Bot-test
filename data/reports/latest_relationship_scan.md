# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T11:52:29.782981+00:00`
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

- `market_context_high->unknown_24h` score `383.1559` n `74` status `ready` deltaP `5.9779` edge `31.9039` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.7414` n `53` status `ready` deltaP `31.9314` edge `2.5862` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.2422` n `74` status `ready` deltaP `27.5713` edge `2.0605` maxDD `-8.597`
- `market_context_high->crypto_alt_24h` score `18.2774` n `74` status `ready` deltaP `51.2716` edge `1.4543` maxDD `-17.8394`
- `news_risk_high->crypto_major_24h` score `14.201` n `53` status `ready` deltaP `42.3906` edge `1.7346` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.4838` n `53` status `ready` deltaP `35.0207` edge `0.7532` maxDD `-7.0416`
- `market_context_high->metal_24h` score `6.1933` n `74` status `ready` deltaP `39.1798` edge `0.3325` maxDD `-3.2069`
- `news_risk_high->commodity_24h` score `5.9011` n `53` status `ready` deltaP `37.6736` edge `0.2406` maxDD `0.0`
- `market_context_high->index_24h` score `4.8324` n `74` status `ready` deltaP `25.9572` edge `0.2388` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.6254` n `53` status `ready` deltaP `44.262` edge `0.128` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1339` n `53` status `ready` deltaP `24.0959` edge `0.2142` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.3094` n `53` status `ready` deltaP `17.5658` edge `0.2217` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.1619` n `53` status `ready` deltaP `19.3713` edge `0.2831` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1023` n `53` status `ready` deltaP `28.5406` edge `0.0936` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `3.0692` n `53` status `ready` deltaP `19.808` edge `0.712` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1211` n `53` status `ready` deltaP `24.9915` edge `0.0356` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9502` n `53` status `ready` deltaP `20.1363` edge `0.0719` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8821` n `53` status `ready` deltaP `26.4985` edge `0.2285` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1484` n `53` status `ready` deltaP `15.8287` edge `0.0203` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6291` n `53` status `ready` deltaP `17.1449` edge `0.0643` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T11:37:28.096969+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_24h` score `548.9039` n `68` status `ready` deltaP `4.5139` edge `45.7119` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.3897` n `53` status `ready` deltaP `37.6606` edge `3.0187` maxDD `-3.6503`
- `market_context_high->equity_24h` score `33.6096` n `68` status `ready` deltaP `33.221` edge `2.7335` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `21.8086` n `68` status `ready` deltaP `55.2696` edge `1.5566` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `16.0979` n `53` status `ready` deltaP `42.0434` edge `1.9801` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.245` n `53` status `ready` deltaP `36.2402` edge `0.8085` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.9177` n `53` status `ready` deltaP `47.3958` edge `0.2605` maxDD `0.0`
- `market_context_high->index_24h` score `6.737` n `68` status `ready` deltaP `39.1749` edge `0.3094` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.4896` n `53` status `ready` deltaP `35.207` edge `0.2531` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.9822` n `68` status `ready` deltaP `49.0196` edge `0.4011` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.9075` n `53` status `ready` deltaP `46.2437` edge `0.1383` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.087` n `53` status `ready` deltaP `21.2006` edge `0.348` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5768` n `53` status `ready` deltaP `18.7634` edge `0.236` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2065` n `53` status `ready` deltaP `29.3028` edge `0.0972` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.1835` n `53` status `ready` deltaP `25.4406` edge `0.0378` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `2.1731` n `53` status `ready` deltaP `26.4985` edge `0.2658` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.1687` n `53` status `ready` deltaP `22.118` edge `0.0769` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.8744` n `53` status `ready` deltaP `14.4261` edge `0.5947` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2502` n `53` status `ready` deltaP `16.8766` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7484` n `53` status `ready` deltaP `17.7437` edge `0.0756` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

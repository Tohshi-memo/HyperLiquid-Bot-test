# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T20:07:34.411349+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10548`

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

- `market_context_high->unknown_24h` score `370.2572` n `75` status `ready` deltaP `2.8889` edge `30.8496` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `34.2147` n `53` status `ready` deltaP `33.6675` edge `2.6974` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.981` n `75` status `ready` deltaP `28.2083` edge `2.1312` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.0881` n `75` status `ready` deltaP `47.757` edge `1.3571` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.4646` n `53` status `ready` deltaP `42.0434` edge `1.7707` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.9346` n `53` status `ready` deltaP `34.7158` edge `0.7928` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.7859` n `53` status `ready` deltaP `37.6736` edge `0.231` maxDD `0.0`
- `market_context_high->index_24h` score `4.9827` n `75` status `ready` deltaP `26.9514` edge `0.2447` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.835` n `53` status `ready` deltaP `45.7864` edge `0.1353` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.3017` n `53` status `ready` deltaP `24.9639` edge `0.2224` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.0089` n `75` status `ready` deltaP `40.2917` edge `0.3345` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3851` n `53` status `ready` deltaP `17.4161` edge `0.229` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2888` n `53` status `ready` deltaP `29.9126` edge `0.1` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1149` n `53` status `ready` deltaP `19.2189` edge `0.2802` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2254` n `53` status `ready` deltaP `26.0394` edge `0.0373` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.975` n `53` status `ready` deltaP `19.8315` edge `0.076` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.9014` n `53` status `ready` deltaP `14.5997` edge `0.597` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.7497` n `53` status `ready` deltaP `25.7363` edge `0.2166` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1723` n `53` status `ready` deltaP `15.9784` edge `0.0213` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.573` n `53` status `ready` deltaP `16.5461` edge `0.0611` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

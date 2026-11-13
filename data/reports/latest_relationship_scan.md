# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T11:07:30.253472+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10524`

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

- `market_context_high->unknown_24h` score `385.5943` n `74` status `ready` deltaP `5.9779` edge `32.1071` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.7066` n `53` status `ready` deltaP `31.9314` edge `2.5833` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.872` n `74` status `ready` deltaP `27.5713` edge `2.0799` maxDD `-6.6166`
- `news_risk_high->crypto_major_24h` score `14.141` n `53` status `ready` deltaP `42.3906` edge `1.7269` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `11.1588` n `74` status `ready` deltaP `50.0938` edge `1.4257` maxDD `-21.3236`
- `news_risk_high->equity_4h` score `10.5322` n `53` status `ready` deltaP `35.3255` edge `0.7552` maxDD `-7.0416`
- `market_context_high->metal_24h` score `6.8386` n `74` status `ready` deltaP `42.713` edge `0.3492` maxDD `-2.1259`
- `news_risk_high->commodity_24h` score `5.9908` n `53` status `ready` deltaP `38.1944` edge `0.2446` maxDD `0.0`
- `market_context_high->index_24h` score `4.713` n `74` status `ready` deltaP `24.7795` edge `0.2367` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.612` n `53` status `ready` deltaP `44.1096` edge `0.1279` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1514` n `53` status `ready` deltaP `24.2695` edge `0.2145` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.2842` n `53` status `ready` deltaP `17.5658` edge `0.2196` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.2441` n `53` status `ready` deltaP `19.8286` edge `0.2869` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1289` n `53` status `ready` deltaP `28.6931` edge `0.0948` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `3.111` n `53` status `ready` deltaP `19.9816` edge `0.7162` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1056` n `53` status `ready` deltaP `24.8418` edge `0.0353` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.949` n `53` status `ready` deltaP `20.1363` edge `0.0718` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8429` n `53` status `ready` deltaP `26.1936` edge `0.2255` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1591` n `53` status `ready` deltaP `15.9784` edge `0.0202` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6213` n `53` status `ready` deltaP `17.1449` edge `0.0633` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T23:22:28.274824+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10332`

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

- `market_context_high->unknown_24h` score `381.5069` n `75` status `ready` deltaP `2.1944` edge `31.7917` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `35.0334` n `53` status `ready` deltaP `34.3619` edge `2.761` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.7997` n `75` status `ready` deltaP `28.9027` edge `2.1948` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.8822` n `75` status `ready` deltaP `47.5834` edge `1.3411` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.7399` n `53` status `ready` deltaP `42.0434` edge `1.806` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.9346` n `53` status `ready` deltaP `34.7158` edge `0.7928` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.0244` n `53` status `ready` deltaP `39.4097` edge `0.2393` maxDD `0.0`
- `market_context_high->index_24h` score `5.2317` n `75` status `ready` deltaP `29.2084` edge `0.2504` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0125` n `53` status `ready` deltaP `47.6157` edge `0.1379` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.5507` n `53` status `ready` deltaP `27.2209` edge `0.2281` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.1153` n `75` status `ready` deltaP `41.3334` edge `0.3412` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.5241` n `53` status `ready` deltaP `18.3143` edge `0.2346` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.3744` n `53` status `ready` deltaP `20.4384` edge `0.2937` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.2221` n `53` status `ready` deltaP `29.3028` edge `0.0985` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2901` n `53` status `ready` deltaP `26.7879` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.902` n `53` status `ready` deltaP `19.0693` edge `0.075` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7931` n `53` status `ready` deltaP `25.4314` edge `0.2242` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7676` n `53` status `ready` deltaP `14.4261` edge `0.581` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1616` n `53` status `ready` deltaP `15.8287` edge `0.0214` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6424` n `53` status `ready` deltaP `16.9952` edge `0.067` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

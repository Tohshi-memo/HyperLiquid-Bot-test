# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T15:07:35.350509+00:00`
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

- `market_context_high->unknown_24h` score `371.6532` n `75` status `ready` deltaP `4.7986` edge `30.9532` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.5627` n `53` status `ready` deltaP `31.0633` edge `2.5771` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.3291` n `75` status `ready` deltaP `25.6041` edge `2.0109` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `18.0718` n `75` status `ready` deltaP `50.7084` edge `1.4194` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.2064` n `53` status `ready` deltaP `42.0434` edge `1.7376` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.1123` n `53` status `ready` deltaP `33.4963` edge `0.7324` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.5913` n `53` status `ready` deltaP `36.1111` edge `0.2252` maxDD `0.0`
- `market_context_high->index_24h` score `4.7111` n `75` status `ready` deltaP `25.0417` edge `0.2348` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.5888` n `53` status `ready` deltaP `43.8047` edge `0.128` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0302` n `53` status `ready` deltaP `23.0542` edge `0.2125` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.8358` n `75` status `ready` deltaP `38.2084` edge `0.3262` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3491` n `53` status `ready` deltaP `17.4161` edge `0.226` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9095` n `53` status `ready` deltaP `27.0162` edge `0.0877` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.8197` n `53` status `ready` deltaP `18.3042` edge `0.2617` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.5408` n `53` status `ready` deltaP `17.5511` edge `0.6593` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1068` n `53` status `ready` deltaP `24.8418` edge `0.0354` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.8978` n `53` status `ready` deltaP `19.5266` edge `0.0716` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7113` n `53` status `ready` deltaP `25.5838` edge `0.2127` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2083` n `53` status `ready` deltaP `16.4275` edge `0.0213` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5917` n `53` status `ready` deltaP `16.8455` edge `0.0615` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

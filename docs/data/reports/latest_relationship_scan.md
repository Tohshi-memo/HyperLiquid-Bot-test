# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T20:52:29.667886+00:00`
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

- `market_context_high->unknown_24h` score `369.9704` n `75` status `ready` deltaP `2.8889` edge `30.8257` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `34.3816` n `53` status `ready` deltaP `34.0147` edge `2.709` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.148` n `75` status `ready` deltaP `28.5555` edge `2.1428` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.9866` n `75` status `ready` deltaP `47.5834` edge `1.3498` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.495` n `53` status `ready` deltaP `42.0434` edge `1.7746` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.8588` n `53` status `ready` deltaP `34.5633` edge `0.7875` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.819` n `53` status `ready` deltaP `37.8472` edge `0.2326` maxDD `0.0`
- `market_context_high->index_24h` score `5.0364` n `75` status `ready` deltaP `27.4723` edge `0.2457` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.8787` n `53` status `ready` deltaP `46.2437` edge `0.1359` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.3554` n `53` status `ready` deltaP `25.4848` edge `0.2234` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.0484` n `75` status `ready` deltaP `40.8125` edge `0.3361` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.397` n `53` status `ready` deltaP `17.5658` edge `0.229` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2742` n `53` status `ready` deltaP `29.7601` edge `0.0998` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.0595` n `53` status `ready` deltaP `19.0664` edge `0.2766` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2505` n `53` status `ready` deltaP `26.3388` edge `0.0374` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9288` n `53` status `ready` deltaP `19.3741` edge `0.0752` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.8354` n `53` status `ready` deltaP `14.4261` edge `0.5897` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.7112` n `53` status `ready` deltaP `25.4314` edge `0.2137` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1592` n `53` status `ready` deltaP `15.8287` edge `0.0212` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5761` n `53` status `ready` deltaP `16.5461` edge `0.0615` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T18:52:27.364146+00:00`
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

- `market_context_high->unknown_24h` score `370.3964` n `75` status `ready` deltaP `2.8889` edge `30.8612` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `33.8536` n `53` status `ready` deltaP `32.7994` edge `2.6731` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.6199` n `75` status `ready` deltaP `27.3402` edge `2.1069` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.3207` n `75` status `ready` deltaP `48.625` edge `1.3707` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.4162` n `53` status `ready` deltaP `42.0434` edge `1.7645` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.9922` n `53` status `ready` deltaP `34.7158` edge `0.7976` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.6871` n `53` status `ready` deltaP `36.9792` edge `0.2274` maxDD `0.0`
- `market_context_high->index_24h` score `4.8905` n `75` status `ready` deltaP `26.0834` edge `0.2428` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.7852` n `53` status `ready` deltaP `45.3291` edge `0.1342` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.2095` n `53` status `ready` deltaP `24.0959` edge `0.2205` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.9811` n `75` status `ready` deltaP `40.1181` edge `0.3321` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3767` n `53` status `ready` deltaP `17.2664` edge `0.2293` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2125` n `53` status `ready` deltaP `29.3028` edge `0.0977` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1971` n `53` status `ready` deltaP `19.6762` edge `0.284` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.211` n `53` status `ready` deltaP `25.8897` edge `0.0371` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `2.0526` n `53` status `ready` deltaP `15.4677` edge `0.6106` maxDD `-29.0448`
- `news_risk_high->index_4h` score `2.0346` n `53` status `ready` deltaP `20.4412` edge `0.0769` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8243` n `53` status `ready` deltaP `26.346` edge `0.2221` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1879` n `53` status `ready` deltaP `16.1281` edge `0.0216` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6174` n `53` status `ready` deltaP `16.9952` edge `0.0638` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

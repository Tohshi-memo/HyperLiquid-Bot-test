# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T22:52:29.775638+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11566`

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

- `market_context_high->unknown_4h` score `92.5959` n `88` status `ready` deltaP `8.3863` edge `7.7052` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `52.1417` n `34` status `ready` deltaP `37.7163` edge `4.0937` maxDD `0.0`
- `market_context_high->unknown_24h` score `39.7548` n `88` status `ready` deltaP `4.9937` edge `3.2937` maxDD `-0.4609`
- `news_risk_high->crypto_major_24h` score `28.845` n `34` status `ready` deltaP `53.8062` edge `2.2416` maxDD `-12.7247`
- `market_context_high->equity_24h` score `21.5155` n `88` status `ready` deltaP `20.6708` edge `1.8943` maxDD `-16.7984`
- `news_risk_high->crypto_alt_24h` score `14.8689` n `34` status `ready` deltaP `31.4879` edge `1.204` maxDD `-10.9876`
- `news_risk_high->equity_4h` score `11.1704` n `53` status `ready` deltaP `34.1199` edge `0.8156` maxDD `-6.9762`
- `news_risk_high->index_24h` score `7.5483` n `34` status `ready` deltaP `34.4291` edge `0.3995` maxDD `0.0`
- `news_risk_high->commodity_24h` score `7.156` n `34` status `ready` deltaP `39.9654` edge `0.3299` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.8512` n `88` status `ready` deltaP `34.9638` edge `1.1547` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.6378` n `88` status `ready` deltaP `33.1039` edge `0.2211` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.124` n `53` status `ready` deltaP `40.4399` edge `0.1117` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.04` n `88` status `ready` deltaP `20.7927` edge `0.2443` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.5861` n `53` status `ready` deltaP `18.6137` edge `0.246` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.5587` n `53` status `ready` deltaP `19.9519` edge `0.3123` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.7087` n `53` status `ready` deltaP `24.4452` edge `0.0881` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2284` n `53` status `ready` deltaP `21.0644` edge `0.0889` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9797` n `53` status `ready` deltaP `23.9436` edge `0.0308` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.8946` n `53` status `ready` deltaP `23.5734` edge `0.2496` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3688` n `53` status `ready` deltaP `17.7748` edge `0.0257` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

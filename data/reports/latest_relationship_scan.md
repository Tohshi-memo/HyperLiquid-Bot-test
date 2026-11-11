# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T22:37:28.878992+00:00`
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

- `market_context_high->unknown_4h` score `92.6799` n `88` status `ready` deltaP `8.3863` edge `7.7122` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `52.8623` n `33` status `ready` deltaP `37.8893` edge `4.1526` maxDD `0.0`
- `market_context_high->unknown_24h` score `35.0844` n `88` status `ready` deltaP `4.9937` edge `2.9045` maxDD `-0.4609`
- `news_risk_high->crypto_major_24h` score `29.3965` n `33` status `ready` deltaP `55.9453` edge `2.2733` maxDD `-12.7247`
- `market_context_high->equity_24h` score `21.7681` n `88` status `ready` deltaP `20.8438` edge `1.9142` maxDD `-16.7984`
- `news_risk_high->crypto_alt_24h` score `15.5802` n `33` status `ready` deltaP `33.4487` edge `1.2502` maxDD `-10.9876`
- `news_risk_high->equity_4h` score `11.1596` n `53` status `ready` deltaP `34.1199` edge `0.8147` maxDD `-6.9762`
- `news_risk_high->index_24h` score `7.6342` n `33` status `ready` deltaP `34.6021` edge `0.4055` maxDD `0.0`
- `news_risk_high->commodity_24h` score `7.2268` n `33` status `ready` deltaP `39.9654` edge `0.3358` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.8949` n `88` status `ready` deltaP `34.9638` edge `1.1603` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.6204` n `88` status `ready` deltaP `32.9309` edge `0.2208` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.1059` n `53` status `ready` deltaP `40.2879` edge `0.1112` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.0874` n `88` status `ready` deltaP `20.9657` edge `0.2471` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.5514` n `53` status `ready` deltaP `18.464` edge `0.2441` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.519` n `53` status `ready` deltaP `19.7999` edge `0.31` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.7099` n `53` status `ready` deltaP `24.4452` edge `0.0882` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2296` n `53` status `ready` deltaP `21.0644` edge `0.089` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9797` n `53` status `ready` deltaP `23.9436` edge `0.0308` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.8687` n `53` status `ready` deltaP `23.4214` edge `0.2473` maxDD `-10.1088`
- `news_risk_high->metal_24h` score `1.4832` n `33` status `ready` deltaP `18.9158` edge `0.1143` maxDD `-0.6872`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

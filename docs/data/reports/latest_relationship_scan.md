# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T08:22:26.749511+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11540`

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

- `market_context_high->unknown_24h` score `219.9386` n `88` status `ready` deltaP `6.0318` edge `18.3021` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `88.623` n `88` status `ready` deltaP `7.2201` edge `7.3819` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `30.2963` n `52` status `ready` deltaP `23.9486` edge `2.4262` maxDD `-3.2263`
- `market_context_high->equity_24h` score `15.0645` n `88` status `ready` deltaP `16.5185` edge `1.3844` maxDD `-16.7984`
- `news_risk_high->crypto_major_24h` score `12.4748` n `52` status `ready` deltaP `37.9491` edge `1.5429` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.5254` n `53` status `ready` deltaP `34.8682` edge `0.8402` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.8435` n `52` status `ready` deltaP `40.1384` edge `0.3027` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.1937` n `88` status `ready` deltaP `34.9638` edge `0.9422` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8813` n `88` status `ready` deltaP `35.0071` edge `0.2287` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.3403` n `53` status `ready` deltaP `41.823` edge `0.1205` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1338` n `53` status `ready` deltaP `22.1152` edge `0.3458` maxDD `-9.2335`
- `news_risk_high->index_24h` score `4.0405` n `52` status `ready` deltaP `21.0074` edge `0.2227` maxDD `-0.4168`
- `news_risk_high->equity_1h` score `3.543` n `53` status `ready` deltaP `18.1646` edge `0.2454` maxDD `-3.6997`
- `market_context_high->index_24h` score `2.9086` n `88` status `ready` deltaP `16.9864` edge `0.1754` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.7712` n `53` status `ready` deltaP `24.8821` edge `0.0904` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.2942` n `53` status `ready` deltaP `25.8887` edge `0.2854` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.2629` n `53` status `ready` deltaP `21.6607` edge `0.0878` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0816` n `53` status `ready` deltaP `24.8418` edge `0.0333` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3556` n `53` status `ready` deltaP `17.7748` edge `0.0246` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7765` n `53` status `ready` deltaP `17.8934` edge `0.0782` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

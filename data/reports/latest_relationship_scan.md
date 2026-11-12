# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T02:52:25.970744+00:00`
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

- `market_context_high->unknown_24h` score `115.5828` n `88` status `ready` deltaP `4.9937` edge `9.6127` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `91.6958` n `88` status `ready` deltaP `7.8298` edge `7.6339` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `39.8842` n `47` status `ready` deltaP `34.9481` edge `3.0907` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `23.4923` n `47` status `ready` deltaP `43.882` edge `1.8617` maxDD `-12.7247`
- `market_context_high->equity_24h` score `17.8908` n `88` status `ready` deltaP `17.9026` edge `1.6107` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.2589` n `53` status `ready` deltaP `33.8012` edge `0.8251` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.5248` n `47` status `ready` deltaP `39.9654` edge `0.2773` maxDD `0.0`
- `news_risk_high->index_24h` score `6.0897` n `47` status `ready` deltaP `31.6609` edge `0.2964` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.0221` n `88` status `ready` deltaP `34.9638` edge `1.0484` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8609` n `88` status `ready` deltaP `35.0071` edge `0.227` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.3559` n `53` status `ready` deltaP `41.823` edge `0.1218` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.927` n `53` status `ready` deltaP `20.8957` edge `0.3367` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5166` n `53` status `ready` deltaP `18.3143` edge `0.2422` maxDD `-3.6997`
- `news_risk_high->crypto_alt_24h` score `3.3923` n `47` status `ready` deltaP `13.5905` edge `0.6452` maxDD `-19.0713`
- `market_context_high->index_24h` score `3.3421` n `88` status `ready` deltaP `18.0245` edge `0.2046` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.586` n `53` status `ready` deltaP `23.6626` edge `0.0831` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.214` n `53` status `ready` deltaP `25.1265` edge `0.2802` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.179` n `53` status `ready` deltaP `20.7461` edge `0.0869` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0947` n `53` status `ready` deltaP `24.9915` edge `0.0334` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3197` n `53` status `ready` deltaP `17.3257` edge `0.0246` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

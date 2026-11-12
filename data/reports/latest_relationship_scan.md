# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T03:22:25.757763+00:00`
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

- `market_context_high->unknown_24h` score `125.124` n `88` status `ready` deltaP `4.9937` edge `10.4078` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `90.8906` n `88` status `ready` deltaP `7.8298` edge `7.5668` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `39.5362` n `47` status `ready` deltaP `34.6021` edge `3.064` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `23.2823` n `47` status `ready` deltaP `43.882` edge `1.8442` maxDD `-12.7247`
- `market_context_high->equity_24h` score `17.5428` n `88` status `ready` deltaP `17.5566` edge `1.584` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.1793` n `53` status `ready` deltaP `33.4963` edge `0.8205` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.5752` n `47` status `ready` deltaP `39.9654` edge `0.2815` maxDD `0.0`
- `news_risk_high->index_24h` score `6.0188` n `47` status `ready` deltaP `31.3149` edge `0.2928` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.9433` n `88` status `ready` deltaP `34.9638` edge `1.0383` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8597` n `88` status `ready` deltaP `35.0071` edge `0.2269` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.3231` n `53` status `ready` deltaP `41.5181` edge `0.1211` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.8654` n `53` status `ready` deltaP `20.5908` edge `0.3336` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5525` n `53` status `ready` deltaP `18.6137` edge `0.2432` maxDD `-3.6997`
- `news_risk_high->crypto_alt_24h` score `3.3135` n `47` status `ready` deltaP `13.5905` edge `0.6351` maxDD `-19.0713`
- `market_context_high->index_24h` score `3.2712` n `88` status `ready` deltaP `17.6785` edge `0.201` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.6164` n `53` status `ready` deltaP `23.9675` edge `0.0836` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.1756` n `53` status `ready` deltaP `24.8216` edge `0.2773` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.145` n `53` status `ready` deltaP `20.4412` edge `0.0861` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.1223` n `53` status `ready` deltaP `25.2909` edge `0.0337` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3209` n `53` status `ready` deltaP `17.3257` edge `0.0247` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

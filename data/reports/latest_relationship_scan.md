# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T06:52:29.952072+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11530`

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

- `market_context_high->unknown_24h` score `191.7164` n `88` status `ready` deltaP `5.8588` edge `15.9514` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `88.2342` n `88` status `ready` deltaP `7.2201` edge `7.3495` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `30.9767` n `52` status `ready` deltaP `23.9486` edge `2.4829` maxDD `-3.2263`
- `market_context_high->equity_24h` score `15.7449` n `88` status `ready` deltaP `16.5185` edge `1.4411` maxDD `-16.7984`
- `news_risk_high->crypto_major_24h` score `12.8937` n `52` status `ready` deltaP `37.9491` edge `1.5966` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3396` n `53` status `ready` deltaP `34.106` edge `0.8298` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.7139` n `52` status `ready` deltaP `40.1384` edge `0.2919` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.4215` n `88` status `ready` deltaP `34.9638` edge `0.9714` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8561` n `88` status `ready` deltaP `35.0071` edge `0.2266` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.2649` n `53` status `ready` deltaP `41.0608` edge `0.1193` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1269` n `52` status `ready` deltaP `21.0074` edge `0.2299` maxDD `-0.4168`
- `news_risk_high->crypto_major_4h` score `4.0238` n `53` status `ready` deltaP `21.5054` edge `0.3407` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.537` n `53` status `ready` deltaP `18.3143` edge `0.2439` maxDD `-3.6997`
- `market_context_high->index_24h` score `2.995` n `88` status `ready` deltaP `16.9864` edge `0.1826` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.7556` n `53` status `ready` deltaP `24.8821` edge `0.0891` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.2377` n `53` status `ready` deltaP `25.4314` edge `0.2812` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.1694` n `53` status `ready` deltaP `20.7461` edge `0.0861` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0911` n `53` status `ready` deltaP `24.9915` edge `0.0331` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3029` n `53` status `ready` deltaP `17.176` edge `0.0242` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7874` n `53` status `ready` deltaP `18.0431` edge `0.0786` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

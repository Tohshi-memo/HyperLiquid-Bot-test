# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T23:22:29.637413+00:00`
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

- `market_context_high->unknown_4h` score `92.0907` n `88` status `ready` deltaP `8.3863` edge `7.6631` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `50.3464` n `36` status `ready` deltaP `37.3702` edge `3.9464` maxDD `0.0`
- `market_context_high->unknown_24h` score `49.098` n `88` status `ready` deltaP `4.9937` edge `4.0723` maxDD `-0.4609`
- `news_risk_high->crypto_major_24h` score `27.866` n `36` status `ready` deltaP `52.4894` edge `2.1688` maxDD `-12.7247`
- `market_context_high->equity_24h` score `21.0186` n `88` status `ready` deltaP `20.3247` edge `1.8552` maxDD `-16.7984`
- `news_risk_high->crypto_alt_24h` score `13.3609` n `36` status `ready` deltaP `27.8931` edge `1.1023` maxDD `-10.9876`
- `news_risk_high->equity_4h` score `11.2028` n `53` status `ready` deltaP `34.1199` edge `0.8183` maxDD `-6.9762`
- `news_risk_high->index_24h` score `7.3694` n `36` status `ready` deltaP `34.083` edge `0.3869` maxDD `0.0`
- `news_risk_high->commodity_24h` score `7.0324` n `36` status `ready` deltaP `39.9654` edge `0.3196` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.7537` n `88` status `ready` deltaP `34.9638` edge `1.1422` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.6727` n `88` status `ready` deltaP `33.45` edge `0.2217` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.17` n `53` status `ready` deltaP `40.7439` edge `0.1135` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.9439` n `88` status `ready` deltaP `20.4466` edge `0.2386` maxDD `-2.3671`
- `news_risk_high->crypto_major_4h` score `3.6586` n `53` status `ready` deltaP `20.2558` edge `0.3186` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6401` n `53` status `ready` deltaP `18.7634` edge `0.2495` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.7039` n `53` status `ready` deltaP `24.4452` edge `0.0877` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2272` n `53` status `ready` deltaP `21.0644` edge `0.0888` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9953` n `53` status `ready` deltaP `24.0933` edge `0.0311` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.958` n `53` status `ready` deltaP `23.8773` edge `0.2557` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3976` n `53` status `ready` deltaP `18.0742` edge `0.0261` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

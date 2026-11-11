# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T15:52:27.829230+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_4h` score `72.4314` n `88` status `ready` deltaP `8.1347` edge `6.0265` maxDD `-0.9161`
- `market_context_high->equity_24h` score `29.3247` n `88` status `ready` deltaP `25.3156` edge `2.5141` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.5518` n `53` status `ready` deltaP `34.8682` edge `0.8424` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.2011` n `88` status `ready` deltaP `39.1887` edge `1.4278` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.2806` n `88` status `ready` deltaP `25.4261` edge `0.3168` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.3705` n `88` status `ready` deltaP `31.2026` edge `0.2115` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.8265` n `53` status `ready` deltaP `20.1335` edge `0.3334` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `3.7008` n `53` status `ready` deltaP `37.2498` edge `0.0977` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.5166` n `53` status `ready` deltaP `18.1646` edge `0.2432` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.7516` n `53` status `ready` deltaP `24.5772` edge `0.0908` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3363` n `53` status `ready` deltaP `21.8132` edge `0.0929` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8848` n `53` status `ready` deltaP `23.1448` edge `0.2512` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.7892` n `53` status `ready` deltaP `21.9975` edge `0.0279` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3425` n `53` status `ready` deltaP `17.4754` edge `0.0255` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7511` n `53` status `ready` deltaP `18.9413` edge `0.0752` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.7382` n `53` status `ready` deltaP `17.8934` edge `0.0733` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.213` n `88` status `ready` deltaP `4.8449` edge `0.0176` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.3146` n `53` status `ready` deltaP `-3.6973` edge `0.0319` maxDD `-0.3438`
- `market_context_high->crypto_major_24h` score `-0.4736` n `88` status `ready` deltaP `17.3927` edge `1.0071` maxDD `-80.6681`
- `market_context_high->commodity_1h` score `-0.5422` n `88` status `ready` deltaP `1.0411` edge `-0.0082` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

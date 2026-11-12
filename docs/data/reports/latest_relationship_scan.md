# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T04:07:27.079126+00:00`
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

- `market_context_high->unknown_24h` score `139.5312` n `88` status `ready` deltaP `4.9937` edge `11.6084` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `89.6996` n `88` status `ready` deltaP `7.3725` edge `7.4706` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `39.0842` n `47` status `ready` deltaP `34.083` edge `3.0298` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `22.9847` n `47` status `ready` deltaP `43.882` edge `1.8194` maxDD `-12.7247`
- `market_context_high->equity_24h` score `17.0908` n `88` status `ready` deltaP `17.0375` edge `1.5498` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.1227` n `53` status `ready` deltaP `33.3438` edge `0.8168` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.6556` n `47` status `ready` deltaP `39.9654` edge `0.2882` maxDD `0.0`
- `news_risk_high->index_24h` score `5.9233` n `47` status `ready` deltaP `30.7958` edge `0.2883` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.838` n `88` status `ready` deltaP `34.9638` edge `1.0248` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8633` n `88` status `ready` deltaP `35.0071` edge `0.2272` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.2769` n `53` status `ready` deltaP `41.0608` edge `0.1203` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.8546` n `53` status `ready` deltaP `20.5908` edge `0.3327` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5669` n `53` status `ready` deltaP `18.6137` edge `0.2444` maxDD `-3.6997`
- `news_risk_high->crypto_alt_24h` score `3.2082` n `47` status `ready` deltaP `13.5905` edge `0.6216` maxDD `-19.0713`
- `market_context_high->index_24h` score `3.1757` n `88` status `ready` deltaP `17.1594` edge `0.1965` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.6164` n `53` status `ready` deltaP `23.9675` edge `0.0836` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.163` n `53` status `ready` deltaP `24.6692` edge `0.2767` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.1259` n `53` status `ready` deltaP `25.2909` edge `0.034` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.111` n `53` status `ready` deltaP `20.1363` edge `0.0853` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.3197` n `53` status `ready` deltaP `17.3257` edge `0.0246` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

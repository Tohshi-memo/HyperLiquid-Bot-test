# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T22:22:29.500709+00:00`
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

- `market_context_high->unknown_4h` score `92.7531` n `88` status `ready` deltaP `8.3863` edge `7.7183` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `53.6094` n `32` status `ready` deltaP `38.0623` edge `4.2137` maxDD `0.0`
- `market_context_high->unknown_24h` score `30.4368` n `88` status `ready` deltaP `4.9937` edge `2.5172` maxDD `-0.4609`
- `news_risk_high->crypto_major_24h` score `29.5774` n `32` status `ready` deltaP `55.266` edge `2.2929` maxDD `-12.7247`
- `market_context_high->equity_24h` score `22.034` n `88` status `ready` deltaP `21.0168` edge `1.9352` maxDD `-16.7984`
- `news_risk_high->crypto_alt_24h` score `16.114` n `32` status `ready` deltaP `35.532` edge `1.2808` maxDD `-10.9876`
- `news_risk_high->equity_4h` score `11.1596` n `53` status `ready` deltaP `34.1199` edge `0.8147` maxDD `-6.9762`
- `news_risk_high->index_24h` score `7.7176` n `32` status `ready` deltaP `34.7751` edge `0.4113` maxDD `0.0`
- `news_risk_high->commodity_24h` score `7.3072` n `32` status `ready` deltaP `39.9654` edge `0.3425` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.9526` n `88` status `ready` deltaP `34.9638` edge `1.1677` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.6054` n `88` status `ready` deltaP `32.7579` edge `0.2207` maxDD `-1.4245`
- `market_context_high->index_24h` score `4.136` n `88` status `ready` deltaP `21.1387` edge `0.25` maxDD `-2.3671`
- `news_risk_high->metal_4h` score `4.0865` n `53` status `ready` deltaP `40.136` edge `0.1106` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.5178` n `53` status `ready` deltaP `18.3143` edge `0.2423` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.4864` n `53` status `ready` deltaP `19.6479` edge `0.3083` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.7123` n `53` status `ready` deltaP `24.4452` edge `0.0884` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2332` n `53` status `ready` deltaP `21.0644` edge `0.0893` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9929` n `53` status `ready` deltaP `24.0933` edge `0.0309` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.8563` n `53` status `ready` deltaP `23.4214` edge `0.2457` maxDD `-10.1088`
- `news_risk_high->metal_24h` score `1.6671` n `32` status `ready` deltaP `20.8261` edge `0.1201` maxDD `-0.617`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

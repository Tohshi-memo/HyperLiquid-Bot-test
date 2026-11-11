# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T22:07:43.793388+00:00`
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

- `market_context_high->unknown_4h` score `92.8408` n `88` status `ready` deltaP `8.5383` edge `7.7246` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `54.078` n `31` status `ready` deltaP `38.2353` edge `4.2516` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `29.6194` n `31` status `ready` deltaP `54.5317` edge `2.3013` maxDD `-12.7247`
- `market_context_high->unknown_24h` score `25.8288` n `88` status `ready` deltaP `4.9937` edge `2.1332` maxDD `-0.4609`
- `market_context_high->equity_24h` score `22.3082` n `88` status `ready` deltaP `21.1898` edge `1.9569` maxDD `-16.7984`
- `news_risk_high->crypto_alt_24h` score `16.2236` n `31` status `ready` deltaP `34.6969` edge `1.2955` maxDD `-10.9876`
- `news_risk_high->equity_4h` score `11.1464` n `53` status `ready` deltaP `34.1199` edge `0.8136` maxDD `-6.9762`
- `news_risk_high->index_24h` score `7.7734` n `31` status `ready` deltaP `34.9481` edge `0.4148` maxDD `0.0`
- `news_risk_high->commodity_24h` score `7.3972` n `31` status `ready` deltaP `39.9654` edge `0.35` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.0217` n `88` status `ready` deltaP `35.1368` edge `1.1754` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.5903` n `88` status `ready` deltaP `32.5849` edge `0.2206` maxDD `-1.4245`
- `market_context_high->index_24h` score `4.1847` n `88` status `ready` deltaP `21.3117` edge `0.2529` maxDD `-2.3671`
- `news_risk_high->metal_4h` score `4.0708` n `53` status `ready` deltaP `39.984` edge `0.1103` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.4878` n `53` status `ready` deltaP `18.1646` edge `0.2408` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.4598` n `53` status `ready` deltaP `19.4959` edge `0.3071` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.7135` n `53` status `ready` deltaP `24.4452` edge `0.0885` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2344` n `53` status `ready` deltaP `21.0644` edge `0.0894` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0061` n `53` status `ready` deltaP `24.243` edge `0.031` maxDD `-0.3692`
- `news_risk_high->metal_24h` score `1.8563` n `31` status `ready` deltaP `22.8708` edge `0.1258` maxDD `-0.5566`
- `news_risk_high->crypto_alt_4h` score `1.839` n `53` status `ready` deltaP `23.2694` edge `0.2445` maxDD `-10.1088`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T07:52:27.089568+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7085`

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

- `market_context_high->unknown_24h` score `1745.6954` n `134` status `ready` deltaP `-2.7908` edge `145.5362` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `34.8033` n `134` status `ready` deltaP `4.0749` edge `2.8864` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.0498` n `134` status `ready` deltaP `33.3541` edge `0.0501` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.4452` n `134` status `ready` deltaP `16.3117` edge `0.2874` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3244` n `134` status `ready` deltaP `10.0054` edge `0.0128` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.2377` n `134` status `ready` deltaP `13.633` edge `0.0508` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.2302` n `134` status `ready` deltaP `14.6114` edge `0.0217` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.0939` n `134` status `ready` deltaP `4.1827` edge `0.0675` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0551` n `134` status `ready` deltaP `6.5667` edge `0.0544` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0715` n `134` status `ready` deltaP `4.1782` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.314` n `134` status `ready` deltaP `1.7942` edge `0.0133` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.4536` n `134` status `ready` deltaP `0.8668` edge `0.0945` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5717` n `134` status `ready` deltaP `-1.3878` edge `-0.0042` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.7978` n `134` status `ready` deltaP `3.4476` edge `0.0612` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8869` n `134` status `ready` deltaP `-2.6946` edge `-0.0001` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.348` n `134` status `ready` deltaP `3.9257` edge `0.0657` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.8366` n `134` status `ready` deltaP `7.5515` edge `0.0437` maxDD `-19.0267`
- `market_context_high->fx_24h` score `-1.8376` n `134` status `ready` deltaP `-2.7985` edge `-0.0014` maxDD `-0.9792`
- `market_context_high->index_4h` score `-2.1059` n `134` status `ready` deltaP `-4.3002` edge `-0.0148` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-3.7585` n `134` status `ready` deltaP `8.5432` edge `0.0202` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

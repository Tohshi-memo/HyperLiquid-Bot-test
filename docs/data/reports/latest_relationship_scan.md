# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T22:07:39.418008+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7058`

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

- `market_context_high->unknown_24h` score `1589.9499` n `134` status `ready` deltaP `-6.0894` edge `132.5794` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `109.4327` n `82` status `ready` deltaP `-0.9676` edge `9.1384` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `36.7846` n `134` status `ready` deltaP `0.4163` edge `3.0759` maxDD `-0.3966`
- `market_context_high->equity_24h` score `6.1853` n `134` status `ready` deltaP `16.6589` edge `0.6801` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.3103` n `70` status `ready` deltaP `20.2656` edge `0.3735` maxDD `-3.6198`
- `market_context_high->index_24h` score `3.6622` n `134` status `ready` deltaP `35.2638` edge `0.0884` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.7884` n `82` status `ready` deltaP `6.4809` edge `0.1054` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.445` n `134` status `ready` deltaP `15.3099` edge `0.0569` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3797` n `134` status `ready` deltaP `10.7539` edge `0.0149` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3762` n `134` status `ready` deltaP `15.6785` edge `0.0333` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2737` n `134` status `ready` deltaP `5.0809` edge `0.0765` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.0874` n `134` status `ready` deltaP `2.3912` edge `0.1537` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.0156` n `134` status `ready` deltaP `7.3152` edge `0.0553` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.052` n `134` status `ready` deltaP `4.4776` edge `-0.0007` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.1846` n `134` status `ready` deltaP `2.9918` edge `0.0161` maxDD `-0.4475`
- `news_risk_high->commodity_4h` score `-0.4165` n `70` status `ready` deltaP `2.6873` edge `0.0179` maxDD `-3.1371`
- `market_context_high->fx_4h` score `-0.4816` n `134` status `ready` deltaP `0.1365` edge `-0.0028` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.7133` n `82` status `ready` deltaP `-5.0716` edge `0.0042` maxDD `-1.6142`
- `market_context_high->index_1h` score `-0.8174` n `134` status `ready` deltaP `-1.9461` edge `0.0007` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-0.8285` n `134` status `ready` deltaP `3.9257` edge `0.1323` maxDD `-10.5088`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

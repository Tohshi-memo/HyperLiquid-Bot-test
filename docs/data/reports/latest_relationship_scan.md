# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T21:07:25.388916+00:00`
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

- `market_context_high->unknown_24h` score `1590.0159` n `134` status `ready` deltaP `-6.0894` edge `132.5849` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `99.5396` n `78` status `ready` deltaP `-0.311` edge `8.3096` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `36.2974` n `134` status `ready` deltaP `0.4163` edge `3.0353` maxDD `-0.3966`
- `market_context_high->equity_24h` score `5.9501` n `134` status `ready` deltaP `16.6589` edge `0.6605` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1183` n `66` status `ready` deltaP `19.2304` edge `0.3644` maxDD `-3.6198`
- `market_context_high->index_24h` score `3.6418` n `134` status `ready` deltaP `35.2638` edge `0.0867` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.4062` n `134` status `ready` deltaP `11.203` edge `0.0153` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.4046` n `134` status `ready` deltaP `16.1358` edge `0.0339` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.3784` n `134` status `ready` deltaP `14.8525` edge `0.0544` maxDD `-1.0837`
- `news_risk_high->crypto_alt_1h` score `0.3115` n `78` status `ready` deltaP `4.6407` edge `0.0919` maxDD `-3.9659`
- `market_context_high->equity_1h` score `0.2821` n `134` status `ready` deltaP `5.0809` edge `0.0772` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.1706` n `134` status `ready` deltaP `3.001` edge `0.1603` maxDD `-6.008`
- `news_risk_high->commodity_4h` score `0.1302` n `66` status `ready` deltaP `5.1737` edge `0.037` maxDD `-1.7171`
- `market_context_high->crypto_major_1h` score `0.0732` n `134` status `ready` deltaP `7.6146` edge `0.0581` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0862` n `134` status `ready` deltaP `3.8788` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2145` n `134` status `ready` deltaP `2.6924` edge `0.0156` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4895` n `134` status `ready` deltaP `-0.0159` edge `-0.0028` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.7364` n `78` status `ready` deltaP `-5.7462` edge `0.0041` maxDD `-1.4833`
- `market_context_high->index_1h` score `-0.7791` n `134` status `ready` deltaP `-1.497` edge `0.0009` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-0.873` n `134` status `ready` deltaP `3.9257` edge `0.1266` maxDD `-10.5088`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

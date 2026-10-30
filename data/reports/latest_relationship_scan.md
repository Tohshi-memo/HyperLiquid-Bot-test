# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T21:22:25.298189+00:00`
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

- `market_context_high->unknown_24h` score `1590.0027` n `134` status `ready` deltaP `-6.0894` edge `132.5838` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `95.2932` n `79` status `ready` deltaP `-1.4307` edge `7.9632` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `36.355` n `134` status `ready` deltaP `0.4163` edge `3.0401` maxDD `-0.3966`
- `market_context_high->equity_24h` score `6.0077` n `134` status `ready` deltaP `16.6589` edge `0.6653` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1236` n `67` status `ready` deltaP `19.5077` edge `0.363` maxDD `-3.6198`
- `market_context_high->index_24h` score `3.6478` n `134` status `ready` deltaP `35.2638` edge `0.0872` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.5826` n `79` status `ready` deltaP `5.1239` edge `0.0973` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.4062` n `134` status `ready` deltaP `11.203` edge `0.0153` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.4038` n `134` status `ready` deltaP `16.1358` edge `0.0338` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.4002` n `134` status `ready` deltaP `15.005` edge `0.0552` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.2821` n `134` status `ready` deltaP `5.0809` edge `0.0772` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.1518` n `134` status `ready` deltaP `2.8486` edge `0.1589` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.0564` n `134` status `ready` deltaP `7.4649` edge `0.0577` maxDD `-5.2213`
- `news_risk_high->commodity_4h` score `-0.0276` n `67` status `ready` deltaP `4.5573` edge `0.0307` maxDD `-2.1699`
- `market_context_high->fx_1h` score `-0.0785` n `134` status `ready` deltaP `4.0285` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.199` n `134` status `ready` deltaP `2.8421` edge `0.0159` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4816` n `134` status `ready` deltaP `0.1365` edge `-0.0028` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.7755` n `79` status `ready` deltaP `-6.132` edge `0.003` maxDD `-1.5904`
- `market_context_high->index_1h` score `-0.7791` n `134` status `ready` deltaP `-1.497` edge `0.0009` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-0.8621` n `134` status `ready` deltaP `3.9257` edge `0.128` maxDD `-10.5088`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

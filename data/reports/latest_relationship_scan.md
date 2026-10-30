# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T11:37:43.447043+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7046`

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

- `market_context_high->unknown_24h` score `1798.0682` n `134` status `ready` deltaP `-2.7908` edge `149.9006` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `256.2464` n `40` status `ready` deltaP `-2.2754` edge `21.3816` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `33.7919` n `134` status `ready` deltaP `3.3127` edge `2.8072` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.1868` n `134` status `ready` deltaP `33.7013` edge `0.0592` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `2.6674` n `40` status `ready` deltaP `16.6916` edge `0.1527` maxDD `-1.669`
- `market_context_high->equity_24h` score `2.2516` n `134` status `ready` deltaP `16.3117` edge `0.3546` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.368` n `134` status `ready` deltaP `10.7539` edge `0.0134` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2932` n `134` status `ready` deltaP `15.3736` edge `0.0247` maxDD `-1.8344`
- `news_risk_high->index_1h` score `0.171` n `40` status `ready` deltaP `9.9551` edge `-0.0018` maxDD `-0.4118`
- `market_context_high->equity_1h` score `0.1178` n `134` status `ready` deltaP `4.3324` edge `0.0685` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.0729` n `134` status `ready` deltaP `12.4135` edge `0.0452` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.0227` n `134` status `ready` deltaP `6.8661` edge `0.0551` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1205` n `134` status `ready` deltaP `3.28` edge `-0.0015` maxDD `-0.1986`
- `news_risk_high->commodity_1h` score `-0.2608` n `40` status `ready` deltaP `-4.5509` edge `0.0271` maxDD `-0.4158`
- `market_context_high->equity_4h` score `-0.3721` n `134` status `ready` deltaP `1.3242` edge `0.1019` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.3727` n `134` status `ready` deltaP `1.1954` edge `0.0124` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.6018` n `134` status `ready` deltaP `-1.8452` edge `-0.005` maxDD `-0.4545`
- `news_risk_high->fx_1h` score `-0.6105` n `40` status `ready` deltaP `-3.6976` edge `-0.0019` maxDD `-0.1376`
- `market_context_high->crypto_alt_1h` score `-0.8711` n `134` status `ready` deltaP `2.6991` edge `0.0568` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.875` n `134` status `ready` deltaP `-2.5449` edge `-0.0001` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

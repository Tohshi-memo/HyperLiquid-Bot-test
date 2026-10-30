# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T22:37:29.742860+00:00`
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

- `market_context_high->unknown_24h` score `1585.7828` n `134` status `ready` deltaP `-6.263` edge `132.2333` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `151.1739` n `84` status `ready` deltaP `-0.6773` edge `12.6149` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `36.9058` n `134` status `ready` deltaP `0.4163` edge `3.086` maxDD `-0.3966`
- `market_context_high->equity_24h` score `6.2957` n `134` status `ready` deltaP `16.6589` edge `0.6893` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.657` n `72` status `ready` deltaP `20.7148` edge `0.3994` maxDD `-3.6198`
- `market_context_high->index_24h` score `3.6718` n `134` status `ready` deltaP `35.2638` edge `0.0892` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.8478` n `84` status `ready` deltaP `7.3139` edge `0.1048` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4546` n `134` status `ready` deltaP `15.3099` edge `0.0577` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3618` n `134` status `ready` deltaP `10.4545` edge `0.0146` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3564` n `134` status `ready` deltaP `15.3736` edge `0.0328` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2378` n `134` status `ready` deltaP `4.7815` edge `0.0755` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.0357` n `134` status `ready` deltaP `2.0864` edge `0.1491` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `-0.0168` n `134` status `ready` deltaP `7.3152` edge `0.0526` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.052` n `134` status `ready` deltaP `4.4776` edge `-0.0007` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.1714` n `134` status `ready` deltaP `3.1415` edge `0.0162` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4816` n `134` status `ready` deltaP `0.1365` edge `-0.0028` maxDD `-0.4545`
- `news_risk_high->commodity_4h` score `-0.6715` n `72` status `ready` deltaP `1.3381` edge `0.0102` maxDD `-3.7504`
- `news_risk_high->commodity_1h` score `-0.6973` n `84` status `ready` deltaP `-4.7477` edge `0.0041` maxDD `-1.6142`
- `market_context_high->metal_24h` score `-0.8067` n `134` status `ready` deltaP `3.9257` edge `0.1351` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.8438` n `134` status `ready` deltaP `-2.2455` edge `0.0005` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

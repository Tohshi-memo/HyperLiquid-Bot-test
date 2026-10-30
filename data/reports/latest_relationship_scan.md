# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T22:22:34.710887+00:00`
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

- `market_context_high->unknown_24h` score `1585.7972` n `134` status `ready` deltaP `-6.263` edge `132.2345` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `130.6232` n `83` status `ready` deltaP `-0.8207` edge `10.9033` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `36.8482` n `134` status `ready` deltaP `0.4163` edge `3.0812` maxDD `-0.3966`
- `market_context_high->equity_24h` score `6.2405` n `134` status `ready` deltaP `16.6589` edge `0.6847` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.4427` n `71` status `ready` deltaP `20.4955` edge `0.383` maxDD `-3.6198`
- `market_context_high->index_24h` score `3.667` n `134` status `ready` deltaP `35.2638` edge `0.0888` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.8067` n `83` status `ready` deltaP `6.9042` edge `0.1041` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4498` n `134` status `ready` deltaP `15.3099` edge `0.0573` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3704` n `134` status `ready` deltaP `10.6042` edge `0.0147` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3667` n `134` status `ready` deltaP `15.5261` edge `0.0331` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2546` n `134` status `ready` deltaP `4.9312` edge `0.0759` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.0623` n `134` status `ready` deltaP `2.2388` edge `0.1515` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `-0.0036` n `134` status `ready` deltaP `7.3152` edge `0.0537` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0434` n `134` status `ready` deltaP `4.6273` edge `-0.0006` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.1846` n `134` status `ready` deltaP `2.9918` edge `0.0161` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4808` n `134` status `ready` deltaP `0.1365` edge `-0.0027` maxDD `-0.4545`
- `news_risk_high->commodity_4h` score `-0.5522` n `71` status `ready` deltaP `2.0032` edge `0.0135` maxDD `-3.4791`
- `news_risk_high->commodity_1h` score `-0.6774` n `83` status `ready` deltaP `-4.381` edge `0.0042` maxDD `-1.6142`
- `market_context_high->metal_24h` score `-0.8176` n `134` status `ready` deltaP `3.9257` edge `0.1337` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.8306` n `134` status `ready` deltaP `-2.0958` edge `0.0006` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

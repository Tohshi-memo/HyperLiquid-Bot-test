# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T23:37:30.787016+00:00`
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

- `market_context_high->unknown_24h` score `1585.658` n `134` status `ready` deltaP `-6.263` edge `132.2229` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `157.3888` n `88` status `ready` deltaP `-0.2858` edge `13.1302` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `37.147` n `134` status `ready` deltaP `0.4163` edge `3.1061` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `6.6453` n `76` status `ready` deltaP `22.1037` edge `0.4725` maxDD `-3.6198`
- `market_context_high->equity_24h` score `6.5594` n `134` status `ready` deltaP `17.1798` edge `0.7078` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.7326` n `134` status `ready` deltaP `35.7846` edge `0.0908` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.2231` n `88` status `ready` deltaP `9.1249` edge `0.124` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.457` n `134` status `ready` deltaP `15.3099` edge `0.0579` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3626` n `134` status `ready` deltaP `10.4545` edge `0.0147` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3367` n `134` status `ready` deltaP `15.0688` edge `0.0323` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2114` n `134` status `ready` deltaP `4.4821` edge `0.0753` maxDD `-2.3383`
- `market_context_high->equity_4h` score `-0.0049` n `134` status `ready` deltaP `2.0864` edge `0.1439` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `-0.0515` n `134` status `ready` deltaP `7.0158` edge `0.0517` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0683` n `134` status `ready` deltaP `4.1782` edge `-0.0008` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.1714` n `134` status `ready` deltaP `3.1415` edge `0.0162` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4808` n `134` status `ready` deltaP `0.1365` edge `-0.0027` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.7434` n `88` status `ready` deltaP `-5.5593` edge `0.0036` maxDD `-1.6142`
- `market_context_high->metal_24h` score `-0.7615` n `134` status `ready` deltaP `3.9257` edge `0.1409` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.8558` n `134` status `ready` deltaP `-2.3952` edge `0.0005` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-1.0235` n `88` status `ready` deltaP `-0.1225` edge `-0.0045` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

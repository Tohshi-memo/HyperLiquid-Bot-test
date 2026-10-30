# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T06:22:28.240969+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7087`

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

- `market_context_high->unknown_24h` score `1723.2998` n `134` status `ready` deltaP `-2.7908` edge `143.6699` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `35.1589` n `134` status `ready` deltaP `4.3798` edge `2.914` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.0198` n `134` status `ready` deltaP `33.3541` edge `0.0476` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.216` n `134` status `ready` deltaP `16.3117` edge `0.2683` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3112` n `134` status `ready` deltaP `9.8557` edge `0.0121` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1951` n `134` status `ready` deltaP `13.1757` edge `0.0503` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.1947` n `134` status `ready` deltaP `14.1541` edge `0.0202` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.0483` n `134` status `ready` deltaP `3.8833` edge `0.0657` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.0621` n `134` status `ready` deltaP `4.3279` edge `-0.001` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.0779` n `134` status `ready` deltaP `6.7164` edge `0.0515` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.308` n `134` status `ready` deltaP `1.7942` edge `0.0138` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.3704` n `134` status `ready` deltaP `1.4766` edge `0.1011` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.571` n `134` status `ready` deltaP `-1.3878` edge `-0.0041` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.783` n `134` status `ready` deltaP `3.747` edge `0.0611` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8342` n `134` status `ready` deltaP `-2.0958` edge `0.0003` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.3925` n `134` status `ready` deltaP `3.9257` edge `0.06` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.7033` n `134` status `ready` deltaP `8.3137` edge `0.0557` maxDD `-19.0267`
- `market_context_high->fx_24h` score `-1.7338` n `134` status `ready` deltaP `-1.7568` edge `0.0003` maxDD `-0.9792`
- `market_context_high->index_4h` score `-2.0112` n `134` status `ready` deltaP `-3.3855` edge `-0.013` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-3.8188` n `134` status `ready` deltaP `7.8488` edge `0.0171` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

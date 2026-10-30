# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T04:07:29.804277+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6624`

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

- `market_context_high->unknown_24h` score `1689.491` n `134` status `ready` deltaP `-2.7908` edge `140.8525` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `36.1085` n `134` status `ready` deltaP `4.6846` edge `2.9911` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.8982` n `134` status `ready` deltaP `32.6596` edge `0.0421` maxDD `-0.1315`
- `market_context_high->equity_24h` score `0.6161` n `134` status `ready` deltaP `15.4437` edge `0.2241` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3057` n `134` status `ready` deltaP `9.8557` edge `0.0114` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.1585` n `134` status `ready` deltaP `13.6968` edge `0.0186` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1307` n `134` status `ready` deltaP `12.566` edge `0.049` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.0359` n `134` status `ready` deltaP `6.7164` edge `0.055` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.0824` n `134` status `ready` deltaP `3.1348` edge `0.0598` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1174` n `134` status `ready` deltaP `3.28` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3499` n `134` status `ready` deltaP `1.3451` edge `0.0133` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.3759` n `134` status `ready` deltaP `1.4766` edge `0.1004` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.571` n `134` status `ready` deltaP `-1.3878` edge `-0.0041` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.7362` n `134` status `ready` deltaP `3.747` edge `0.0671` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8869` n `134` status `ready` deltaP `-2.6946` edge `-0.0001` maxDD `-1.1344`
- `market_context_high->crypto_major_4h` score `-1.4504` n `134` status `ready` deltaP `8.6185` edge `0.0861` maxDD `-19.0267`
- `market_context_high->metal_24h` score `-1.4525` n `134` status `ready` deltaP `3.9257` edge `0.0523` maxDD `-10.5088`
- `market_context_high->fx_24h` score `-1.574` n `134` status `ready` deltaP `-0.1943` edge `0.0032` maxDD `-0.9792`
- `market_context_high->index_4h` score `-1.9942` n `134` status `ready` deltaP `-3.2331` edge `-0.0126` maxDD `-3.5621`
- `market_context_high->crypto_alt_4h` score `-3.7902` n `134` status `ready` deltaP `1.5563` edge `0.0912` maxDD `-37.0003`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T00:22:26.897962+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6714`

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

- `market_context_high->unknown_24h` score `1635.0758` n `134` status `ready` deltaP `-2.7908` edge `136.3179` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `48.015` n `134` status `ready` deltaP `5.7517` edge `3.9762` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.5989` n `134` status `ready` deltaP `30.4027` edge `0.0322` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2894` n `134` status `ready` deltaP `9.706` edge `0.0103` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1169` n `134` status `ready` deltaP `12.1086` edge `0.0509` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0523` n `134` status `ready` deltaP `12.6297` edge `0.0121` maxDD `-1.8344`
- `market_context_high->crypto_major_1h` score `-0.0251` n `134` status `ready` deltaP `6.5667` edge `0.0569` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1454` n `134` status `ready` deltaP `2.8309` edge `-0.0017` maxDD `-0.1986`
- `market_context_high->equity_1h` score `-0.1879` n `134` status `ready` deltaP `2.6857` edge `0.054` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.3595` n `134` status `ready` deltaP `1.1954` edge `0.0135` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.6081` n `134` status `ready` deltaP `-1.9976` edge `-0.0048` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8041` n `134` status `ready` deltaP `3.4476` edge `0.0604` maxDD `-8.251`
- `market_context_high->equity_24h` score `-0.8342` n `134` status `ready` deltaP `12.8395` edge `0.1206` maxDD `-14.0571`
- `market_context_high->equity_4h` score `-0.8425` n `134` status `ready` deltaP `-0.6575` edge `0.0548` maxDD `-6.008`
- `market_context_high->index_1h` score `-0.9253` n `134` status `ready` deltaP `-2.994` edge `-0.0013` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.3299` n `134` status `ready` deltaP `2.0626` edge `0.0085` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.568` n `134` status `ready` deltaP `3.9257` edge `0.0375` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.8605` n `134` status `ready` deltaP `6.9417` edge `0.0447` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.2527` n `134` status `ready` deltaP `-5.5197` edge `-0.0189` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.125` n `134` status `ready` deltaP `4.3766` edge `0.001` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

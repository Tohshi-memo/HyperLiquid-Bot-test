# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T21:22:27.590908+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6816`

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

- `market_context_high->unknown_24h` score `1613.6495` n `134` status `ready` deltaP `-2.2699` edge `134.5289` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `60.9222` n `134` status `ready` deltaP `5.7517` edge `5.0518` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.3422` n `134` status `ready` deltaP `28.3193` edge `0.0247` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3034` n `134` status `ready` deltaP `10.0054` edge `0.0101` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.0918` n `134` status `ready` deltaP `13.2395` edge `0.0131` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.0308` n `134` status `ready` deltaP `11.3464` edge `0.0488` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.1182` n `134` status `ready` deltaP `3.28` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.1882` n `134` status `ready` deltaP `5.9679` edge `0.0473` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.3138` n `134` status `ready` deltaP `2.0869` edge `0.0475` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.3978` n `134` status `ready` deltaP `0.7463` edge `0.0133` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5385` n `134` status `ready` deltaP `-0.7781` edge `-0.004` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.96` n `134` status `ready` deltaP `2.6991` edge `0.0454` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.9792` n `134` status `ready` deltaP `-3.5928` edge `-0.0018` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.1308` n `134` status `ready` deltaP `4.1459` edge `0.0112` maxDD `-0.9792`
- `market_context_high->equity_4h` score `-1.383` n `134` status `ready` deltaP `-2.4868` edge `-0.0023` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.6366` n `134` status `ready` deltaP `3.9257` edge `0.0287` maxDD `-10.5088`
- `market_context_high->equity_24h` score `-2.1745` n `134` status `ready` deltaP `10.7562` edge `0.0228` maxDD `-14.0571`
- `market_context_high->index_4h` score `-2.4092` n `134` status `ready` deltaP `-6.8916` edge `-0.0228` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.4898` n `134` status `ready` deltaP `5.2649` edge `-0.0248` maxDD `-19.0267`
- `market_context_high->commodity_24h` score `-4.3526` n `134` status `ready` deltaP `2.2932` edge `-0.0143` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

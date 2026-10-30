# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T07:22:27.797791+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7085`

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

- `market_context_high->unknown_24h` score `1738.3766` n `134` status `ready` deltaP `-2.7908` edge `144.9263` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `34.8081` n `134` status `ready` deltaP `4.0749` edge `2.8868` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.0402` n `134` status `ready` deltaP `33.3541` edge `0.0493` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.3684` n `134` status `ready` deltaP `16.3117` edge `0.281` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3143` n `134` status `ready` deltaP `9.8557` edge `0.0125` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.2571` n `134` status `ready` deltaP `13.7855` edge `0.0514` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.2081` n `134` status `ready` deltaP `14.3066` edge `0.0209` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.0435` n `134` status `ready` deltaP `3.8833` edge `0.0653` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.0629` n `134` status `ready` deltaP `4.3279` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.1078` n `134` status `ready` deltaP `6.417` edge `0.051` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.2924` n `134` status `ready` deltaP `1.9439` edge `0.0141` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.4427` n `134` status `ready` deltaP `0.8668` edge `0.0959` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.571` n `134` status `ready` deltaP `-1.3878` edge `-0.0041` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8165` n `134` status `ready` deltaP `3.2979` edge `0.0598` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8881` n `134` status `ready` deltaP `-2.6946` edge `-0.0002` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.3644` n `134` status `ready` deltaP `3.9257` edge `0.0636` maxDD `-10.5088`
- `market_context_high->fx_24h` score `-1.8038` n `134` status `ready` deltaP `-2.4513` edge `-0.0009` maxDD `-0.9792`
- `market_context_high->crypto_major_4h` score `-1.8263` n `134` status `ready` deltaP `7.7039` edge `0.044` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.0743` n `134` status `ready` deltaP `-3.9953` edge `-0.0142` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-3.764` n `134` status `ready` deltaP `8.5432` edge `0.0195` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

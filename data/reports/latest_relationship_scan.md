# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T07:42:38.867368+00:00`
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

- `market_context_high->unknown_24h` score `1742.0186` n `134` status `ready` deltaP `-2.7908` edge `145.2298` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `34.8021` n `134` status `ready` deltaP `4.0749` edge `2.8863` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.045` n `134` status `ready` deltaP `33.3541` edge `0.0497` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.4056` n `134` status `ready` deltaP `16.3117` edge `0.2841` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3237` n `134` status `ready` deltaP `10.0054` edge `0.0127` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.2413` n `134` status `ready` deltaP `13.633` edge `0.0511` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.2192` n `134` status `ready` deltaP `14.459` edge `0.0213` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.0699` n `134` status `ready` deltaP `4.033` edge `0.0665` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.0629` n `134` status `ready` deltaP `4.3279` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.0743` n `134` status `ready` deltaP `6.5667` edge `0.0528` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.3092` n `134` status `ready` deltaP `1.7942` edge `0.0137` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.4497` n `134` status `ready` deltaP `0.8668` edge `0.095` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5717` n `134` status `ready` deltaP `-1.3878` edge `-0.0042` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8017` n `134` status `ready` deltaP `3.4476` edge `0.0607` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8869` n `134` status `ready` deltaP `-2.6946` edge `-0.0001` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.3558` n `134` status `ready` deltaP `3.9257` edge `0.0647` maxDD `-10.5088`
- `market_context_high->fx_24h` score `-1.8213` n `134` status `ready` deltaP `-2.6249` edge `-0.0012` maxDD `-0.9792`
- `market_context_high->crypto_major_4h` score `-1.8389` n `134` status `ready` deltaP `7.5515` edge `0.0434` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.0901` n `134` status `ready` deltaP `-4.1477` edge `-0.0145` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-3.7616` n `134` status `ready` deltaP `8.5432` edge `0.0198` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

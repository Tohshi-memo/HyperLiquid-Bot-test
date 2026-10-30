# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T07:07:23.881465+00:00`
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

- `market_context_high->unknown_24h` score `1734.6158` n `134` status `ready` deltaP `-2.7908` edge `144.6129` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `34.9473` n `134` status `ready` deltaP `4.0749` edge `2.8984` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.0354` n `134` status `ready` deltaP `33.3541` edge `0.0489` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.33` n `134` status `ready` deltaP `16.3117` edge `0.2778` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3135` n `134` status `ready` deltaP `9.8557` edge `0.0124` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.2425` n `134` status `ready` deltaP `13.633` edge `0.0512` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.1971` n `134` status `ready` deltaP `14.1541` edge `0.0205` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.0291` n `134` status `ready` deltaP `3.7336` edge `0.0651` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.0629` n `134` status `ready` deltaP `4.3279` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.1126` n `134` status `ready` deltaP `6.417` edge `0.0506` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.2924` n `134` status `ready` deltaP `1.9439` edge `0.0141` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.4254` n `134` status `ready` deltaP `1.0193` edge `0.0971` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.571` n `134` status `ready` deltaP `-1.3878` edge `-0.0041` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.808` n `134` status `ready` deltaP `3.4476` edge `0.0599` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.875` n `134` status `ready` deltaP `-2.5449` edge `-0.0001` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.3722` n `134` status `ready` deltaP `3.9257` edge `0.0626` maxDD `-10.5088`
- `market_context_high->fx_24h` score `-1.7863` n `134` status `ready` deltaP `-2.2777` edge `-0.0006` maxDD `-0.9792`
- `market_context_high->crypto_major_4h` score `-1.7965` n `134` status `ready` deltaP `7.8563` edge `0.0468` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.0597` n `134` status `ready` deltaP `-3.8429` edge `-0.014` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-3.7777` n `134` status `ready` deltaP `8.3696` edge `0.0189` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T23:37:24.741660+00:00`
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

- `market_context_high->unknown_24h` score `1624.4726` n `134` status `ready` deltaP `-2.7908` edge `135.4343` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `54.0054` n `134` status `ready` deltaP `5.7517` edge `4.4754` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.5308` n `134` status `ready` deltaP `29.8818` edge `0.03` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.28` n `134` status `ready` deltaP `9.5563` edge `0.0101` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.0743` n `134` status `ready` deltaP `11.6513` edge `0.0504` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0404` n `134` status `ready` deltaP `12.4773` edge `0.0116` maxDD `-1.8344`
- `market_context_high->crypto_major_1h` score `-0.1426` n `134` status `ready` deltaP `6.1176` edge `0.0501` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1439` n `134` status `ready` deltaP `2.8309` edge `-0.0015` maxDD `-0.1986`
- `market_context_high->equity_1h` score `-0.249` n `134` status `ready` deltaP `2.3863` edge `0.0509` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.3439` n `134` status `ready` deltaP `1.3451` edge `0.0138` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5994` n `134` status `ready` deltaP `-1.8452` edge `-0.0047` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8891` n `134` status `ready` deltaP `2.9985` edge `0.0525` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.9397` n `134` status `ready` deltaP `-3.1437` edge `-0.0015` maxDD `-1.1344`
- `market_context_high->equity_4h` score `-0.9833` n `134` status `ready` deltaP `-1.1149` edge `0.0398` maxDD `-6.008`
- `market_context_high->equity_24h` score `-1.1975` n `134` status `ready` deltaP `12.3187` edge `0.0938` maxDD `-14.0571`
- `market_context_high->fx_24h` score `-1.2774` n `134` status `ready` deltaP `2.5834` edge `0.0094` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.5867` n `134` status `ready` deltaP `3.9257` edge `0.0351` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-2.0512` n `134` status `ready` deltaP `6.4844` edge `0.0233` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.3037` n `134` status `ready` deltaP `-5.977` edge `-0.0201` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.1801` n `134` status `ready` deltaP `3.8557` edge `-0.0026` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

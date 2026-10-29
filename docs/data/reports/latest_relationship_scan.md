# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T21:07:27.624599+00:00`
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

- `market_context_high->unknown_24h` score `1614.2819` n `134` status `ready` deltaP `-2.2699` edge `134.5816` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `61.461` n `134` status `ready` deltaP `5.7517` edge `5.0967` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.3199` n `134` status `ready` deltaP `28.1457` edge `0.024` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2948` n `134` status `ready` deltaP `9.8557` edge `0.01` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.0918` n `134` status `ready` deltaP `13.2395` edge `0.0131` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.032` n `134` status `ready` deltaP `11.3464` edge `0.0489` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.1189` n `134` status `ready` deltaP `3.28` edge `-0.0013` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.2313` n `134` status `ready` deltaP `5.8182` edge `0.0447` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.3462` n `134` status `ready` deltaP `1.9372` edge `0.0458` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.411` n `134` status `ready` deltaP `0.5966` edge `0.0132` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5298` n `134` status `ready` deltaP `-0.6257` edge `-0.0039` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.9924` n `134` status `ready` deltaP `-3.7425` edge `-0.0019` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.9998` n `134` status `ready` deltaP `2.5494` edge `0.0413` maxDD `-8.251`
- `market_context_high->fx_24h` score `-1.1145` n `134` status `ready` deltaP `4.3196` edge `0.0114` maxDD `-0.9792`
- `market_context_high->equity_4h` score `-1.4284` n `134` status `ready` deltaP `-2.6392` edge `-0.0071` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.6429` n `134` status `ready` deltaP `3.9257` edge `0.0279` maxDD `-10.5088`
- `market_context_high->equity_24h` score `-2.2832` n `134` status `ready` deltaP `10.5825` edge `0.0149` maxDD `-14.0571`
- `market_context_high->index_4h` score `-2.425` n `134` status `ready` deltaP `-7.0441` edge `-0.0231` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.5351` n `134` status `ready` deltaP `5.1124` edge `-0.0296` maxDD `-19.0267`
- `market_context_high->commodity_24h` score `-4.3702` n `134` status `ready` deltaP `2.1196` edge `-0.0154` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

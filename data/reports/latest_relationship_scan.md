# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T16:37:32.635157+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10784`

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

- `risk_on_high->unknown_4h` score `19.9526` n `133` status `ready` deltaP `7.6265` edge `1.6737` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.9526` n `133` status `ready` deltaP `7.6265` edge `1.6737` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.4765` n `133` status `ready` deltaP `-1.5027` edge `1.0241` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.4765` n `133` status `ready` deltaP `-1.5027` edge `1.0241` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.6115` n `211` status `ready` deltaP `9.3298` edge `0.8083` maxDD `-2.563`
- `market_context_high->unknown_1h` score `9.301` n `212` status `ready` deltaP `-0.8785` edge `0.844` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `2.6384` n `52` status `ready` deltaP `19.3242` edge `0.118` maxDD `-0.8236`
- `news_risk_high->commodity_4h` score `1.4683` n `52` status `ready` deltaP `11.1515` edge `0.0681` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `1.2944` n `52` status `ready` deltaP `9.0678` edge `0.0647` maxDD `-0.0495`
- `news_risk_high->equity_1h` score `0.7` n `52` status `ready` deltaP `11.2967` edge `0.0535` maxDD `-0.7924`
- `news_risk_high->index_1h` score `0.5345` n `52` status `ready` deltaP `11.0663` edge `0.0085` maxDD `-0.1`
- `news_risk_high->metal_4h` score `0.3758` n `52` status `ready` deltaP `8.431` edge `0.0278` maxDD `-0.8659`
- `risk_on_high->metal_1h` score `0.1109` n `133` status `ready` deltaP `12.5625` edge `0.0017` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1109` n `133` status `ready` deltaP `12.5625` edge `0.0017` maxDD `-1.699`
- `news_risk_high->fx_4h` score `0.0752` n `52` status `ready` deltaP `7.9854` edge `-0.0004` maxDD `-1.0591`
- `news_risk_high->crypto_major_4h` score `0.068` n `52` status `ready` deltaP `4.1276` edge `0.0759` maxDD `-5.2426`
- `news_risk_high->metal_1h` score `-0.121` n `52` status `ready` deltaP `2.4989` edge `0.0028` maxDD `-0.7973`
- `market_context_high->equity_24h` score `-0.1473` n `167` status `ready` deltaP `12.4636` edge `0.3392` maxDD `-20.7654`
- `news_risk_high->equity_24h` score `-0.1504` n `52` status `ready` deltaP `2.8712` edge `0.0749` maxDD `-5.0655`
- `news_risk_high->commodity_1h` score `-0.1562` n `52` status `ready` deltaP `4.9517` edge `-0.0014` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

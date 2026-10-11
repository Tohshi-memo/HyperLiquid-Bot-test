# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T19:07:24.988618+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8206`

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

- `market_context_high->unknown_24h` score `1380.965` n `40` status `ready` deltaP `-21.5278` edge `115.2603` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `56.6783` n `85` status `ready` deltaP `-5.2134` edge `4.816` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.7924` n `40` status `ready` deltaP `27.6736` edge `0.5911` maxDD `-1.0977`
- `market_context_high->unknown_1h` score `8.3936` n `97` status `ready` deltaP `-1.4569` edge `0.7428` maxDD `-1.0231`
- `market_context_high->index_24h` score `6.3904` n `40` status `ready` deltaP `52.4306` edge `0.183` maxDD `0.0`
- `market_context_high->fx_24h` score `3.2179` n `40` status `ready` deltaP `36.4236` edge `0.0383` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.4963` n `40` status `ready` deltaP `-20.9375` edge `0.5791` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.7986` n `85` status `ready` deltaP `13.0524` edge `0.0079` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.394` n `85` status `ready` deltaP `10.7658` edge `0.0144` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.3256` n `97` status `ready` deltaP `5.1531` edge `0.0962` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.1882` n `85` status `ready` deltaP `1.589` edge `0.2241` maxDD `-11.1784`
- `market_context_high->commodity_1h` score `0.0626` n `97` status `ready` deltaP `4.2719` edge `0.0051` maxDD `-0.6025`
- `market_context_high->fx_1h` score `0.0068` n `97` status `ready` deltaP `3.5234` edge `0.0013` maxDD `-0.271`
- `market_context_high->metal_4h` score `-0.0753` n `85` status `ready` deltaP `6.6894` edge `0.0214` maxDD `-1.1153`
- `market_context_high->crypto_alt_4h` score `-0.1341` n `85` status `ready` deltaP `-2.2417` edge `0.2536` maxDD `-13.8008`
- `market_context_high->crypto_major_1h` score `-0.1908` n `97` status `ready` deltaP `0.6482` edge `0.0601` maxDD `-3.7778`
- `market_context_high->metal_1h` score `-0.3213` n `97` status `ready` deltaP `4.3058` edge `0.0034` maxDD `-0.7107`
- `market_context_high->index_4h` score `-0.6265` n `85` status `ready` deltaP `-2.3081` edge `0.0051` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.7165` n `97` status `ready` deltaP `-3.7919` edge `-0.0015` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-0.9791` n `97` status `ready` deltaP `-6.0713` edge `0.0019` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T01:37:31.000966+00:00`
- Price records: `672`
- Market context records: `6980`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11735`

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

- `market_context_high->fx_1h` score `-0.2499` n `237` status `ready` deltaP `2.1842` edge `0.0019` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3777` n `237` status `ready` deltaP `1.9809` edge `0.0248` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.699` n `237` status `ready` deltaP `0.2103` edge `0.0001` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7255` n `237` status `ready` deltaP `-2.0901` edge `-0.0023` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9077` n `237` status `ready` deltaP `12.2401` edge `0.0084` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.216` n `237` status `ready` deltaP `2.43` edge `0.0177` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2742` n `237` status `ready` deltaP `-2.6744` edge `-0.0162` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.5673` n `237` status `ready` deltaP `-1.9809` edge `-0.0273` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `-1.5959` n `224` status `ready` deltaP `-9.0278` edge `0.3106` maxDD `-18.7342`
- `market_context_high->commodity_4h` score `-1.6679` n `237` status `ready` deltaP `-4.4329` edge `-0.0353` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.8095` n `237` status `ready` deltaP `7.6669` edge `-0.0132` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.9243` n `237` status `ready` deltaP `3.1367` edge `-0.0122` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.9739` n `237` status `ready` deltaP `5.6332` edge `0.0077` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.859` n `237` status `ready` deltaP `1.1256` edge `0.0045` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-2.9878` n `237` status `ready` deltaP `-7.0386` edge `0.0345` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.5` n `237` status `ready` deltaP `-0.1293` edge `-0.0194` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.8005` n `224` status `ready` deltaP `-6.4485` edge `-0.0869` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4377` n `224` status `ready` deltaP `-7.3661` edge `-0.016` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.5024` n `237` status `ready` deltaP `5.2305` edge `-0.075` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.0901` n `224` status `ready` deltaP `-4.1418` edge `-0.1154` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

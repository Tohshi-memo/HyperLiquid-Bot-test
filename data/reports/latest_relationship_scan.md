# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T05:07:28.856980+00:00`
- Price records: `672`
- Market context records: `6995`
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

- `market_context_high->fx_1h` score `-0.2266` n `237` status `ready` deltaP `2.6333` edge `0.0019` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.2944` n `237` status `ready` deltaP `2.5797` edge `0.0315` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6305` n `237` status `ready` deltaP `1.2582` edge `0.0019` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.678` n `237` status `ready` deltaP `-1.4913` edge `-0.0002` maxDD `-2.1427`
- `market_context_high->unknown_24h` score `-0.7207` n `224` status `ready` deltaP `-6.5972` edge `0.4066` maxDD `-18.7342`
- `market_context_high->fx_4h` score `-0.9147` n `237` status `ready` deltaP `12.2401` edge `0.0075` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-0.9858` n `237` status `ready` deltaP `3.6276` edge `0.0289` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2286` n `237` status `ready` deltaP `-2.2253` edge `-0.0154` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.3765` n `237` status `ready` deltaP `-1.8312` edge `-0.0124` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6694` n `237` status `ready` deltaP `-4.2805` edge `-0.0365` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7577` n `237` status `ready` deltaP `8.1243` edge `-0.0096` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8081` n `237` status `ready` deltaP `4.0349` edge `-0.0033` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8894` n `237` status `ready` deltaP `6.8527` edge `0.0104` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.7118` n `237` status `ready` deltaP `-6.124` edge `0.0514` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.7559` n `237` status `ready` deltaP `1.2781` edge `0.0167` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.2861` n `237` status `ready` deltaP `0.9378` edge `0.0009` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.8713` n `224` status `ready` deltaP `-6.4485` edge `-0.0928` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4461` n `224` status `ready` deltaP `-7.3661` edge `-0.0167` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.314` n `237` status `ready` deltaP `5.6878` edge `-0.0539` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.8331` n `224` status `ready` deltaP `-1.8849` edge `-0.0975` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

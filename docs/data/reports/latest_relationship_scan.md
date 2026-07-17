# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T02:22:32.062365+00:00`
- Price records: `672`
- Market context records: `6983`
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

- `market_context_high->fx_1h` score `-0.2421` n `237` status `ready` deltaP `2.3339` edge `0.0019` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3037` n `237` status `ready` deltaP `2.43` edge `0.0313` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.678` n `237` status `ready` deltaP `0.5097` edge `0.0008` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6952` n `237` status `ready` deltaP `-1.641` edge `-0.0014` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8831` n `237` status `ready` deltaP `12.6974` edge `0.0085` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.0901` n `237` status `ready` deltaP `2.8791` edge `0.0252` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2334` n `237` status `ready` deltaP `-2.2253` edge `-0.0158` maxDD `-2.4388`
- `market_context_high->unknown_24h` score `-1.4658` n `224` status `ready` deltaP `-8.5069` edge `0.3238` maxDD `-18.7342`
- `market_context_high->unknown_1h` score `-1.5445` n `237` status `ready` deltaP `-1.9809` edge `-0.0254` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6671` n `237` status `ready` deltaP `-4.4329` edge `-0.0352` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7741` n `237` status `ready` deltaP `8.1243` edge `-0.0117` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8674` n `237` status `ready` deltaP `3.5858` edge `-0.0079` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.9416` n `237` status `ready` deltaP `6.0905` edge `0.0088` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.758` n `237` status `ready` deltaP `1.583` edge `0.0144` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-2.8168` n `237` status `ready` deltaP `-6.5813` edge `0.0457` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.3888` n `237` status `ready` deltaP `0.328` edge `-0.0082` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.8101` n `224` status `ready` deltaP `-6.4485` edge `-0.0877` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4377` n `224` status `ready` deltaP `-7.3661` edge `-0.016` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.4107` n `237` status `ready` deltaP `5.6878` edge `-0.0663` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.0341` n `224` status `ready` deltaP `-3.621` edge `-0.1117` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

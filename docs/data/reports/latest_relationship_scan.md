# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T04:22:24.853322+00:00`
- Price records: `672`
- Market context records: `6991`
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

- `market_context_high->fx_1h` score `-0.2507` n `237` status `ready` deltaP `2.1842` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.2983` n `237` status `ready` deltaP `2.5797` edge `0.031` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6414` n `237` status `ready` deltaP `1.1085` edge `0.0015` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6811` n `237` status `ready` deltaP `-1.4913` edge `-0.0006` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8965` n `237` status `ready` deltaP `12.545` edge `0.0078` maxDD `-2.1765`
- `market_context_high->unknown_24h` score `-0.9014` n `224` status `ready` deltaP `-7.1181` edge `0.3869` maxDD `-18.7342`
- `market_context_high->crypto_major_1h` score `-1.0242` n `237` status `ready` deltaP `3.3282` edge `0.0277` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.1891` n `237` status `ready` deltaP `-1.7762` edge `-0.0151` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.3885` n `237` status `ready` deltaP `-1.9809` edge `-0.0124` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6608` n `237` status `ready` deltaP `-4.2805` edge `-0.0354` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7616` n `237` status `ready` deltaP `8.1243` edge `-0.0101` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.837` n `237` status `ready` deltaP `3.7355` edge `-0.005` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8918` n `237` status `ready` deltaP `6.8527` edge `0.0101` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.6754` n `237` status `ready` deltaP `-5.8191` edge `0.0524` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.7487` n `237` status `ready` deltaP `1.4305` edge `0.0166` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.301` n `237` status `ready` deltaP `0.9378` edge `-0.001` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.8521` n `224` status `ready` deltaP `-6.4485` edge `-0.0912` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4437` n `224` status `ready` deltaP `-7.3661` edge `-0.0165` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.3296` n `237` status `ready` deltaP `5.6878` edge `-0.0559` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.8839` n `224` status `ready` deltaP `-2.2321` edge `-0.1017` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

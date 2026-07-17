# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T01:52:30.340436+00:00`
- Price records: `672`
- Market context records: `6981`
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
- `market_context_high->crypto_alt_1h` score `-0.3497` n `237` status `ready` deltaP `2.1306` edge `0.0274` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6889` n `237` status `ready` deltaP `0.36` edge `0.0004` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7154` n `237` status `ready` deltaP `-1.9404` edge `-0.002` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8998` n `237` status `ready` deltaP `12.3925` edge `0.0084` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.1669` n `237` status `ready` deltaP `2.5797` edge `0.0208` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2622` n `237` status `ready` deltaP `-2.5247` edge `-0.0162` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.5493` n `237` status `ready` deltaP `-1.9809` edge `-0.0258` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `-1.5626` n `224` status `ready` deltaP `-8.8542` edge `0.3137` maxDD `-18.7342`
- `market_context_high->commodity_4h` score `-1.6766` n `237` status `ready` deltaP `-4.5853` edge `-0.0354` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7969` n `237` status `ready` deltaP `7.8194` edge `-0.0126` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.9032` n `237` status `ready` deltaP `3.2864` edge `-0.0105` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.9621` n `237` status `ready` deltaP `5.7856` edge `0.0082` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.8222` n `237` status `ready` deltaP `1.2781` edge `0.0082` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-2.912` n `237` status `ready` deltaP `-6.8862` edge `0.0398` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.4577` n `237` status `ready` deltaP `0.0231` edge `-0.015` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.8041` n `224` status `ready` deltaP `-6.4485` edge `-0.0872` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4377` n `224` status `ready` deltaP `-7.3661` edge `-0.016` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.4695` n `237` status `ready` deltaP `5.383` edge `-0.0718` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.0709` n `224` status `ready` deltaP `-3.9682` edge `-0.1141` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

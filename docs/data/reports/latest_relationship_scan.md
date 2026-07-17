# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T02:07:25.803548+00:00`
- Price records: `672`
- Market context records: `6982`
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
- `market_context_high->crypto_alt_1h` score `-0.3255` n `237` status `ready` deltaP `2.2803` edge `0.0295` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6795` n `237` status `ready` deltaP `0.5097` edge `0.0006` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7053` n `237` status `ready` deltaP `-1.7907` edge `-0.0017` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8911` n `237` status `ready` deltaP `12.545` edge `0.0085` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.1261` n `237` status `ready` deltaP `2.7294` edge `0.0232` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2478` n `237` status `ready` deltaP `-2.375` edge `-0.016` maxDD `-2.4388`
- `market_context_high->unknown_24h` score `-1.5302` n `224` status `ready` deltaP `-8.6806` edge `0.3167` maxDD `-18.7342`
- `market_context_high->unknown_1h` score `-1.5421` n `237` status `ready` deltaP `-1.9809` edge `-0.0252` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6758` n `237` status `ready` deltaP `-4.5853` edge `-0.0353` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7851` n `237` status `ready` deltaP `7.9718` edge `-0.0121` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8845` n `237` status `ready` deltaP `3.4361` edge `-0.0091` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.951` n `237` status `ready` deltaP `5.9381` edge `0.0086` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7885` n `237` status `ready` deltaP `1.4305` edge `0.0115` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-2.8506` n `237` status `ready` deltaP `-6.7337` edge `0.0439` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.4209` n `237` status `ready` deltaP `0.1756` edge `-0.0113` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.8065` n `224` status `ready` deltaP `-6.4485` edge `-0.0874` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4365` n `224` status `ready` deltaP `-7.3661` edge `-0.0159` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.4397` n `237` status `ready` deltaP `5.5354` edge `-0.069` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.0525` n `224` status `ready` deltaP `-3.7946` edge `-0.1129` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

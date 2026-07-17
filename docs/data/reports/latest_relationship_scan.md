# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T05:22:23.951460+00:00`
- Price records: `672`
- Market context records: `6996`
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
- `market_context_high->crypto_alt_1h` score `-0.3037` n `237` status `ready` deltaP `2.43` edge `0.0313` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6305` n `237` status `ready` deltaP `1.2582` edge `0.0019` maxDD `-2.2895`
- `market_context_high->unknown_24h` score `-0.6422` n `224` status `ready` deltaP `-6.4236` edge `0.4155` maxDD `-18.7342`
- `market_context_high->metal_1h` score `-0.6772` n `237` status `ready` deltaP `-1.4913` edge `-0.0001` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9155` n `237` status `ready` deltaP `12.2401` edge `0.0074` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-0.9858` n `237` status `ready` deltaP `3.6276` edge `0.0289` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2286` n `237` status `ready` deltaP `-2.2253` edge `-0.0154` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.355` n `237` status `ready` deltaP `-1.6815` edge `-0.0116` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6709` n `237` status `ready` deltaP `-4.2805` edge `-0.0367` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7569` n `237` status `ready` deltaP `8.1243` edge `-0.0095` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8058` n `237` status `ready` deltaP `4.0349` edge `-0.003` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8871` n `237` status `ready` deltaP `6.8527` edge `0.0107` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.6926` n `237` status `ready` deltaP `-6.124` edge `0.053` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.7417` n `237` status `ready` deltaP `1.4305` edge `0.0175` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.2642` n `237` status `ready` deltaP `1.0902` edge `0.0027` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.8785` n `224` status `ready` deltaP `-6.4485` edge `-0.0934` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4473` n `224` status `ready` deltaP `-7.3661` edge `-0.0168` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.307` n `237` status `ready` deltaP `5.6878` edge `-0.053` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.8124` n `224` status `ready` deltaP `-1.7113` edge `-0.096` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

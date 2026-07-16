# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T22:37:26.347010+00:00`
- Price records: `672`
- Market context records: `6965`
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

- `market_context_high->fx_1h` score `-0.2429` n `237` status `ready` deltaP `2.3339` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4105` n `237` status `ready` deltaP `1.9809` edge `0.0206` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.7107` n `237` status `ready` deltaP `-1.7907` edge `-0.0024` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7426` n `237` status `ready` deltaP `-0.5382` edge `-0.0005` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.9228` n `237` status `ready` deltaP `11.9352` edge `0.0085` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.2317` n `237` status `ready` deltaP `2.7294` edge `0.0144` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.3209` n `237` status `ready` deltaP `-3.2732` edge `-0.0161` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.6381` n `237` status `ready` deltaP `-2.2803` edge `-0.0312` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6671` n `237` status `ready` deltaP `-4.4329` edge `-0.0352` maxDD `-5.5853`
- `market_context_high->unknown_24h` score `-1.6704` n `224` status `ready` deltaP `-9.2014` edge `0.3022` maxDD `-18.7342`
- `market_context_high->index_4h` score `-1.8568` n `237` status `ready` deltaP `7.0572` edge `-0.0152` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-2.0326` n `237` status `ready` deltaP `1.9391` edge `-0.0181` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.0741` n `237` status `ready` deltaP `4.2612` edge `0.004` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-3.1951` n `237` status `ready` deltaP `-0.7036` edge `-0.0264` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-3.3681` n `237` status `ready` deltaP `-8.8679` edge `0.015` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.7681` n `224` status `ready` deltaP `-6.4485` edge `-0.0842` maxDD `-5.2791`
- `market_context_high->crypto_major_4h` score `-3.8696` n `237` status `ready` deltaP `-1.9586` edge `-0.0546` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-4.4269` n `224` status `ready` deltaP `-7.3661` edge `-0.0151` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.7369` n `237` status `ready` deltaP `3.7061` edge `-0.0949` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.2904` n `224` status `ready` deltaP `-6.2252` edge `-0.1272` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

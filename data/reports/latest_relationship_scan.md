# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T03:07:24.117311+00:00`
- Price records: `672`
- Market context records: `6986`
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

- `market_context_high->fx_1h` score `-0.2593` n `237` status `ready` deltaP `2.0345` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.2827` n `237` status `ready` deltaP `2.5797` edge `0.033` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6601` n `237` status `ready` deltaP `0.8091` edge `0.0011` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6718` n `237` status `ready` deltaP `-1.3416` edge `-0.0004` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8934` n `237` status `ready` deltaP `12.545` edge `0.0082` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.0541` n `237` status `ready` deltaP `3.0288` edge `0.0272` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2035` n `237` status `ready` deltaP `-1.9259` edge `-0.0153` maxDD `-2.4388`
- `market_context_high->unknown_24h` score `-1.2515` n `224` status `ready` deltaP `-7.9861` edge `0.3478` maxDD `-18.7342`
- `market_context_high->unknown_1h` score `-1.5553` n `237` status `ready` deltaP `-1.9809` edge `-0.0263` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6577` n `237` status `ready` deltaP `-4.2805` edge `-0.035` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.767` n `237` status `ready` deltaP `8.1243` edge `-0.0108` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8292` n `237` status `ready` deltaP `3.8852` edge `-0.005` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.91` n `237` status `ready` deltaP `6.5478` edge `0.0098` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7117` n `237` status `ready` deltaP `1.8878` edge `0.0183` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-2.7564` n `237` status `ready` deltaP `-6.2764` edge `0.0487` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.3221` n `237` status `ready` deltaP `0.7853` edge `-0.0027` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.8221` n `224` status `ready` deltaP `-6.4485` edge `-0.0887` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4401` n `224` status `ready` deltaP `-7.3661` edge `-0.0162` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.36` n `237` status `ready` deltaP `5.6878` edge `-0.0598` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.9782` n `224` status `ready` deltaP `-3.1002` edge `-0.108` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

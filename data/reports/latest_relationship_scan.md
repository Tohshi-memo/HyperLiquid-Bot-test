# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T04:37:25.992634+00:00`
- Price records: `672`
- Market context records: `6993`
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
- `market_context_high->crypto_alt_1h` score `-0.2936` n `237` status `ready` deltaP `2.5797` edge `0.0316` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6313` n `237` status `ready` deltaP `1.2582` edge `0.0018` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6796` n `237` status `ready` deltaP `-1.4913` edge `-0.0004` maxDD `-2.1427`
- `market_context_high->unknown_24h` score `-0.8432` n `224` status `ready` deltaP `-6.9444` edge `0.3932` maxDD `-18.7342`
- `market_context_high->fx_4h` score `-0.8973` n `237` status `ready` deltaP `12.545` edge `0.0077` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.0014` n `237` status `ready` deltaP `3.4779` edge `0.0286` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2023` n `237` status `ready` deltaP `-1.9259` edge `-0.0152` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.3909` n `237` status `ready` deltaP `-1.9809` edge `-0.0126` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6639` n `237` status `ready` deltaP `-4.2805` edge `-0.0358` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.76` n `237` status `ready` deltaP `8.1243` edge `-0.0099` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8206` n `237` status `ready` deltaP `3.8852` edge `-0.0039` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.891` n `237` status `ready` deltaP `6.8527` edge `0.0102` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.6912` n `237` status `ready` deltaP `-5.9715` edge `0.0521` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.759` n `237` status `ready` deltaP `1.2781` edge `0.0163` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.2978` n `237` status `ready` deltaP `0.9378` edge `-0.0006` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.8593` n `224` status `ready` deltaP `-6.4485` edge `-0.0918` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4437` n `224` status `ready` deltaP `-7.3661` edge `-0.0165` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.3257` n `237` status `ready` deltaP `5.6878` edge `-0.0554` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.864` n `224` status `ready` deltaP `-2.0585` edge `-0.1003` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

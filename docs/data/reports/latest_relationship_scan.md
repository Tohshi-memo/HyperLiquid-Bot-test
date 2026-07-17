# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T06:52:31.842431+00:00`
- Price records: `672`
- Market context records: `7002`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11539`

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

- `market_context_high->unknown_24h` score `-0.2012` n `224` status `ready` deltaP `-5.3819` edge `0.4651` maxDD `-18.7342`
- `market_context_high->fx_1h` score `-0.2639` n `237` status `ready` deltaP `2.0345` edge `0.0011` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.2889` n `237` status `ready` deltaP `2.43` edge `0.0332` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6663` n `237` status `ready` deltaP `0.6594` edge `0.0013` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6975` n `237` status `ready` deltaP `-1.7907` edge `-0.0007` maxDD `-2.1427`
- `market_context_high->crypto_major_1h` score `-0.9403` n `237` status `ready` deltaP `3.7773` edge `0.0317` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.9534` n `237` status `ready` deltaP `11.6304` edge `0.0066` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.1939` n `237` status `ready` deltaP `-1.9259` edge `-0.0145` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.301` n `237` status `ready` deltaP `-1.3821` edge `-0.0091` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.667` n `237` status `ready` deltaP `-4.2805` edge `-0.0362` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7522` n `237` status `ready` deltaP `8.1243` edge `-0.0089` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8424` n `237` status `ready` deltaP `3.5858` edge `-0.0047` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.9226` n `237` status `ready` deltaP `6.3954` edge `0.0092` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.5238` n `237` status `ready` deltaP `-5.5142` edge `0.063` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.6772` n `237` status `ready` deltaP `2.0403` edge `0.0217` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.1363` n `237` status `ready` deltaP `2.0049` edge `0.013` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.9013` n `224` status `ready` deltaP `-6.4485` edge `-0.0953` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4533` n `224` status `ready` deltaP `-7.3661` edge `-0.0173` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.2867` n `237` status `ready` deltaP `5.6878` edge `-0.0504` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.6903` n `224` status `ready` deltaP `-0.6696` edge `-0.0873` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

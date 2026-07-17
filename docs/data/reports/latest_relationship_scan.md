# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T07:22:30.220196+00:00`
- Price records: `672`
- Market context records: `7005`
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

- `market_context_high->unknown_24h` score `-0.0528` n `224` status `ready` deltaP `-5.0347` edge `0.4818` maxDD `-18.7342`
- `market_context_high->fx_1h` score `-0.2554` n `237` status `ready` deltaP `2.1842` edge `0.0012` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.2974` n `237` status `ready` deltaP `2.2803` edge `0.0331` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6663` n `237` status `ready` deltaP `0.6594` edge `0.0013` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6959` n `237` status `ready` deltaP `-1.7907` edge `-0.0005` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9368` n `237` status `ready` deltaP `11.9352` edge `0.0067` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-0.9439` n `237` status `ready` deltaP `3.7773` edge `0.0314` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2262` n `237` status `ready` deltaP `-2.2253` edge `-0.0152` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.2399` n `237` status `ready` deltaP `-1.0827` edge `-0.006` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.667` n `237` status `ready` deltaP `-4.2805` edge `-0.0362` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7317` n `237` status `ready` deltaP `8.4291` edge `-0.0083` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8533` n `237` status `ready` deltaP `3.4361` edge `-0.0051` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.9226` n `237` status `ready` deltaP `6.3954` edge `0.0092` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.4538` n `237` status `ready` deltaP `-5.2093` edge `0.0668` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.6341` n `237` status `ready` deltaP `2.3451` edge `0.0252` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.0838` n `237` status `ready` deltaP `2.3097` edge `0.0177` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.9121` n `224` status `ready` deltaP `-6.4485` edge `-0.0962` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4521` n `224` status `ready` deltaP `-7.3661` edge `-0.0172` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.2554` n `237` status `ready` deltaP `5.8403` edge `-0.0474` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.6481` n `224` status `ready` deltaP `-0.3224` edge `-0.0842` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T07:01:06.718975+00:00`
- Price records: `672`
- Market context records: `7003`
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

- `market_context_high->unknown_24h` score `-0.1274` n `224` status `ready` deltaP `-5.2083` edge `0.4734` maxDD `-18.7342`
- `market_context_high->fx_1h` score `-0.2639` n `237` status `ready` deltaP `2.0345` edge `0.0011` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3006` n `237` status `ready` deltaP `2.2803` edge `0.0327` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6671` n `237` status `ready` deltaP `0.6594` edge `0.0012` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6975` n `237` status `ready` deltaP `-1.7907` edge `-0.0007` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9534` n `237` status `ready` deltaP `11.6304` edge `0.0066` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-0.9582` n `237` status `ready` deltaP `3.6276` edge `0.0312` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2083` n `237` status `ready` deltaP `-2.0756` edge `-0.0147` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.2698` n `237` status `ready` deltaP `-1.2324` edge `-0.0075` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6662` n `237` status `ready` deltaP `-4.2805` edge `-0.0361` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7427` n `237` status `ready` deltaP `8.2767` edge `-0.0087` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8541` n `237` status `ready` deltaP `3.4361` edge `-0.0052` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.9234` n `237` status `ready` deltaP `6.3954` edge `0.0091` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.49` n `237` status `ready` deltaP `-5.3618` edge `0.0648` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.6592` n `237` status `ready` deltaP `2.1927` edge `0.023` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.1127` n `237` status `ready` deltaP `2.1573` edge `0.015` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.9049` n `224` status `ready` deltaP `-6.4485` edge `-0.0956` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4521` n `224` status `ready` deltaP `-7.3661` edge `-0.0172` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.2774` n `237` status `ready` deltaP `5.6878` edge `-0.0492` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.6696` n `224` status `ready` deltaP `-0.496` edge `-0.0858` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

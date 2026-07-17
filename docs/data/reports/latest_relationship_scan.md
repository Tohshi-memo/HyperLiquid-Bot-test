# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T15:22:38.475644+00:00`
- Price records: `672`
- Market context records: `7041`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `market_context_high->fx_4h` score `-0.0228` n `205` status `ready` deltaP `13.6281` edge `0.0102` maxDD `-0.9847`
- `market_context_high->fx_1h` score `-0.2236` n `205` status `ready` deltaP `2.2287` edge `0.0017` maxDD `-0.285`
- `market_context_high->crypto_alt_1h` score `-0.2618` n `205` status `ready` deltaP `2.3499` edge `0.0372` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7152` n `205` status `ready` deltaP `0.0788` edge `-0.0011` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7394` n `205` status `ready` deltaP `-2.626` edge `-0.0005` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.7639` n `205` status `ready` deltaP `-3.1656` edge `-0.0152` maxDD `-1.9306`
- `market_context_high->crypto_major_1h` score `-0.8397` n `205` status `ready` deltaP `4.2238` edge `0.0371` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.0373` n `205` status `ready` deltaP `-2.5771` edge `0.009` maxDD `-2.5944`
- `market_context_high->unknown_4h` score `-1.7236` n `205` status `ready` deltaP `-6.372` edge `0.0923` maxDD `-7.143`
- `market_context_high->equity_1h` score `-1.7618` n `205` status `ready` deltaP `4.5465` edge `-0.0139` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.0187` n `205` status `ready` deltaP `4.7256` edge `-0.0204` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-2.0449` n `205` status `ready` deltaP `4.2683` edge `0.0077` maxDD `-5.5324`
- `market_context_high->commodity_4h` score `-2.0643` n `205` status `ready` deltaP `-3.6281` edge `-0.0318` maxDD `-2.9494`
- `market_context_high->unknown_24h` score `-2.2441` n `200` status `ready` deltaP `-10.2292` edge `0.2741` maxDD `-21.8217`
- `market_context_high->commodity_24h` score `-2.2573` n `200` status `ready` deltaP `-0.2292` edge `-0.0557` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.5108` n `205` status `ready` deltaP `3.1707` edge `0.0355` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.7743` n `205` status `ready` deltaP `4.3902` edge `0.0435` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.686` n `200` status `ready` deltaP `-1.9583` edge `-0.0114` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.318` n `205` status `ready` deltaP `5.0` edge `-0.0845` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.5771` n `200` status `ready` deltaP `-15.1181` edge `-0.0712` maxDD `-43.0885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

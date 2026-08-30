# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T02:37:29.891526+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11504`

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

- `risk_on_high->unknown_4h` score `5.9631` n `61` status `ready` deltaP `21.7164` edge `0.395` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `5.9631` n `61` status `ready` deltaP `21.7164` edge `0.395` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6615` n `104` status `ready` deltaP `34.2414` edge `0.2621` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.5318` n `61` status `ready` deltaP `25.1824` edge `0.2457` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `4.5318` n `61` status `ready` deltaP `25.1824` edge `0.2457` maxDD `-1.208`
- `market_context_high->unknown_4h` score `4.0581` n `163` status `ready` deltaP `18.4779` edge `0.262` maxDD `-1.0945`
- `risk_on_high->crypto_alt_4h` score `3.0247` n `61` status `ready` deltaP `16.4509` edge `0.3258` maxDD `-1.4818`
- `risk_on_and_context->crypto_alt_4h` score `3.0247` n `61` status `ready` deltaP `16.4509` edge `0.3258` maxDD `-1.4818`
- `risk_on_high->equity_4h` score `2.6228` n `61` status `ready` deltaP `23.5056` edge `0.0868` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.6228` n `61` status `ready` deltaP `23.5056` edge `0.0868` maxDD `-0.3281`
- `risk_on_high->unknown_1h` score `2.0305` n `66` status `ready` deltaP `3.4568` edge `0.1901` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `2.0305` n `66` status `ready` deltaP `3.4568` edge `0.1901` maxDD `-1.5148`
- `risk_on_high->metal_4h` score `2.0096` n `61` status `ready` deltaP `25.2225` edge `0.0289` maxDD `-0.0336`
- `risk_on_and_context->metal_4h` score `2.0096` n `61` status `ready` deltaP `25.2225` edge `0.0289` maxDD `-0.0336`
- `market_context_high->unknown_1h` score `1.9426` n `168` status `ready` deltaP `9.4633` edge `0.1469` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.8529` n `61` status `ready` deltaP `26.0596` edge `0.0116` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.8529` n `61` status `ready` deltaP `26.0596` edge `0.0116` maxDD `-0.1405`
- `risk_on_high->metal_1h` score `1.1789` n `66` status `ready` deltaP `16.8527` edge `0.0073` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.1789` n `66` status `ready` deltaP `16.8527` edge `0.0073` maxDD `-0.0463`
- `news_risk_high->fx_4h` score `0.5004` n `39` status `ready` deltaP `16.4986` edge `0.0091` maxDD `-0.3953`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

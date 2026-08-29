# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T23:52:23.768994+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `risk_on_high->crypto_alt_4h` score `7.279` n `50` status `ready` deltaP `25.6951` edge `0.4663` maxDD `-0.4812`
- `risk_on_and_context->crypto_alt_4h` score `7.279` n `50` status `ready` deltaP `25.6951` edge `0.4663` maxDD `-0.4812`
- `risk_on_high->crypto_major_4h` score `6.3203` n `50` status `ready` deltaP `34.7988` edge `0.3223` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `6.3203` n `50` status `ready` deltaP `34.7988` edge `0.3223` maxDD `-1.208`
- `news_risk_high->crypto_alt_24h` score `5.0051` n `43` status `ready` deltaP `20.3933` edge `0.8433` maxDD `-22.3391`
- `news_risk_high->unknown_4h` score `4.7443` n `50` status `ready` deltaP `-2.1951` edge `0.469` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6802` n `104` status `ready` deltaP `34.415` edge `0.2625` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `3.3457` n `50` status `ready` deltaP `-6.6287` edge `0.3587` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `3.1286` n `50` status `ready` deltaP `35.311` edge `0.0339` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.1286` n `50` status `ready` deltaP `35.311` edge `0.0339` maxDD `-0.0208`
- `risk_on_high->equity_4h` score `2.4119` n `50` status `ready` deltaP `19.5793` edge `0.0954` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.4119` n `50` status `ready` deltaP `19.5793` edge `0.0954` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.8641` n `152` status `ready` deltaP `18.0681` edge `0.0819` maxDD `-1.0945`
- `risk_on_high->index_4h` score `1.4947` n `50` status `ready` deltaP `21.7317` edge `0.0106` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.4947` n `50` status `ready` deltaP `21.7317` edge `0.0106` maxDD `-0.1405`
- `market_context_high->unknown_1h` score `1.3675` n `164` status `ready` deltaP `8.2737` edge `0.1069` maxDD `-1.5148`
- `risk_on_high->metal_1h` score `1.247` n `62` status `ready` deltaP `17.6743` edge `0.0075` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.247` n `62` status `ready` deltaP `17.6743` edge `0.0075` maxDD `-0.0463`
- `news_risk_high->fx_4h` score `1.0564` n `50` status `ready` deltaP `26.6524` edge `0.0127` maxDD `-0.3953`
- `risk_on_high->unknown_1h` score `0.5829` n `62` status `ready` deltaP `0.6616` edge `0.0881` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

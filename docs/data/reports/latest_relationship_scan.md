# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T17:37:31.998209+00:00`
- Price records: `672`
- Market context records: `3914`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11409`

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

- `risk_on_high->unknown_4h` score `53.3625` n `66` status `ready` deltaP `6.0329` edge `7.0153` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `53.3625` n `66` status `ready` deltaP `6.0329` edge `7.0153` maxDD `-13.467`
- `risk_on_high->equity_24h` score `19.8743` n `40` status `ready` deltaP `42.0139` edge `1.3761` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `19.8743` n `40` status `ready` deltaP `42.0139` edge `1.3761` maxDD `0.0`
- `market_context_high->unknown_4h` score `11.579` n `202` status `ready` deltaP `-1.6029` edge `1.5165` maxDD `-35.6052`
- `risk_on_high->crypto_major_24h` score `10.4605` n `40` status `ready` deltaP `3.125` edge `1.4993` maxDD `-9.3236`
- `risk_on_and_context->crypto_major_24h` score `10.4605` n `40` status `ready` deltaP `3.125` edge `1.4993` maxDD `-9.3236`
- `risk_on_high->crypto_major_4h` score `7.9864` n `66` status `ready` deltaP `26.9678` edge `0.5523` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `7.9864` n `66` status `ready` deltaP `26.9678` edge `0.5523` maxDD `-2.6576`
- `risk_on_high->index_24h` score `7.9552` n `40` status `ready` deltaP `30.0347` edge `0.4627` maxDD `0.0`
- `risk_on_and_context->index_24h` score `7.9552` n `40` status `ready` deltaP `30.0347` edge `0.4627` maxDD `0.0`
- `market_context_high->equity_24h` score `5.7204` n `165` status `ready` deltaP `20.8018` edge `0.641` maxDD `-14.5715`
- `risk_on_high->equity_4h` score `5.0131` n `66` status `ready` deltaP `32.525` edge `0.2391` maxDD `-1.7208`
- `risk_on_and_context->equity_4h` score `5.0131` n `66` status `ready` deltaP `32.525` edge `0.2391` maxDD `-1.7208`
- `market_context_high->index_24h` score `4.416` n `165` status `ready` deltaP `25.7923` edge `0.31` maxDD `-7.1159`
- `market_context_high->crypto_major_4h` score `3.2644` n `202` status `ready` deltaP `19.002` edge `0.3218` maxDD `-9.4488`
- `market_context_high->metal_24h` score `2.6123` n `165` status `ready` deltaP `17.5947` edge `0.2519` maxDD `-9.1203`
- `risk_on_high->crypto_alt_24h` score `2.6119` n `40` status `ready` deltaP `1.0417` edge `0.6351` maxDD `-19.5749`
- `risk_on_and_context->crypto_alt_24h` score `2.6119` n `40` status `ready` deltaP `1.0417` edge `0.6351` maxDD `-19.5749`
- `risk_on_high->crypto_alt_4h` score `1.6193` n `66` status `ready` deltaP `0.887` edge `0.2143` maxDD `-4.1548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

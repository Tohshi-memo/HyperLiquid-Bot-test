# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T00:52:27.953573+00:00`
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

- `risk_on_high->crypto_alt_4h` score `6.7061` n `54` status `ready` deltaP `25.1637` edge `0.4221` maxDD `-0.4812`
- `risk_on_and_context->crypto_alt_4h` score `6.7061` n `54` status `ready` deltaP `25.1637` edge `0.4221` maxDD `-0.4812`
- `risk_on_high->crypto_major_4h` score `5.9995` n `54` status `ready` deltaP `33.6833` edge `0.303` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `5.9995` n `54` status `ready` deltaP `33.6833` edge `0.303` maxDD `-1.208`
- `market_context_high->metal_24h` score `4.6802` n `104` status `ready` deltaP `34.415` edge `0.2625` maxDD `-3.1535`
- `news_risk_high->unknown_4h` score `3.3996` n `46` status `ready` deltaP `-5.3685` edge `0.3781` maxDD `-1.7205`
- `news_risk_high->unknown_1h` score `3.2009` n `46` status `ready` deltaP `-10.6287` edge `0.3733` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `2.8718` n `54` status `ready` deltaP `32.3566` edge `0.0322` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `2.8718` n `54` status `ready` deltaP `32.3566` edge `0.0322` maxDD `-0.0208`
- `news_risk_high->crypto_alt_24h` score `2.786` n `43` status `ready` deltaP `20.3933` edge `0.5588` maxDD `-22.3391`
- `risk_on_high->equity_4h` score `2.5348` n `54` status `ready` deltaP `21.5052` edge `0.0928` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.5348` n `54` status `ready` deltaP `21.5052` edge `0.0928` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `2.2632` n `156` status `ready` deltaP `17.597` edge `0.1183` maxDD `-1.0945`
- `risk_on_high->unknown_1h` score `1.865` n `66` status `ready` deltaP `3.0077` edge `0.1793` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `1.865` n `66` status `ready` deltaP `3.0077` edge `0.1793` maxDD `-1.5148`
- `market_context_high->unknown_1h` score `1.7771` n `168` status `ready` deltaP `9.0142` edge `0.1361` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.6417` n `54` status `ready` deltaP `23.5095` edge `0.011` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.6417` n `54` status `ready` deltaP `23.5095` edge `0.011` maxDD `-0.1405`
- `risk_on_high->metal_1h` score `1.1657` n `66` status `ready` deltaP `16.703` edge `0.0072` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.1657` n `66` status `ready` deltaP `16.703` edge `0.0072` maxDD `-0.0463`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

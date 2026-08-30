# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T02:07:29.137161+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11498`

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

- `risk_on_high->unknown_4h` score `4.8063` n `59` status `ready` deltaP `21.1606` edge `0.3023` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `4.8063` n `59` status `ready` deltaP `21.1606` edge `0.3023` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `4.8042` n `59` status `ready` deltaP `26.3073` edge `0.2609` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `4.8042` n `59` status `ready` deltaP `26.3073` edge `0.2609` maxDD `-1.208`
- `market_context_high->metal_24h` score `4.679` n `104` status `ready` deltaP `34.415` edge `0.2624` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `3.6041` n `161` status `ready` deltaP `18.234` edge `0.2258` maxDD `-1.0945`
- `risk_on_high->crypto_alt_4h` score `3.365` n `59` status `ready` deltaP `18.7293` edge `0.3486` maxDD `-1.3639`
- `risk_on_and_context->crypto_alt_4h` score `3.365` n `59` status `ready` deltaP `18.7293` edge `0.3486` maxDD `-1.3639`
- `risk_on_high->equity_4h` score `2.6074` n `59` status `ready` deltaP `23.0881` edge `0.0883` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.6074` n `59` status `ready` deltaP `23.0881` edge `0.0883` maxDD `-0.3281`
- `risk_on_high->metal_4h` score `1.9979` n `59` status `ready` deltaP `24.9715` edge `0.0296` maxDD `-0.0336`
- `risk_on_and_context->metal_4h` score `1.9979` n `59` status `ready` deltaP `24.9715` edge `0.0296` maxDD `-0.0336`
- `risk_on_high->unknown_1h` score `1.8746` n `66` status `ready` deltaP `3.1574` edge `0.1791` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `1.8746` n `66` status `ready` deltaP `3.1574` edge `0.1791` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.7983` n `59` status `ready` deltaP `25.3927` edge `0.0115` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.7983` n `59` status `ready` deltaP `25.3927` edge `0.0115` maxDD `-0.1405`
- `market_context_high->unknown_1h` score `1.7867` n `168` status `ready` deltaP `9.1639` edge `0.1359` maxDD `-1.5148`
- `news_risk_high->unknown_1h` score `1.599` n `41` status `ready` deltaP `-14.1375` edge `0.2632` maxDD `-0.8558`
- `risk_on_high->metal_1h` score `1.1908` n `66` status `ready` deltaP `17.0024` edge `0.0073` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.1908` n `66` status `ready` deltaP `17.0024` edge `0.0073` maxDD `-0.0463`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T11:07:22.821441+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11456`

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

- `risk_on_high->unknown_4h` score `9.6768` n `59` status `ready` deltaP `24.6667` edge `0.6848` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.6768` n `59` status `ready` deltaP `24.6667` edge `0.6848` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `5.9217` n `152` status `ready` deltaP `20.5633` edge `0.4034` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `4.6518` n `59` status `ready` deltaP `24.5944` edge `0.252` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.6518` n `59` status `ready` deltaP `24.5944` edge `0.252` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.5522` n `101` status `ready` deltaP `33.6702` edge `0.2568` maxDD `-3.1535`
- `risk_on_high->unknown_1h` score `3.9706` n `59` status `ready` deltaP `11.1083` edge `0.2771` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.9706` n `59` status `ready` deltaP `11.1083` edge `0.2771` maxDD `-0.2885`
- `risk_on_high->equity_4h` score `3.4319` n `59` status `ready` deltaP `30.9529` edge `0.0983` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.4319` n `59` status `ready` deltaP `30.9529` edge `0.0983` maxDD `-0.1594`
- `market_context_high->unknown_1h` score `2.7947` n `152` status `ready` deltaP `12.0115` edge `0.1937` maxDD `-0.9372`
- `risk_on_high->index_4h` score `2.7774` n `59` status `ready` deltaP `33.7149` edge `0.0152` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.7774` n `59` status `ready` deltaP `33.7149` edge `0.0152` maxDD `-0.0147`
- `risk_on_high->crypto_alt_4h` score `2.2396` n `59` status `ready` deltaP `12.407` edge `0.2527` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.2396` n `59` status `ready` deltaP `12.407` edge `0.2527` maxDD `-1.5298`
- `risk_on_high->metal_4h` score `1.8112` n `59` status `ready` deltaP `22.6669` edge `0.0296` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.8112` n `59` status `ready` deltaP `22.6669` edge `0.0296` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.7131` n `59` status `ready` deltaP `22.6784` edge `0.0086` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.7131` n `59` status `ready` deltaP `22.6784` edge `0.0086` maxDD `-0.0291`
- `risk_on_high->equity_1h` score `1.3369` n `59` status `ready` deltaP `17.3425` edge `0.0192` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

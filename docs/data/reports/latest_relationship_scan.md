# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T11:37:26.877478+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11452`

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

- `risk_on_high->unknown_4h` score `9.8175` n `59` status `ready` deltaP `24.9715` edge `0.6945` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.8175` n `59` status `ready` deltaP `24.9715` edge `0.6945` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `6.0625` n `152` status `ready` deltaP `20.8681` edge `0.4131` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `4.7074` n `59` status `ready` deltaP `24.8992` edge `0.2546` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.7074` n `59` status `ready` deltaP `24.8992` edge `0.2546` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.5614` n `103` status `ready` deltaP `34.0547` edge `0.255` maxDD `-3.1535`
- `risk_on_high->unknown_1h` score `4.0029` n `59` status `ready` deltaP `11.4077` edge `0.2778` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `4.0029` n `59` status `ready` deltaP `11.4077` edge `0.2778` maxDD `-0.2885`
- `risk_on_high->equity_4h` score `3.4379` n `59` status `ready` deltaP `30.9529` edge `0.0988` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.4379` n `59` status `ready` deltaP `30.9529` edge `0.0988` maxDD `-0.1594`
- `market_context_high->unknown_1h` score `2.8271` n `152` status `ready` deltaP `12.3109` edge `0.1944` maxDD `-0.9372`
- `risk_on_high->index_4h` score `2.7774` n `59` status `ready` deltaP `33.7149` edge `0.0152` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.7774` n `59` status `ready` deltaP `33.7149` edge `0.0152` maxDD `-0.0147`
- `risk_on_high->crypto_alt_4h` score `2.2762` n `59` status `ready` deltaP `12.407` edge `0.2574` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.2762` n `59` status `ready` deltaP `12.407` edge `0.2574` maxDD `-1.5298`
- `risk_on_high->metal_4h` score `1.8246` n `59` status `ready` deltaP `22.8193` edge `0.0297` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.8246` n `59` status `ready` deltaP `22.8193` edge `0.0297` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.7143` n `59` status `ready` deltaP `22.6784` edge `0.0087` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.7143` n `59` status `ready` deltaP `22.6784` edge `0.0087` maxDD `-0.0291`
- `risk_on_high->equity_1h` score `1.3393` n `59` status `ready` deltaP `17.3425` edge `0.0194` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

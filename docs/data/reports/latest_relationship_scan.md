# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T13:07:26.765646+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11462`

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

- `risk_on_high->unknown_4h` score `10.0745` n `59` status `ready` deltaP `25.124` edge `0.7149` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.0745` n `59` status `ready` deltaP `25.124` edge `0.7149` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `6.3195` n `152` status `ready` deltaP `21.0206` edge `0.4335` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `4.7158` n `59` status `ready` deltaP `24.8992` edge `0.2553` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.7158` n `59` status `ready` deltaP `24.8992` edge `0.2553` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.5785` n `109` status `ready` deltaP `35.1236` edge `0.2493` maxDD `-3.1535`
- `risk_on_high->unknown_1h` score `4.0545` n `59` status `ready` deltaP `11.5574` edge `0.2811` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `4.0545` n `59` status `ready` deltaP `11.5574` edge `0.2811` maxDD `-0.2885`
- `risk_on_high->equity_4h` score `3.4803` n `59` status `ready` deltaP `31.2578` edge `0.1003` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.4803` n `59` status `ready` deltaP `31.2578` edge `0.1003` maxDD `-0.1594`
- `market_context_high->unknown_1h` score `2.8701` n `153` status `ready` deltaP `12.6541` edge `0.1957` maxDD `-0.9372`
- `risk_on_high->index_4h` score `2.7786` n `59` status `ready` deltaP `33.7149` edge `0.0153` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.7786` n `59` status `ready` deltaP `33.7149` edge `0.0153` maxDD `-0.0147`
- `risk_on_high->crypto_alt_4h` score `2.3488` n `59` status `ready` deltaP `12.407` edge `0.2667` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.3488` n `59` status `ready` deltaP `12.407` edge `0.2667` maxDD `-1.5298`
- `risk_on_high->metal_4h` score `1.8782` n `59` status `ready` deltaP `23.4291` edge `0.0301` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.8782` n `59` status `ready` deltaP `23.4291` edge `0.0301` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.7646` n `59` status `ready` deltaP `23.2772` edge `0.0089` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.7646` n `59` status `ready` deltaP `23.2772` edge `0.0089` maxDD `-0.0291`
- `risk_on_high->equity_1h` score `1.3944` n `59` status `ready` deltaP `17.9413` edge `0.02` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

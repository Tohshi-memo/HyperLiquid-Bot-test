# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T14:22:23.286533+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11546`

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

- `risk_on_high->unknown_4h` score `10.1987` n `59` status `ready` deltaP `25.5813` edge `0.7222` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.1987` n `59` status `ready` deltaP `25.5813` edge `0.7222` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `6.4437` n `152` status `ready` deltaP `21.4779` edge `0.4408` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `4.6618` n `59` status `ready` deltaP `24.8992` edge `0.2508` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.6618` n `59` status `ready` deltaP `24.8992` edge `0.2508` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.6116` n `114` status `ready` deltaP `35.9283` edge `0.2467` maxDD `-3.1535`
- `risk_on_high->equity_4h` score `3.5045` n `59` status `ready` deltaP `31.4102` edge `0.1013` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.5045` n `59` status `ready` deltaP `31.4102` edge `0.1013` maxDD `-0.1594`
- `risk_on_high->unknown_1h` score `3.3167` n `64` status `ready` deltaP `8.2897` edge `0.2414` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.3167` n `64` status `ready` deltaP `8.2897` edge `0.2414` maxDD `-0.2885`
- `risk_on_high->index_4h` score `2.7798` n `59` status `ready` deltaP `33.7149` edge `0.0154` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.7798` n `59` status `ready` deltaP `33.7149` edge `0.0154` maxDD `-0.0147`
- `market_context_high->unknown_1h` score `2.6616` n `158` status `ready` deltaP `11.652` edge `0.185` maxDD `-0.9372`
- `risk_on_high->crypto_alt_4h` score `2.3839` n `59` status `ready` deltaP `12.407` edge `0.2712` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.3839` n `59` status `ready` deltaP `12.407` edge `0.2712` maxDD `-1.5298`
- `risk_on_high->metal_1h` score `1.913` n `64` status `ready` deltaP `24.8316` edge `0.0109` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.913` n `64` status `ready` deltaP `24.8316` edge `0.0109` maxDD `-0.0291`
- `risk_on_high->metal_4h` score `1.877` n `59` status `ready` deltaP `23.4291` edge `0.03` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.877` n `59` status `ready` deltaP `23.4291` edge `0.03` maxDD `-0.0488`
- `risk_on_high->crypto_alt_1h` score `1.4754` n `64` status `ready` deltaP `15.3911` edge `0.0701` maxDD `-1.3137`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

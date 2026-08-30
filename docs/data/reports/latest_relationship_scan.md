# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T12:52:28.577987+00:00`
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

- `risk_on_high->unknown_4h` score `10.0469` n `59` status `ready` deltaP `25.124` edge `0.7126` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.0469` n `59` status `ready` deltaP `25.124` edge `0.7126` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `6.2919` n `152` status `ready` deltaP `21.0206` edge `0.4312` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `4.7182` n `59` status `ready` deltaP `24.8992` edge `0.2555` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.7182` n `59` status `ready` deltaP `24.8992` edge `0.2555` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.5745` n `108` status `ready` deltaP `34.9537` edge `0.2501` maxDD `-3.1535`
- `risk_on_high->unknown_1h` score `4.0401` n `59` status `ready` deltaP `11.5574` edge `0.2799` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `4.0401` n `59` status `ready` deltaP `11.5574` edge `0.2799` maxDD `-0.2885`
- `risk_on_high->equity_4h` score `3.4657` n `59` status `ready` deltaP `31.1053` edge `0.1001` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.4657` n `59` status `ready` deltaP `31.1053` edge `0.1001` maxDD `-0.1594`
- `market_context_high->unknown_1h` score `2.8643` n `152` status `ready` deltaP `12.4606` edge `0.1965` maxDD `-0.9372`
- `risk_on_high->index_4h` score `2.7786` n `59` status `ready` deltaP `33.7149` edge `0.0153` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.7786` n `59` status `ready` deltaP `33.7149` edge `0.0153` maxDD `-0.0147`
- `risk_on_high->crypto_alt_4h` score `2.3417` n `59` status `ready` deltaP `12.407` edge `0.2658` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.3417` n `59` status `ready` deltaP `12.407` edge `0.2658` maxDD `-1.5298`
- `risk_on_high->metal_4h` score `1.877` n `59` status `ready` deltaP `23.4291` edge `0.03` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.877` n `59` status `ready` deltaP `23.4291` edge `0.03` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.7646` n `59` status `ready` deltaP `23.2772` edge `0.0089` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.7646` n `59` status `ready` deltaP `23.2772` edge `0.0089` maxDD `-0.0291`
- `risk_on_high->equity_1h` score `1.3812` n `59` status `ready` deltaP `17.7916` edge `0.0199` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

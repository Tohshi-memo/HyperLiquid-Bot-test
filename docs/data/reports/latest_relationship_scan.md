# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T01:22:22.638269+00:00`
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

- `risk_on_high->crypto_major_4h` score `5.5768` n `56` status `ready` deltaP `30.5749` edge `0.2885` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `5.5768` n `56` status `ready` deltaP `30.5749` edge `0.2885` maxDD `-1.208`
- `market_context_high->metal_24h` score `4.6826` n `104` status `ready` deltaP `34.415` edge `0.2627` maxDD `-3.1535`
- `risk_on_high->crypto_alt_4h` score `3.9948` n `56` status `ready` deltaP `22.4521` edge `0.3955` maxDD `-0.6423`
- `risk_on_and_context->crypto_alt_4h` score `3.9948` n `56` status `ready` deltaP `22.4521` edge `0.3955` maxDD `-0.6423`
- `news_risk_high->unknown_1h` score `3.0455` n `44` status `ready` deltaP `-12.9014` edge `0.3755` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.7664` n `158` status `ready` deltaP `17.8566` edge `0.1585` maxDD `-1.0945`
- `risk_on_high->equity_4h` score `2.5844` n `56` status `ready` deltaP `22.365` edge `0.0912` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.5844` n `56` status `ready` deltaP `22.365` edge `0.0912` maxDD `-0.3281`
- `risk_on_high->unknown_4h` score `2.54` n `56` status `ready` deltaP `20.2527` edge `0.1195` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `2.54` n `56` status `ready` deltaP `20.2527` edge `0.1195` maxDD `-1.0945`
- `risk_on_high->metal_4h` score `2.5237` n `56` status `ready` deltaP `29.4207` edge `0.0311` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `2.5237` n `56` status `ready` deltaP `29.4207` edge `0.0311` maxDD `-0.0208`
- `news_risk_high->unknown_4h` score `2.4951` n `44` status `ready` deltaP `-7.3447` edge `0.3159` maxDD `-1.7205`
- `news_risk_high->crypto_alt_24h` score `1.9149` n `41` status `ready` deltaP `18.8051` edge `0.4577` maxDD `-22.3391`
- `risk_on_high->unknown_1h` score `1.7318` n `66` status `ready` deltaP `3.0077` edge `0.1682` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `1.7318` n `66` status `ready` deltaP `3.0077` edge `0.1682` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.7052` n `56` status `ready` deltaP `24.3031` edge `0.011` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.7052` n `56` status `ready` deltaP `24.3031` edge `0.011` maxDD `-0.1405`
- `market_context_high->unknown_1h` score `1.6439` n `168` status `ready` deltaP `9.0142` edge `0.125` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

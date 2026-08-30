# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T01:38:05.522206+00:00`
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

- `risk_on_high->crypto_major_4h` score `5.351` n `57` status `ready` deltaP `29.1024` edge `0.2795` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `5.351` n `57` status `ready` deltaP `29.1024` edge `0.2795` maxDD `-1.208`
- `market_context_high->metal_24h` score `4.6802` n `104` status `ready` deltaP `34.415` edge `0.2625` maxDD `-3.1535`
- `risk_on_high->crypto_alt_4h` score `3.7955` n `57` status `ready` deltaP `21.1676` edge `0.3808` maxDD `-0.8254`
- `risk_on_and_context->crypto_alt_4h` score `3.7955` n `57` status `ready` deltaP `21.1676` edge `0.3808` maxDD `-0.8254`
- `risk_on_high->unknown_4h` score `3.3343` n `57` status `ready` deltaP `20.5659` edge `0.1836` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `3.3343` n `57` status `ready` deltaP `20.5659` edge `0.1836` maxDD `-1.0945`
- `news_risk_high->unknown_1h` score `3.3131` n `43` status `ready` deltaP `-11.9412` edge `0.3914` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `3.0285` n `159` status `ready` deltaP `17.984` edge `0.1795` maxDD `-1.0945`
- `risk_on_high->equity_4h` score `2.594` n `57` status `ready` deltaP `22.6198` edge `0.0903` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.594` n `57` status `ready` deltaP `22.6198` edge `0.0903` maxDD `-0.3281`
- `risk_on_high->metal_4h` score `2.3458` n `57` status `ready` deltaP `27.8856` edge `0.0307` maxDD `-0.023`
- `risk_on_and_context->metal_4h` score `2.3458` n `57` status `ready` deltaP `27.8856` edge `0.0307` maxDD `-0.023`
- `news_risk_high->unknown_4h` score `1.873` n `43` status `ready` deltaP `-8.4018` edge `0.2711` maxDD `-1.7205`
- `risk_on_high->index_4h` score `1.7401` n `57` status `ready` deltaP `24.6791` edge `0.0114` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.7401` n `57` status `ready` deltaP `24.6791` edge `0.0114` maxDD `-0.1405`
- `risk_on_high->unknown_1h` score `1.7186` n `66` status `ready` deltaP `2.858` edge `0.1681` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `1.7186` n `66` status `ready` deltaP `2.858` edge `0.1681` maxDD `-1.5148`
- `market_context_high->unknown_1h` score `1.6307` n `168` status `ready` deltaP `8.8645` edge `0.1249` maxDD `-1.5148`
- `news_risk_high->crypto_alt_24h` score `1.5476` n `40` status `ready` deltaP `17.9514` edge `0.4163` maxDD `-22.3391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

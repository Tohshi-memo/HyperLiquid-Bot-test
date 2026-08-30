# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T00:22:25.056778+00:00`
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

- `risk_on_high->crypto_alt_4h` score `6.9096` n `52` status `ready` deltaP `24.5427` edge `0.4432` maxDD `-0.4812`
- `risk_on_and_context->crypto_alt_4h` score `6.9096` n `52` status `ready` deltaP `24.5427` edge `0.4432` maxDD `-0.4812`
- `risk_on_high->crypto_major_4h` score `6.0776` n `52` status `ready` deltaP `33.4897` edge `0.3108` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `6.0776` n `52` status `ready` deltaP `33.4897` edge `0.3108` maxDD `-1.208`
- `market_context_high->metal_24h` score `4.679` n `104` status `ready` deltaP `34.415` edge `0.2624` maxDD `-3.1535`
- `news_risk_high->unknown_4h` score `4.0978` n `48` status `ready` deltaP `-3.5569` edge `0.4242` maxDD `-1.7205`
- `news_risk_high->crypto_alt_24h` score `3.9123` n `43` status `ready` deltaP `20.3933` edge `0.7032` maxDD `-22.3391`
- `news_risk_high->unknown_1h` score `3.4144` n `48` status `ready` deltaP `-8.5454` edge `0.3772` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `3.141` n `52` status `ready` deltaP `35.5418` edge `0.0334` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.141` n `52` status `ready` deltaP `35.5418` edge `0.0334` maxDD `-0.0208`
- `risk_on_high->equity_4h` score `2.4823` n `52` status `ready` deltaP `20.5793` edge `0.0946` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.4823` n `52` status `ready` deltaP `20.5793` edge `0.0946` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.8015` n `154` status `ready` deltaP `17.3306` edge `0.0816` maxDD `-1.0945`
- `risk_on_high->index_4h` score `1.5697` n `52` status `ready` deltaP `22.6548` edge `0.0107` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.5697` n `52` status `ready` deltaP `22.6548` edge `0.0107` maxDD `-0.1405`
- `market_context_high->unknown_1h` score `1.3531` n `166` status `ready` deltaP `8.6484` edge `0.1032` maxDD `-1.5148`
- `risk_on_high->metal_1h` score `1.3184` n `64` status `ready` deltaP `18.5816` edge `0.0074` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.3184` n `64` status `ready` deltaP `18.5816` edge `0.0074` maxDD `-0.0463`
- `news_risk_high->fx_4h` score `0.9706` n `48` status `ready` deltaP `25.1524` edge `0.0117` maxDD `-0.3953`
- `risk_on_high->unknown_1h` score `0.5645` n `64` status `ready` deltaP `1.8713` edge `0.0785` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

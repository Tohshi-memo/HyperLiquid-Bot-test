# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T05:37:26.525413+00:00`
- Price records: `672`
- Market context records: `4387`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11239`

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

- `risk_on_high->unknown_4h` score `132.7671` n `44` status `ready` deltaP `-0.6791` edge `11.2503` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `132.7671` n `44` status `ready` deltaP `-0.6791` edge `11.2503` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `34.5457` n `218` status `ready` deltaP `2.4035` edge `3.0124` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.3642` n `213` status `ready` deltaP `4.1545` edge `1.4623` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.3392` n `44` status `ready` deltaP `35.5322` edge `0.0461` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.3392` n `44` status `ready` deltaP `35.5322` edge `0.0461` maxDD `-0.044`
- `risk_on_high->metal_24h` score `3.0238` n `44` status `ready` deltaP `-15.183` edge `0.5503` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.0238` n `44` status `ready` deltaP `-15.183` edge `0.5503` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `1.8655` n `44` status `ready` deltaP `18.0017` edge `0.102` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.8655` n `44` status `ready` deltaP `18.0017` edge `0.102` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.7973` n `44` status `ready` deltaP `20.4861` edge `0.0132` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7973` n `44` status `ready` deltaP `20.4861` edge `0.0132` maxDD `0.0`
- `risk_on_high->index_24h` score `1.2398` n `44` status `ready` deltaP `22.7431` edge `-0.0483` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.2398` n `44` status `ready` deltaP `22.7431` edge `-0.0483` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.5433` n `46` status `ready` deltaP `10.6548` edge `0.0132` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.5433` n `46` status `ready` deltaP `10.6548` edge `0.0132` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.4766` n `46` status `ready` deltaP `10.2773` edge `0.0468` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.4766` n `46` status `ready` deltaP `10.2773` edge `0.0468` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.4369` n `44` status `ready` deltaP `6.7904` edge `0.0443` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4369` n `44` status `ready` deltaP `6.7904` edge `0.0443` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

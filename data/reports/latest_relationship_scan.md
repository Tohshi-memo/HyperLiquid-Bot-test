# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T19:37:27.076488+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11372`

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

- `news_risk_high->unknown_24h` score `29.6938` n `58` status `ready` deltaP `2.7837` edge `2.5533` maxDD `-4.1232`
- `risk_on_high->crypto_alt_4h` score `11.9831` n `35` status `ready` deltaP `46.9905` edge `0.6912` maxDD `-0.1367`
- `risk_on_and_context->crypto_alt_4h` score `11.9831` n `35` status `ready` deltaP `46.9905` edge `0.6912` maxDD `-0.1367`
- `market_context_high->unknown_24h` score `11.4823` n `104` status `ready` deltaP `20.9535` edge `0.8904` maxDD `-3.1917`
- `news_risk_high->crypto_alt_24h` score `10.6128` n `58` status `ready` deltaP `28.8135` edge `1.5061` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `8.025` n `35` status `ready` deltaP `39.142` edge `0.4354` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `8.025` n `35` status `ready` deltaP `39.142` edge `0.4354` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `5.9791` n `67` status `ready` deltaP `7.3444` edge `0.5083` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6946` n `104` status `ready` deltaP `34.415` edge `0.2637` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `3.0254` n `35` status `ready` deltaP `33.1969` edge `0.0394` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0254` n `35` status `ready` deltaP `33.1969` edge `0.0394` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.6073` n `67` status `ready` deltaP `0.2659` edge `0.2512` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.2935` n `67` status `ready` deltaP `33.805` edge `0.0207` maxDD `-0.3953`
- `market_context_high->unknown_4h` score `2.1538` n `135` status `ready` deltaP `17.9358` edge `0.1031` maxDD `-0.7887`
- `risk_on_high->metal_1h` score `1.4938` n `45` status `ready` deltaP `20.489` edge `0.0093` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.4938` n `45` status `ready` deltaP `20.489` edge `0.0093` maxDD `-0.0463`
- `risk_on_high->equity_4h` score `1.0717` n `35` status `ready` deltaP `8.4364` edge `0.058` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `1.0717` n `35` status `ready` deltaP `8.4364` edge `0.058` maxDD `-0.3281`
- `market_context_high->crypto_major_4h` score `0.8397` n `135` status `ready` deltaP `21.7875` edge `0.2698` maxDD `-20.9394`
- `risk_on_high->unknown_4h` score `0.7949` n `35` status `ready` deltaP `25.7665` edge `-0.081` maxDD `-0.6293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

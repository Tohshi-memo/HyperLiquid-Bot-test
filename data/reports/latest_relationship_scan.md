# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T20:52:29.362539+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11432`

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

- `news_risk_high->unknown_24h` score `27.9494` n `53` status `ready` deltaP `0.3439` edge `2.4242` maxDD `-4.1232`
- `market_context_high->unknown_24h` score `12.0343` n `104` status `ready` deltaP `20.9535` edge `0.9364` maxDD `-3.1917`
- `risk_on_high->crypto_alt_4h` score `9.8932` n `40` status `ready` deltaP `37.1951` edge `0.5895` maxDD `-0.376`
- `risk_on_and_context->crypto_alt_4h` score `9.8932` n `40` status `ready` deltaP `37.1951` edge `0.5895` maxDD `-0.376`
- `news_risk_high->crypto_alt_24h` score `9.8657` n `53` status `ready` deltaP `26.5363` edge `1.4255` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `7.2919` n `40` status `ready` deltaP `37.1037` edge `0.3879` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `7.2919` n `40` status `ready` deltaP `37.1037` edge `0.3879` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.5179` n `62` status `ready` deltaP `5.3943` edge `0.5662` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6874` n `104` status `ready` deltaP `34.415` edge `0.2631` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `3.0712` n `40` status `ready` deltaP `33.9634` edge `0.0381` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0712` n `40` status `ready` deltaP `33.9634` edge `0.0381` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.7205` n `62` status `ready` deltaP `-2.7139` edge `0.2805` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `1.8049` n `140` status `ready` deltaP `16.9381` edge `0.0845` maxDD `-1.0945`
- `risk_on_high->equity_4h` score `1.6387` n `40` status `ready` deltaP `13.0793` edge `0.0743` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `1.6387` n `40` status `ready` deltaP `13.0793` edge `0.0743` maxDD `-0.3281`
- `news_risk_high->fx_4h` score `1.4037` n `62` status `ready` deltaP `32.4006` edge `0.0189` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.3799` n `50` status `ready` deltaP `19.1557` edge `0.0087` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.3799` n `50` status `ready` deltaP `19.1557` edge `0.0087` maxDD `-0.0463`
- `risk_on_high->index_4h` score `0.9571` n `40` status `ready` deltaP `15.7317` edge `0.0058` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `0.9571` n `40` status `ready` deltaP `15.7317` edge `0.0058` maxDD `-0.1405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

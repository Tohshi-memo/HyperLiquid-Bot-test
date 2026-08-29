# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T21:21:03.459532+00:00`
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

- `news_risk_high->unknown_24h` score `27.0926` n `51` status `ready` deltaP `-0.766` edge `2.3602` maxDD `-4.1232`
- `market_context_high->unknown_24h` score `12.2599` n `104` status `ready` deltaP `20.9535` edge `0.9552` maxDD `-3.1917`
- `news_risk_high->crypto_alt_24h` score `9.5935` n `51` status `ready` deltaP `25.5004` edge `1.3975` maxDD `-22.3391`
- `risk_on_high->crypto_alt_4h` score `9.319` n `42` status `ready` deltaP `35.257` edge `0.5597` maxDD `-0.4529`
- `risk_on_and_context->crypto_alt_4h` score `9.319` n `42` status `ready` deltaP `35.257` edge `0.5597` maxDD `-0.4529`
- `risk_on_high->crypto_major_4h` score `7.1088` n `42` status `ready` deltaP `37.275` edge `0.3715` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `7.1088` n `42` status `ready` deltaP `37.275` edge `0.3715` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.7019` n `60` status `ready` deltaP `4.3191` edge `0.5887` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.685` n `104` status `ready` deltaP `34.415` edge `0.2629` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `3.0827` n `42` status `ready` deltaP `34.1681` edge `0.0377` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0827` n `42` status `ready` deltaP `34.1681` edge `0.0377` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.7` n `60` status `ready` deltaP `-2.5948` edge `0.278` maxDD `-0.8558`
- `risk_on_high->equity_4h` score `1.8297` n `42` status `ready` deltaP `14.6269` edge `0.0799` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `1.8297` n `42` status `ready` deltaP `14.6269` edge `0.0799` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.773` n `142` status `ready` deltaP `17.2299` edge `0.0799` maxDD `-1.0945`
- `risk_on_high->metal_1h` score `1.4541` n `52` status `ready` deltaP `20.0829` edge `0.0087` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.4541` n `52` status `ready` deltaP `20.0829` edge `0.0087` maxDD `-0.0463`
- `market_context_high->unknown_1h` score `1.3934` n `154` status `ready` deltaP `8.5524` edge `0.1072` maxDD `-1.5148`
- `news_risk_high->fx_4h` score `1.3599` n `60` status `ready` deltaP `31.7378` edge `0.0177` maxDD `-0.3953`
- `risk_on_high->index_4h` score `1.0857` n `42` status `ready` deltaP `17.1603` edge `0.007` maxDD `-0.1405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T18:22:23.914890+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11330`

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

- `news_risk_high->unknown_24h` score `31.1593` n `62` status `ready` deltaP `4.4523` edge `2.6643` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `16.8384` n `62` status `ready` deltaP `30.3708` edge `1.5383` maxDD `-22.3391`
- `risk_on_high->crypto_alt_4h` score `13.7566` n `30` status `ready` deltaP `50.4573` edge `0.81` maxDD `0.0`
- `risk_on_and_context->crypto_alt_4h` score `13.7566` n `30` status `ready` deltaP `50.4573` edge `0.81` maxDD `0.0`
- `market_context_high->unknown_24h` score `10.8703` n `104` status `ready` deltaP `20.9535` edge `0.8394` maxDD `-3.1917`
- `risk_on_high->crypto_major_4h` score `8.364` n `30` status `ready` deltaP `38.4756` edge `0.4681` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `8.364` n `30` status `ready` deltaP `38.4756` edge `0.4681` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `5.7492` n `71` status `ready` deltaP `8.4164` edge `0.482` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.7018` n `104` status `ready` deltaP `34.415` edge `0.2643` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `2.9077` n `30` status `ready` deltaP `31.9207` edge `0.0381` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `2.9077` n `30` status `ready` deltaP `31.9207` edge `0.0381` maxDD `-0.0208`
- `risk_on_high->unknown_4h` score `2.832` n `30` status `ready` deltaP `36.5854` edge `-0.0079` maxDD `0.0`
- `risk_on_and_context->unknown_4h` score `2.832` n `30` status `ready` deltaP `36.5854` edge `-0.0079` maxDD `0.0`
- `news_risk_high->unknown_1h` score `2.6923` n `71` status `ready` deltaP `2.1528` edge `0.2457` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5343` n `130` status `ready` deltaP `19.6623` edge `0.1233` maxDD `-0.7887`
- `news_risk_high->fx_4h` score `2.3632` n `71` status `ready` deltaP `34.5564` edge `0.0215` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.3905` n `42` status `ready` deltaP `19.1831` edge `0.0094` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.3905` n `42` status `ready` deltaP `19.1831` edge `0.0094` maxDD `-0.0463`
- `market_context_high->crypto_major_4h` score `0.9013` n `130` status `ready` deltaP `21.5525` edge `0.2765` maxDD `-20.9394`
- `market_context_high->unknown_1h` score `0.6469` n `142` status `ready` deltaP `7.7866` edge `0.0501` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

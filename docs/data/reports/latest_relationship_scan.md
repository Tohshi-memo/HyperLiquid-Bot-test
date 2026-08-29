# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T16:22:31.630112+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11276`

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

- `news_risk_high->unknown_24h` score `41.8013` n `63` status `ready` deltaP `9.0774` edge `3.5203` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `19.1519` n `63` status `ready` deltaP `30.7292` edge `1.7287` maxDD `-22.3391`
- `market_context_high->unknown_24h` score `9.4799` n `104` status `ready` deltaP `20.4327` edge `0.727` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3578` n `79` status `ready` deltaP `11.2689` edge `0.5137` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6028` n `104` status `ready` deltaP `33.3734` edge `0.263` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.6614` n `79` status `ready` deltaP `5.1126` edge `0.2234` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5583` n `122` status `ready` deltaP `18.5526` edge `0.1327` maxDD `-0.7887`
- `news_risk_high->fx_4h` score `2.5318` n `79` status `ready` deltaP `36.514` edge `0.0225` maxDD `-0.3953`
- `market_context_high->unknown_1h` score `0.9091` n `134` status `ready` deltaP `8.9195` edge `0.0644` maxDD `-1.5148`
- `news_risk_high->equity_24h` score `0.9021` n `63` status `ready` deltaP `18.2292` edge `0.285` maxDD `-18.9364`
- `risk_on_high->metal_1h` score `0.8754` n `34` status `ready` deltaP `12.7598` edge `0.0093` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `0.8754` n `34` status `ready` deltaP `12.7598` edge `0.0093` maxDD `-0.0463`
- `risk_on_high->crypto_alt_1h` score `0.8114` n `34` status `ready` deltaP `15.2519` edge `0.0499` maxDD `-2.1381`
- `risk_on_and_context->crypto_alt_1h` score `0.8114` n `34` status `ready` deltaP `15.2519` edge `0.0499` maxDD `-2.1381`
- `news_risk_high->fx_1h` score `0.7425` n `79` status `ready` deltaP `14.2841` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.3966` n `79` status `ready` deltaP `11.7259` edge `0.0047` maxDD `-0.5618`
- `market_context_high->crypto_major_4h` score `0.3821` n `122` status `ready` deltaP `19.7871` edge `0.245` maxDD `-20.9394`
- `news_risk_high->metal_24h` score `0.2756` n `63` status `ready` deltaP `28.7947` edge `-0.0004` maxDD `-7.8323`
- `news_risk_high->index_24h` score `0.1236` n `63` status `ready` deltaP `14.1121` edge `0.008` maxDD `-2.2325`
- `market_context_high->crypto_alt_4h` score `0.0233` n `122` status `ready` deltaP `22.0737` edge `0.3394` maxDD `-31.4361`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

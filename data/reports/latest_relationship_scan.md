# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T22:22:28.926101+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11444`

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

- `risk_on_high->crypto_alt_4h` score `8.9034` n `44` status `ready` deltaP `33.4811` edge `0.5369` maxDD `-0.4529`
- `risk_on_and_context->crypto_alt_4h` score `8.9034` n `44` status `ready` deltaP `33.4811` edge `0.5369` maxDD `-0.4529`
- `news_risk_high->crypto_alt_24h` score `8.4439` n `47` status `ready` deltaP `23.1642` edge `1.2657` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `6.9908` n `44` status `ready` deltaP `37.5554` edge `0.3598` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `6.9908` n `44` status `ready` deltaP `37.5554` edge `0.3598` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.9098` n `56` status `ready` deltaP `1.9381` edge `0.6219` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6838` n `104` status `ready` deltaP `34.415` edge `0.2628` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `3.1845` n `56` status `ready` deltaP `-1.9995` edge `0.3144` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `3.0967` n `44` status `ready` deltaP `34.4928` edge `0.0367` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0967` n `44` status `ready` deltaP `34.4928` edge `0.0367` maxDD `-0.0208`
- `risk_on_high->equity_4h` score `2.0131` n `44` status `ready` deltaP `16.0338` edge `0.0858` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.0131` n `44` status `ready` deltaP `16.0338` edge `0.0858` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.7482` n `146` status `ready` deltaP `17.7894` edge `0.0741` maxDD `-1.0945`
- `risk_on_high->metal_1h` score `1.4603` n `56` status `ready` deltaP `20.2203` edge `0.0083` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.4603` n `56` status `ready` deltaP `20.2203` edge `0.0083` maxDD `-0.0463`
- `market_context_high->unknown_1h` score `1.4559` n `158` status `ready` deltaP `8.0592` edge `0.1157` maxDD `-1.5148`
- `news_risk_high->fx_4h` score `1.2677` n `56` status `ready` deltaP `30.2047` edge `0.0161` maxDD `-0.3953`
- `risk_on_high->index_4h` score `1.2016` n `44` status `ready` deltaP `18.459` edge `0.008` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.2016` n `44` status `ready` deltaP `18.459` edge `0.008` maxDD `-0.1405`
- `risk_on_high->unknown_1h` score `0.8069` n `56` status `ready` deltaP `-0.2138` edge `0.1126` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

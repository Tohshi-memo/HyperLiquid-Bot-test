# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T17:07:28.140150+00:00`
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

- `news_risk_high->unknown_24h` score `37.5305` n `63` status `ready` deltaP `9.0774` edge `3.1644` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `18.0467` n `63` status `ready` deltaP `30.7292` edge `1.6366` maxDD `-22.3391`
- `market_context_high->unknown_24h` score `10.0043` n `104` status `ready` deltaP `20.4327` edge `0.7707` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.1255` n `76` status `ready` deltaP `10.2696` edge `0.501` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6529` n `104` status `ready` deltaP `33.8942` edge `0.2637` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.7303` n `76` status `ready` deltaP `4.1129` edge `0.2358` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5761` n `125` status `ready` deltaP `18.9854` edge `0.1313` maxDD `-0.7887`
- `news_risk_high->fx_4h` score `2.4929` n `76` status `ready` deltaP `36.0719` edge `0.0222` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.09` n `37` status `ready` deltaP `15.4718` edge `0.0091` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.09` n `37` status `ready` deltaP `15.4718` edge `0.0091` maxDD `-0.0463`
- `risk_on_high->crypto_alt_1h` score `0.8407` n `37` status `ready` deltaP `15.3221` edge `0.0532` maxDD `-2.1381`
- `risk_on_and_context->crypto_alt_1h` score `0.8407` n `37` status `ready` deltaP `15.3221` edge `0.0532` maxDD `-2.1381`
- `market_context_high->unknown_1h` score `0.7893` n `137` status `ready` deltaP `8.3964` edge `0.0579` maxDD `-1.5148`
- `market_context_high->crypto_major_4h` score `0.6723` n `125` status `ready` deltaP `20.4756` edge `0.2646` maxDD `-20.9394`
- `news_risk_high->equity_24h` score `0.6492` n `63` status `ready` deltaP `16.8155` edge `0.262` maxDD `-18.9364`
- `news_risk_high->fx_1h` score `0.4213` n `76` status `ready` deltaP `13.1342` edge `0.0053` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.321` n `76` status `ready` deltaP `10.3766` edge `0.004` maxDD `-0.5618`
- `market_context_high->crypto_alt_4h` score `0.25` n `125` status `ready` deltaP `22.7622` edge `0.3537` maxDD `-31.4361`
- `news_risk_high->index_24h` score `-0.0422` n `63` status `ready` deltaP `11.2848` edge `0.0056` maxDD `-2.2325`
- `news_risk_high->metal_24h` score `-0.1006` n `63` status `ready` deltaP `24.5536` edge `-0.0058` maxDD `-7.996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

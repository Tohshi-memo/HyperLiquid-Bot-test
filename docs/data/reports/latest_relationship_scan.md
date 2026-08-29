# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T22:07:25.954449+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11558`

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

- `risk_on_high->crypto_alt_4h` score `9.212` n `43` status `ready` deltaP `35.2843` edge `0.5506` maxDD `-0.4529`
- `risk_on_and_context->crypto_alt_4h` score `9.212` n `43` status `ready` deltaP `35.2843` edge `0.5506` maxDD `-0.4529`
- `news_risk_high->crypto_alt_24h` score `8.8982` n `48` status `ready` deltaP `23.7847` edge `1.3198` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `7.0531` n `43` status `ready` deltaP `37.344` edge `0.3664` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `7.0531` n `43` status `ready` deltaP `37.344` edge `0.3664` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.8531` n `57` status `ready` deltaP `2.5647` edge `0.613` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6838` n `104` status `ready` deltaP `34.415` edge `0.2628` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `3.1281` n `57` status `ready` deltaP `-1.279` edge `0.3049` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `3.0924` n `43` status `ready` deltaP `34.3343` edge `0.0374` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0924` n `43` status `ready` deltaP `34.3343` edge `0.0374` maxDD `-0.0208`
- `risk_on_high->equity_4h` score `1.9221` n `43` status `ready` deltaP `15.3467` edge `0.0828` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `1.9221` n `43` status `ready` deltaP `15.3467` edge `0.0828` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.7504` n `145` status `ready` deltaP `17.6524` edge `0.0752` maxDD `-1.0945`
- `risk_on_high->metal_1h` score `1.5584` n `55` status `ready` deltaP `21.4018` edge `0.0086` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.5584` n `55` status `ready` deltaP `21.4018` edge `0.0086` maxDD `-0.0463`
- `market_context_high->unknown_1h` score `1.4545` n `157` status `ready` deltaP `7.8617` edge `0.1169` maxDD `-1.5148`
- `news_risk_high->fx_4h` score `1.2906` n `57` status `ready` deltaP `30.6162` edge `0.0163` maxDD `-0.3953`
- `risk_on_high->index_4h` score `1.1449` n `43` status `ready` deltaP `17.8247` edge `0.0075` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.1449` n `43` status `ready` deltaP `17.8247` edge `0.0075` maxDD `-0.1405`
- `risk_on_high->unknown_1h` score `0.7845` n `55` status `ready` deltaP `-0.9281` edge `0.1155` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

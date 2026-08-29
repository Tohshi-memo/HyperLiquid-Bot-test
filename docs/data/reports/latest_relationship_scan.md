# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T22:52:29.072013+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `risk_on_high->crypto_alt_4h` score `8.3509` n `46` status `ready` deltaP `30.1299` edge `0.5132` maxDD `-0.4529`
- `risk_on_and_context->crypto_alt_4h` score `8.3509` n `46` status `ready` deltaP `30.1299` edge `0.5132` maxDD `-0.4529`
- `news_risk_high->crypto_alt_24h` score `7.2067` n `45` status `ready` deltaP `21.8403` edge `1.1159` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `6.7011` n `46` status `ready` deltaP `35.9292` edge `0.3465` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `6.7011` n `46` status `ready` deltaP `35.9292` edge `0.3465` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.4356` n `54` status `ready` deltaP `0.6154` edge `0.5912` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6838` n `104` status `ready` deltaP `34.415` edge `0.2628` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `3.1648` n `54` status `ready` deltaP `-3.5207` edge `0.3229` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `3.1072` n `46` status `ready` deltaP `34.7893` edge `0.0356` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.1072` n `46` status `ready` deltaP `34.7893` edge `0.0356` maxDD `-0.0208`
- `risk_on_high->equity_4h` score `2.1795` n `46` status `ready` deltaP `17.3184` edge `0.0911` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.1795` n `46` status `ready` deltaP `17.3184` edge `0.0911` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.784` n `148` status `ready` deltaP `18.0578` edge `0.0753` maxDD `-1.0945`
- `market_context_high->unknown_1h` score `1.4689` n `160` status `ready` deltaP `8.4469` edge `0.1142` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.3157` n `46` status `ready` deltaP `19.6447` edge `0.0096` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.3157` n `46` status `ready` deltaP `19.6447` edge `0.0096` maxDD `-0.1405`
- `risk_on_high->metal_1h` score `1.2511` n `58` status `ready` deltaP `17.6957` edge `0.0077` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.2511` n `58` status `ready` deltaP `17.6957` edge `0.0077` maxDD `-0.0463`
- `news_risk_high->fx_4h` score `1.2154` n `54` status `ready` deltaP `29.3191` edge `0.0153` maxDD `-0.3953`
- `risk_on_high->unknown_1h` score `0.8589` n `58` status `ready` deltaP `1.1409` edge `0.1079` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

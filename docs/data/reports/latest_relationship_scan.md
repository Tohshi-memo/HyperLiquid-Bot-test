# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T20:07:24.289339+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11402`

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

- `news_risk_high->unknown_24h` score `29.0355` n `56` status `ready` deltaP `1.8601` edge `2.5046` maxDD `-4.1232`
- `market_context_high->unknown_24h` score `11.7043` n `104` status `ready` deltaP `20.9535` edge `0.9089` maxDD `-3.1917`
- `risk_on_high->crypto_alt_4h` score `11.0127` n `37` status `ready` deltaP `41.7395` edge `0.6495` maxDD `-0.1367`
- `risk_on_and_context->crypto_alt_4h` score `11.0127` n `37` status `ready` deltaP `41.7395` edge `0.6495` maxDD `-0.1367`
- `news_risk_high->crypto_alt_24h` score `10.302` n `56` status `ready` deltaP `27.9514` edge `1.472` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `7.8588` n `37` status `ready` deltaP `39.3004` edge `0.4205` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `7.8588` n `37` status `ready` deltaP `39.3004` edge `0.4205` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.2072` n `65` status `ready` deltaP `6.7308` edge `0.5314` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6922` n `104` status `ready` deltaP `34.415` edge `0.2635` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `3.0419` n `37` status `ready` deltaP `33.5078` edge `0.0387` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0419` n `37` status `ready` deltaP `33.5078` edge `0.0387` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.627` n `65` status `ready` deltaP `-0.9281` edge `0.2608` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.2446` n `65` status `ready` deltaP `33.2833` edge `0.0201` maxDD `-0.3953`
- `market_context_high->unknown_4h` score `1.9692` n `137` status `ready` deltaP `17.062` edge `0.0947` maxDD `-0.881`
- `risk_on_high->equity_4h` score `1.3091` n `37` status `ready` deltaP `10.4442` edge `0.0644` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `1.3091` n `37` status `ready` deltaP `10.4442` edge `0.0644` maxDD `-0.3281`
- `risk_on_high->metal_1h` score `1.2633` n `47` status `ready` deltaP `17.6679` edge `0.0089` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.2633` n `47` status `ready` deltaP `17.6679` edge `0.0089` maxDD `-0.0463`
- `market_context_high->crypto_major_4h` score `0.8096` n `137` status `ready` deltaP `21.8611` edge `0.2668` maxDD `-20.9394`
- `risk_on_high->index_4h` score `0.7421` n `37` status `ready` deltaP `13.2993` edge `0.0041` maxDD `-0.1405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

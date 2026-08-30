# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T00:37:23.599831+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `risk_on_high->crypto_alt_4h` score `6.8092` n `53` status `ready` deltaP `24.8619` edge `0.4327` maxDD `-0.4812`
- `risk_on_and_context->crypto_alt_4h` score `6.8092` n `53` status `ready` deltaP `24.8619` edge `0.4327` maxDD `-0.4812`
- `risk_on_high->crypto_major_4h` score `6.0449` n `53` status `ready` deltaP `33.5913` edge `0.3074` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `6.0449` n `53` status `ready` deltaP `33.5913` edge `0.3074` maxDD `-1.208`
- `market_context_high->metal_24h` score `4.679` n `104` status `ready` deltaP `34.415` edge `0.2624` maxDD `-3.1535`
- `news_risk_high->unknown_4h` score `3.7437` n `47` status `ready` deltaP `-4.4434` edge `0.4006` maxDD `-1.7205`
- `news_risk_high->crypto_alt_24h` score `3.3086` n `43` status `ready` deltaP `20.3933` edge `0.6258` maxDD `-22.3391`
- `news_risk_high->unknown_1h` score `3.2944` n `47` status `ready` deltaP `-9.5649` edge `0.374` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `3.0038` n `53` status `ready` deltaP `33.9162` edge `0.0328` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0038` n `53` status `ready` deltaP `33.9162` edge `0.0328` maxDD `-0.0208`
- `risk_on_high->equity_4h` score `2.5117` n `53` status `ready` deltaP `21.051` edge `0.0939` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.5117` n `53` status `ready` deltaP `21.051` edge `0.0939` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `2.0378` n `155` status `ready` deltaP `17.4646` edge `0.1004` maxDD `-1.0945`
- `risk_on_high->index_4h` score `1.6069` n `53` status `ready` deltaP `23.0902` edge `0.0109` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.6069` n `53` status `ready` deltaP `23.0902` edge `0.0109` maxDD `-0.1405`
- `market_context_high->unknown_1h` score `1.5682` n `167` status `ready` deltaP `8.8324` edge `0.1199` maxDD `-1.5148`
- `risk_on_high->metal_1h` score `1.2407` n `65` status `ready` deltaP `17.6255` edge `0.0073` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.2407` n `65` status `ready` deltaP `17.6255` edge `0.0073` maxDD `-0.0463`
- `risk_on_high->unknown_1h` score `1.225` n `65` status `ready` deltaP `2.4482` edge `0.1297` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `1.225` n `65` status `ready` deltaP `2.4482` edge `0.1297` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

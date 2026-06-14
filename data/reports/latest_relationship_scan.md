# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T19:52:33.947484+00:00`
- Price records: `672`
- Market context records: `3923`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11427`

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

- `risk_on_high->unknown_4h` score `63.6524` n `57` status `ready` deltaP `4.2362` edge `8.3465` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `63.6524` n `57` status `ready` deltaP `4.2362` edge `8.3465` maxDD `-13.467`
- `risk_on_high->equity_24h` score `14.9687` n `39` status `ready` deltaP `42.0139` edge `0.9673` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `14.9687` n `39` status `ready` deltaP `42.0139` edge `0.9673` maxDD `0.0`
- `market_context_high->unknown_4h` score `13.1023` n `194` status `ready` deltaP `-1.5966` edge `1.6434` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `7.708` n `57` status `ready` deltaP `28.9474` edge `0.5159` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `7.708` n `57` status `ready` deltaP `28.9474` edge `0.5159` maxDD `-2.6576`
- `risk_on_high->equity_4h` score `6.5575` n `57` status `ready` deltaP `38.5644` edge `0.2941` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `6.5575` n `57` status `ready` deltaP `38.5644` edge `0.2941` maxDD `-0.0458`
- `risk_on_high->index_24h` score `6.0496` n `39` status `ready` deltaP `30.0347` edge `0.3039` maxDD `0.0`
- `risk_on_and_context->index_24h` score `6.0496` n `39` status `ready` deltaP `30.0347` edge `0.3039` maxDD `0.0`
- `market_context_high->equity_24h` score `4.7532` n `165` status `ready` deltaP `20.8018` edge `0.5604` maxDD `-14.5715`
- `market_context_high->index_24h` score `4.0452` n `165` status `ready` deltaP `25.7923` edge `0.2791` maxDD `-7.1159`
- `market_context_high->crypto_major_4h` score `3.1141` n `194` status `ready` deltaP `19.0722` edge `0.3088` maxDD `-9.4488`
- `risk_on_high->crypto_major_1h` score `2.7217` n `57` status `ready` deltaP `12.8585` edge `0.1953` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `2.7217` n `57` status `ready` deltaP `12.8585` edge `0.1953` maxDD `-2.3372`
- `market_context_high->metal_24h` score `2.5405` n `165` status `ready` deltaP `17.1622` edge `0.2488` maxDD `-9.1203`
- `risk_on_high->crypto_major_24h` score `2.4055` n `39` status `ready` deltaP `-16.7869` edge `0.6911` maxDD `-13.9966`
- `risk_on_and_context->crypto_major_24h` score `2.4055` n `39` status `ready` deltaP `-16.7869` edge `0.6911` maxDD `-13.9966`
- `market_context_high->equity_4h` score `1.8385` n `194` status `ready` deltaP `16.8155` edge `0.2115` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

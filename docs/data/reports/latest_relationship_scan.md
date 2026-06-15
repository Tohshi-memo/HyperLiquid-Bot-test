# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T02:07:32.353027+00:00`
- Price records: `672`
- Market context records: `3949`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11267`

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

- `risk_on_high->unknown_4h` score `144.0526` n `41` status `ready` deltaP `2.7439` edge `12.1673` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.0526` n `41` status `ready` deltaP `2.7439` edge `12.1673` maxDD `-10.8303`
- `market_context_high->unknown_4h` score `18.2499` n `169` status `ready` deltaP `-1.9465` edge `2.0747` maxDD `-35.6052`
- `market_context_high->unknown_24h` score `17.219` n `158` status `ready` deltaP `-9.4871` edge `2.6598` maxDD `-81.2643`
- `risk_on_high->equity_24h` score `9.2567` n `41` status `ready` deltaP `42.0139` edge `0.4913` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2567` n `41` status `ready` deltaP `42.0139` edge `0.4913` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4604` n `41` status `ready` deltaP `36.5854` edge `0.0492` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.4604` n `41` status `ready` deltaP `36.5854` edge `0.0492` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.3949` n `158` status `ready` deltaP `26.0636` edge `0.2231` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.3734` n `158` status `ready` deltaP `17.493` edge `0.316` maxDD `-9.1203`
- `market_context_high->equity_24h` score `3.2392` n `158` status `ready` deltaP `19.862` edge `0.4405` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.8689` n `41` status `ready` deltaP `29.8611` edge `0.04` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8689` n `41` status `ready` deltaP `29.8611` edge `0.04` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.9752` n `41` status `ready` deltaP `22.1036` edge `0.0838` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9752` n `41` status `ready` deltaP `22.1036` edge `0.0838` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.9713` n `169` status `ready` deltaP `18.7554` edge `0.1959` maxDD `-7.8662`
- `market_context_high->equity_4h` score `1.6737` n `169` status `ready` deltaP `16.6113` edge `0.159` maxDD `-7.0879`
- `market_context_high->crypto_major_1h` score `0.6862` n `169` status `ready` deltaP `11.0823` edge `0.0821` maxDD `-4.904`
- `market_context_high->metal_1h` score `0.6782` n `169` status `ready` deltaP `10.6757` edge `0.0489` maxDD `-2.751`
- `risk_on_high->commodity_24h` score `0.6143` n `41` status `ready` deltaP `3.5569` edge `0.2684` maxDD `-13.9406`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T06:52:35.503550+00:00`
- Price records: `672`
- Market context records: `3968`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10092`

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

- `risk_on_high->unknown_4h` score `148.1135` n `40` status `ready` deltaP `0.9451` edge `12.5177` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.1135` n `40` status `ready` deltaP `0.9451` edge `12.5177` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `34.3302` n `147` status `ready` deltaP `-7.0508` edge `3.4821` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `21.0924` n `161` status `ready` deltaP `1.8302` edge `2.2864` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.0707` n `40` status `ready` deltaP `42.0139` edge `0.4758` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0707` n `40` status `ready` deltaP `42.0139` edge `0.4758` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4687` n `40` status `ready` deltaP `37.439` edge `0.0442` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.4687` n `40` status `ready` deltaP `37.439` edge `0.0442` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.2799` n `147` status `ready` deltaP `16.2947` edge `0.3162` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.1154` n `147` status `ready` deltaP `25.7795` edge `0.2017` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.7453` n `40` status `ready` deltaP `29.8611` edge `0.0297` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7453` n `40` status `ready` deltaP `29.8611` edge `0.0297` maxDD `0.0`
- `market_context_high->equity_4h` score `2.3795` n `161` status `ready` deltaP `20.0632` edge `0.1948` maxDD `-7.0879`
- `market_context_high->equity_24h` score `2.3146` n `147` status `ready` deltaP `18.2044` edge `0.3745` maxDD `-14.5715`
- `market_context_high->crypto_major_4h` score `2.2923` n `161` status `ready` deltaP `20.068` edge `0.2139` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.72` n `40` status `ready` deltaP `20.5183` edge `0.0731` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.72` n `40` status `ready` deltaP `20.5183` edge `0.0731` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6364` n `166` status `ready` deltaP `12.6578` edge `0.1062` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1475` n `166` status `ready` deltaP `9.9813` edge `0.0855` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.1409` n `166` status `ready` deltaP `13.0889` edge `0.0672` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

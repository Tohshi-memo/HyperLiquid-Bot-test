# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T11:07:30.875438+00:00`
- Price records: `672`
- Market context records: `3985`
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

- `risk_on_high->unknown_4h` score `147.3511` n `40` status `ready` deltaP `-1.189` edge `12.4684` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.3511` n `40` status `ready` deltaP `-1.189` edge `12.4684` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `33.1173` n `150` status `ready` deltaP `-7.1042` edge `3.2753` maxDD `-29.453`
- `market_context_high->unknown_4h` score `20.2124` n `163` status `ready` deltaP `0.8202` edge `2.2198` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.3203` n `40` status `ready` deltaP `42.0139` edge `0.4966` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3203` n `40` status `ready` deltaP `42.0139` edge `0.4966` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.8145` n `40` status `ready` deltaP `37.5915` edge `0.072` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.8145` n `40` status `ready` deltaP `37.5915` edge `0.072` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.3984` n `150` status `ready` deltaP `16.7709` edge `0.3229` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.2803` n `150` status `ready` deltaP `25.8611` edge `0.2149` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.8113` n `40` status `ready` deltaP `29.8611` edge `0.0352` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8113` n `40` status `ready` deltaP `29.8611` edge `0.0352` maxDD `0.0`
- `market_context_high->equity_24h` score `2.7883` n `150` status `ready` deltaP `18.6806` edge `0.4108` maxDD `-14.5715`
- `market_context_high->equity_4h` score `2.5024` n `163` status `ready` deltaP `20.4596` edge `0.2024` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.1083` n `163` status `ready` deltaP `19.0277` edge `0.2055` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.9702` n `40` status `ready` deltaP `20.9756` edge `0.0909` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9702` n `40` status `ready` deltaP `20.9756` edge `0.0909` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.4465` n `163` status `ready` deltaP `11.6932` edge `0.0968` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.0759` n `163` status `ready` deltaP `9.5212` edge `0.0826` maxDD `-2.1799`
- `market_context_high->crypto_alt_4h` score `0.9217` n `163` status `ready` deltaP `13.3763` edge `0.1181` maxDD `-7.1038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

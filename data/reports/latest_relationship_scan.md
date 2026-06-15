# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T07:22:32.285756+00:00`
- Price records: `672`
- Market context records: `3970`
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

- `risk_on_high->unknown_4h` score `148.0965` n `40` status `ready` deltaP `0.7927` edge `12.5173` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.0965` n `40` status `ready` deltaP `0.7927` edge `12.5173` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `32.8266` n `149` status `ready` deltaP `-6.7953` edge `3.3551` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `20.454` n `163` status `ready` deltaP `1.5749` edge `2.2349` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.1259` n `40` status `ready` deltaP `42.0139` edge `0.4804` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1259` n `40` status `ready` deltaP `42.0139` edge `0.4804` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4987` n `40` status `ready` deltaP `37.439` edge `0.0467` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.4987` n `40` status `ready` deltaP `37.439` edge `0.0467` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.4687` n `149` status `ready` deltaP `16.6143` edge `0.3298` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.2266` n `149` status `ready` deltaP `25.8343` edge `0.2106` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.7585` n `40` status `ready` deltaP `29.8611` edge `0.0308` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7585` n `40` status `ready` deltaP `29.8611` edge `0.0308` maxDD `0.0`
- `market_context_high->equity_24h` score `2.6042` n `149` status `ready` deltaP `18.524` edge `0.3965` maxDD `-14.5715`
- `market_context_high->equity_4h` score `2.3978` n `163` status `ready` deltaP `20.3071` edge `0.1947` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.2848` n `163` status `ready` deltaP `20.2585` edge `0.212` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.703` n `40` status `ready` deltaP `20.3659` edge `0.0727` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.703` n `40` status `ready` deltaP `20.3659` edge `0.0727` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6616` n `166` status `ready` deltaP `12.8075` edge `0.1073` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1703` n `166` status `ready` deltaP `9.9813` edge `0.0874` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.1253` n `166` status `ready` deltaP `12.9392` edge `0.0669` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

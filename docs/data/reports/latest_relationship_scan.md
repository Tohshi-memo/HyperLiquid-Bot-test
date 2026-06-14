# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T07:07:34.288290+00:00`
- Price records: `672`
- Market context records: `3869`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13656`

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

- `risk_on_high->unknown_4h` score `48.5099` n `72` status `ready` deltaP `7.7235` edge `6.3819` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `48.5099` n `72` status `ready` deltaP `7.7235` edge `6.3819` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.243` n `32` status `ready` deltaP `34.0278` edge `2.631` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.243` n `32` status `ready` deltaP `34.0278` edge `2.631` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8751` n `32` status `ready` deltaP `42.0139` edge `1.9595` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8751` n `32` status `ready` deltaP `42.0139` edge `1.9595` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.3298` n `32` status `ready` deltaP `31.4236` edge `1.7498` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.3298` n `32` status `ready` deltaP `31.4236` edge `1.7498` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.1707` n `32` status `ready` deltaP `30.2083` edge `0.7295` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.1707` n `32` status `ready` deltaP `30.2083` edge `0.7295` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.8372` n `206` status `ready` deltaP `-0.1244` edge `1.5465` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.6096` n `137` status `ready` deltaP `16.4665` edge `0.744` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.6056` n `72` status `ready` deltaP `19.6138` edge `0.4486` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.6056` n `72` status `ready` deltaP `19.6138` edge `0.4486` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.5761` n `137` status `ready` deltaP `25.0988` edge `0.4113` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.456` n `137` status `ready` deltaP `20.846` edge `0.2922` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6337` n `72` status `ready` deltaP `25.8638` edge `0.1605` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6337` n `72` status `ready` deltaP `25.8638` edge `0.1605` maxDD `-5.7426`
- `market_context_high->unknown_24h` score `2.5201` n `137` status `ready` deltaP `-21.8446` edge `3.3169` maxDD `-200.1879`
- `market_context_high->crypto_major_24h` score `2.2693` n `137` status `ready` deltaP `2.8462` edge `0.6165` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T00:21:42.719508+00:00`
- Price records: `672`
- Market context records: `3942`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11355`

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

- `risk_on_high->unknown_4h` score `144.3609` n `41` status `ready` deltaP `3.6586` edge `12.1869` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.3609` n `41` status `ready` deltaP `3.6586` edge `12.1869` maxDD `-10.8303`
- `market_context_high->unknown_4h` score `16.3457` n `176` status `ready` deltaP `-3.1735` edge `1.9242` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.3407` n `41` status `ready` deltaP `42.0139` edge `0.4983` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3407` n `41` status `ready` deltaP `42.0139` edge `0.4983` maxDD `0.0`
- `market_context_high->unknown_24h` score `7.9961` n `165` status `ready` deltaP `-10.3662` edge `2.2013` maxDD `-103.2681`
- `risk_on_high->equity_4h` score `3.7149` n `41` status `ready` deltaP `37.6525` edge `0.0633` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.7149` n `41` status `ready` deltaP `37.6525` edge `0.0633` maxDD `-0.0458`
- `market_context_high->equity_24h` score `3.5784` n `165` status `ready` deltaP `20.8018` edge `0.4625` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.4176` n `165` status `ready` deltaP `25.7923` edge `0.2268` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.2727` n `165` status `ready` deltaP `16.7298` edge `0.3127` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.9296` n `41` status `ready` deltaP `30.0347` edge `0.0439` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.9296` n `41` status `ready` deltaP `30.0347` edge `0.0439` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `2.4122` n `41` status `ready` deltaP `23.1707` edge `0.1131` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.4122` n `41` status `ready` deltaP `23.1707` edge `0.1131` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.3661` n `176` status `ready` deltaP `17.0455` edge `0.174` maxDD `-9.2368`
- `market_context_high->equity_4h` score `0.8992` n `176` status `ready` deltaP `14.6896` edge `0.1474` maxDD `-8.2982`
- `risk_on_high->metal_24h` score `0.7921` n `41` status `ready` deltaP `-15.1254` edge `0.2638` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.7921` n `41` status `ready` deltaP `-15.1254` edge `0.2638` maxDD `-1.9133`
- `risk_on_high->commodity_24h` score `0.5879` n `41` status `ready` deltaP `3.5569` edge `0.2662` maxDD `-13.9406`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

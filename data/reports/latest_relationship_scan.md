# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T05:22:28.710914+00:00`
- Price records: `672`
- Market context records: `3656`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13201`

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

- `risk_on_high->crypto_major_24h` score `35.5034` n `32` status `ready` deltaP `40.7986` edge `2.6909` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `35.5034` n `32` status `ready` deltaP `40.7986` edge `2.6909` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `31.4374` n `32` status `ready` deltaP `42.8819` edge `2.3339` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `31.4374` n `32` status `ready` deltaP `42.8819` edge `2.3339` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `27.5588` n `32` status `ready` deltaP `39.9306` edge `2.0455` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `27.5588` n `32` status `ready` deltaP `39.9306` edge `2.0455` maxDD `-0.8779`
- `risk_on_high->index_24h` score `17.8282` n `32` status `ready` deltaP `42.8819` edge `1.1998` maxDD `0.0`
- `risk_on_and_context->index_24h` score `17.8282` n `32` status `ready` deltaP `42.8819` edge `1.1998` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.2356` n `32` status `ready` deltaP `19.9695` edge `0.9154` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.2356` n `32` status `ready` deltaP `19.9695` edge `0.9154` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `9.5434` n `32` status `ready` deltaP `28.4722` edge `0.6316` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `9.5434` n `32` status `ready` deltaP `28.4722` edge `0.6316` maxDD `-0.7574`
- `market_context_high->index_24h` score `7.4321` n `157` status `ready` deltaP `28.2322` edge `0.6027` maxDD `-11.3924`
- `market_context_high->equity_24h` score `7.1494` n `157` status `ready` deltaP `19.952` edge `1.0292` maxDD `-35.3144`
- `risk_on_high->crypto_alt_4h` score `2.5286` n `32` status `ready` deltaP `0.3811` edge `0.3926` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.5286` n `32` status `ready` deltaP `0.3811` edge `0.3926` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.4636` n `32` status `ready` deltaP `9.375` edge `0.3668` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4636` n `32` status `ready` deltaP `9.375` edge `0.3668` maxDD `-5.7426`
- `market_context_high->metal_24h` score `2.4223` n `157` status `ready` deltaP `22.7795` edge `0.5539` maxDD `-21.6171`
- `market_context_high->crypto_major_24h` score `1.4984` n `157` status `ready` deltaP `6.9809` edge `0.785` maxDD `-49.5335`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

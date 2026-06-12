# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T19:26:01.037501+00:00`
- Price records: `672`
- Market context records: `3716`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13025`

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

- `risk_on_high->crypto_major_24h` score `29.6486` n `32` status `ready` deltaP `31.4236` edge `2.2655` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.6486` n `32` status `ready` deltaP `31.4236` edge `2.2655` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.3923` n `32` status `ready` deltaP `33.3333` edge `1.6438` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.3923` n `32` status `ready` deltaP `33.3333` edge `1.6438` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.7761` n `32` status `ready` deltaP `30.9028` edge `1.6238` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.7761` n `32` status `ready` deltaP `30.9028` edge `1.6238` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.8016` n `32` status `ready` deltaP `33.1597` edge `0.7624` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.8016` n `32` status `ready` deltaP `33.1597` edge `0.7624` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.0873` n `32` status `ready` deltaP `17.2256` edge `0.838` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.0873` n `32` status `ready` deltaP `17.2256` edge `0.838` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.6125` n `162` status `ready` deltaP `23.2832` edge `0.3431` maxDD `-7.1159`
- `market_context_high->equity_24h` score `4.5046` n `162` status `ready` deltaP `15.4321` edge `0.5774` maxDD `-16.7253`
- `risk_on_high->metal_24h` score `2.1608` n `32` status `ready` deltaP `18.75` edge `0.0812` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `2.1608` n `32` status `ready` deltaP `18.75` edge `0.0812` maxDD `-0.7574`
- `market_context_high->metal_24h` score `1.8356` n `162` status `ready` deltaP `18.5185` edge `0.2589` maxDD `-10.6843`
- `risk_on_high->crypto_alt_4h` score `1.7587` n `32` status `ready` deltaP `-1.1433` edge `0.3386` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.7587` n `32` status `ready` deltaP `-1.1433` edge `0.3386` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `1.5673` n `32` status `ready` deltaP `8.3079` edge `0.259` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5673` n `32` status `ready` deltaP `8.3079` edge `0.259` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `0.9611` n `32` status `ready` deltaP `1.7777` edge `0.2183` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

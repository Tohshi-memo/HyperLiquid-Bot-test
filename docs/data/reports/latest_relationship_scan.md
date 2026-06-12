# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T06:21:37.695276+00:00`
- Price records: `672`
- Market context records: `3660`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13157`

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

- `risk_on_high->crypto_major_24h` score `34.9139` n `32` status `ready` deltaP `40.1042` edge `2.6464` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.9139` n `32` status `ready` deltaP `40.1042` edge `2.6464` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `30.5514` n `32` status `ready` deltaP `42.1875` edge `2.2647` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `30.5514` n `32` status `ready` deltaP `42.1875` edge `2.2647` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `26.842` n `32` status `ready` deltaP `39.2361` edge `1.9904` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `26.842` n `32` status `ready` deltaP `39.2361` edge `1.9904` maxDD `-0.8779`
- `risk_on_high->index_24h` score `17.2794` n `32` status `ready` deltaP `42.1875` edge `1.1587` maxDD `0.0`
- `risk_on_and_context->index_24h` score `17.2794` n `32` status `ready` deltaP `42.1875` edge `1.1587` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.208` n `32` status `ready` deltaP `19.9695` edge `0.9131` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.208` n `32` status `ready` deltaP `19.9695` edge `0.9131` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `8.9238` n `32` status `ready` deltaP `27.7778` edge `0.5846` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `8.9238` n `32` status `ready` deltaP `27.7778` edge `0.5846` maxDD `-0.7574`
- `market_context_high->index_24h` score `6.8834` n `157` status `ready` deltaP `27.5378` edge `0.5616` maxDD `-11.3924`
- `market_context_high->equity_24h` score `6.2634` n `157` status `ready` deltaP `19.2576` edge `0.96` maxDD `-35.3144`
- `risk_on_high->equity_4h` score `2.4926` n `32` status `ready` deltaP `9.5274` edge `0.3695` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4926` n `32` status `ready` deltaP `9.5274` edge `0.3695` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `2.4252` n `32` status `ready` deltaP `0.2287` edge `0.385` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.4252` n `32` status `ready` deltaP `0.2287` edge `0.385` maxDD `-11.7537`
- `market_context_high->metal_24h` score `2.0196` n `157` status `ready` deltaP `22.0851` edge `0.5069` maxDD `-21.6171`
- `risk_on_high->crypto_major_1h` score `1.2121` n `32` status `ready` deltaP `3.125` edge `0.2415` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T23:52:33.405671+00:00`
- Price records: `672`
- Market context records: `3633`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `39.733` n `32` status `ready` deltaP `44.6181` edge `3.0179` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `39.733` n `32` status `ready` deltaP `44.6181` edge `3.0179` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `36.5357` n `32` status `ready` deltaP `46.7014` edge `2.7333` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `36.5357` n `32` status `ready` deltaP `46.7014` edge `2.7333` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `32.1267` n `32` status `ready` deltaP `43.75` edge `2.4007` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `32.1267` n `32` status `ready` deltaP `43.75` edge `2.4007` maxDD `-0.8779`
- `risk_on_high->index_24h` score `20.9273` n `32` status `ready` deltaP `46.7014` edge `1.4326` maxDD `0.0`
- `risk_on_and_context->index_24h` score `20.9273` n `32` status `ready` deltaP `46.7014` edge `1.4326` maxDD `0.0`
- `risk_on_high->metal_24h` score `13.2341` n `32` status `ready` deltaP `32.2917` edge `0.9137` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.2341` n `32` status `ready` deltaP `32.2917` edge `0.9137` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `12.2476` n `32` status `ready` deltaP `22.1037` edge `0.9855` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.2476` n `32` status `ready` deltaP `22.1037` edge `0.9855` maxDD `-5.9781`
- `market_context_high->equity_24h` score `10.8057` n `158` status `ready` deltaP `23.2837` edge `1.3865` maxDD `-40.9667`
- `market_context_high->index_24h` score `9.5774` n `158` status `ready` deltaP `31.5115` edge `0.8097` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `4.4104` n `158` status `ready` deltaP `10.4013` edge `1.0713` maxDD `-54.8486`
- `market_context_high->metal_24h` score `4.1266` n `158` status `ready` deltaP `26.1999` edge `0.8084` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `3.7518` n `32` status `ready` deltaP `2.5152` edge `0.4803` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.7518` n `32` status `ready` deltaP `2.5152` edge `0.4803` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.6788` n `32` status `ready` deltaP `11.0518` edge `0.3832` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6788` n `32` status `ready` deltaP `11.0518` edge `0.3832` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

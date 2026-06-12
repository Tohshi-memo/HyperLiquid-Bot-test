# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T00:07:27.876324+00:00`
- Price records: `672`
- Market context records: `3634`
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

- `risk_on_high->crypto_major_24h` score `39.4971` n `32` status `ready` deltaP `44.4444` edge `2.9994` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `39.4971` n `32` status `ready` deltaP `44.4444` edge `2.9994` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `36.2818` n `32` status `ready` deltaP `46.5278` edge `2.7133` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `36.2818` n `32` status `ready` deltaP `46.5278` edge `2.7133` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `31.8812` n `32` status `ready` deltaP `43.5764` edge `2.3814` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `31.8812` n `32` status `ready` deltaP `43.5764` edge `2.3814` maxDD `-0.8779`
- `risk_on_high->index_24h` score `20.7718` n `32` status `ready` deltaP `46.5278` edge `1.4208` maxDD `0.0`
- `risk_on_and_context->index_24h` score `20.7718` n `32` status `ready` deltaP `46.5278` edge `1.4208` maxDD `0.0`
- `risk_on_high->metal_24h` score `13.0318` n `32` status `ready` deltaP `32.1181` edge `0.898` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.0318` n `32` status `ready` deltaP `32.1181` edge `0.898` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `12.1934` n `32` status `ready` deltaP `21.9512` edge `0.982` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.1934` n `32` status `ready` deltaP `21.9512` edge `0.982` maxDD `-5.9781`
- `market_context_high->equity_24h` score `10.5518` n `158` status `ready` deltaP `23.1101` edge `1.3665` maxDD `-40.9667`
- `market_context_high->index_24h` score `9.4219` n `158` status `ready` deltaP `31.3379` edge `0.7979` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `4.1745` n `158` status `ready` deltaP `10.2276` edge `1.0528` maxDD `-54.8486`
- `market_context_high->metal_24h` score `3.9951` n `158` status `ready` deltaP `26.0263` edge `0.7927` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `3.6844` n `32` status `ready` deltaP `2.3628` edge `0.4757` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.6844` n `32` status `ready` deltaP `2.3628` edge `0.4757` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.6529` n `32` status `ready` deltaP `10.8994` edge `0.3809` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6529` n `32` status `ready` deltaP `10.8994` edge `0.3809` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

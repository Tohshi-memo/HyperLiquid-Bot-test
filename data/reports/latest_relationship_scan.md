# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T21:07:37.629009+00:00`
- Price records: `672`
- Market context records: `3621`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13162`

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

- `risk_on_high->crypto_major_24h` score `42.0974` n `32` status `ready` deltaP `46.5278` edge `3.2022` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `42.0974` n `32` status `ready` deltaP `46.5278` edge `3.2022` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `39.1665` n `32` status `ready` deltaP `48.6111` edge `2.9398` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `39.1665` n `32` status `ready` deltaP `48.6111` edge `2.9398` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `34.7383` n `32` status `ready` deltaP `45.6597` edge `2.6056` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `34.7383` n `32` status `ready` deltaP `45.6597` edge `2.6056` maxDD `-0.8779`
- `risk_on_high->index_24h` score `22.6593` n `32` status `ready` deltaP `48.6111` edge `1.5642` maxDD `0.0`
- `risk_on_and_context->index_24h` score `22.6593` n `32` status `ready` deltaP `48.6111` edge `1.5642` maxDD `0.0`
- `risk_on_high->metal_24h` score `15.3417` n `32` status `ready` deltaP `34.2014` edge `1.0766` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.3417` n `32` status `ready` deltaP `34.2014` edge `1.0766` maxDD `-0.7574`
- `market_context_high->equity_24h` score `13.4365` n `158` status `ready` deltaP `25.1934` edge `1.593` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `12.5186` n `32` status `ready` deltaP `22.8659` edge `1.003` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.5186` n `32` status `ready` deltaP `22.8659` edge `1.003` maxDD `-5.9781`
- `market_context_high->index_24h` score `11.3094` n `158` status `ready` deltaP `33.4212` edge `0.9413` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `6.7748` n `158` status `ready` deltaP `12.311` edge `1.2556` maxDD `-54.8486`
- `market_context_high->metal_24h` score `5.4965` n `158` status `ready` deltaP `28.1096` edge `0.9713` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.1273` n `32` status `ready` deltaP `3.4299` edge `0.5055` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.1273` n `32` status `ready` deltaP `3.4299` edge `0.5055` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.053` n `32` status `ready` deltaP `12.7287` edge `0.42` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.053` n `32` status `ready` deltaP `12.7287` edge `0.42` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

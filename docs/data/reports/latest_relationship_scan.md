# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T19:07:33.177791+00:00`
- Price records: `672`
- Market context records: `3612`
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

- `risk_on_high->crypto_major_24h` score `44.0709` n `32` status `ready` deltaP `47.9167` edge `3.3574` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `44.0709` n `32` status `ready` deltaP `47.9167` edge `3.3574` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `40.9948` n `32` status `ready` deltaP `50.0` edge `3.0829` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `40.9948` n `32` status `ready` deltaP `50.0` edge `3.0829` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `36.9938` n `32` status `ready` deltaP `47.0486` edge `2.7843` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `36.9938` n `32` status `ready` deltaP `47.0486` edge `2.7843` maxDD `-0.8779`
- `risk_on_high->index_24h` score `23.884` n `32` status `ready` deltaP `50.0` edge `1.657` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.884` n `32` status `ready` deltaP `50.0` edge `1.657` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.7908` n `32` status `ready` deltaP `35.5903` edge `1.1881` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.7908` n `32` status `ready` deltaP `35.5903` edge `1.1881` maxDD `-0.7574`
- `market_context_high->equity_24h` score `15.2648` n `158` status `ready` deltaP `26.5823` edge `1.7361` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `12.9881` n `32` status `ready` deltaP `24.0854` edge `1.034` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.9881` n `32` status `ready` deltaP `24.0854` edge `1.034` maxDD `-5.9781`
- `market_context_high->index_24h` score `12.5341` n `158` status `ready` deltaP `34.8101` edge `1.0341` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `8.7483` n `158` status `ready` deltaP `13.6999` edge `1.4108` maxDD `-54.8486`
- `market_context_high->metal_24h` score `6.4384` n `158` status `ready` deltaP `29.4985` edge `1.0828` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.6581` n `32` status `ready` deltaP `4.6494` edge `0.5416` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.6581` n `32` status `ready` deltaP `4.6494` edge `0.5416` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.4331` n `32` status `ready` deltaP `13.9482` edge `0.4606` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.4331` n `32` status `ready` deltaP `13.9482` edge `0.4606` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

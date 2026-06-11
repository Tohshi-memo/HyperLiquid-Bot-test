# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T08:22:32.556049+00:00`
- Price records: `672`
- Market context records: `3566`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13076`

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

- `risk_on_high->crypto_major_24h` score `50.0309` n `32` status `ready` deltaP `54.5873` edge `3.8096` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `50.0309` n `32` status `ready` deltaP `54.5873` edge `3.8096` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `44.4344` n `32` status `ready` deltaP `54.2407` edge `3.3564` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `44.4344` n `32` status `ready` deltaP `54.2407` edge `3.3564` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.2778` n `32` status `ready` deltaP `53.5529` edge `3.3328` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.2778` n `32` status `ready` deltaP `53.5529` edge `3.3328` maxDD `0.0`
- `risk_on_high->index_24h` score `25.5712` n `32` status `ready` deltaP `53.8995` edge `1.7716` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.5712` n `32` status `ready` deltaP `53.8995` edge `1.7716` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.6517` n `32` status `ready` deltaP `36.8609` edge `1.3347` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6517` n `32` status `ready` deltaP `36.8609` edge `1.3347` maxDD `-0.7574`
- `market_context_high->equity_24h` score `18.6339` n `156` status `ready` deltaP `30.476` edge `1.9909` maxDD `-40.9667`
- `market_context_high->crypto_major_24h` score `14.5969` n `156` status `ready` deltaP `19.8918` edge `1.8569` maxDD `-54.8486`
- `market_context_high->index_24h` score `14.1865` n `156` status `ready` deltaP `38.5149` edge `1.1471` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.1523` n `32` status `ready` deltaP `24.8476` edge `1.0426` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.1523` n `32` status `ready` deltaP `24.8476` edge `1.0426` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `10.3472` n `156` status `ready` deltaP `14.417` edge `1.5704` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6151` n `156` status `ready` deltaP `30.9314` edge `1.2241` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.6395` n `32` status `ready` deltaP `5.1067` edge `0.537` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.6395` n `32` status `ready` deltaP `5.1067` edge `0.537` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.477` n `32` status `ready` deltaP `14.253` edge `0.4642` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

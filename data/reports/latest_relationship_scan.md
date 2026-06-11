# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T10:22:32.679241+00:00`
- Price records: `672`
- Market context records: `3575`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13114`

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

- `risk_on_high->crypto_major_24h` score `49.0848` n `32` status `ready` deltaP `53.2008` edge `3.74` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `49.0848` n `32` status `ready` deltaP `53.2008` edge `3.74` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `43.906` n `32` status `ready` deltaP `52.3397` edge `3.3099` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `43.906` n `32` status `ready` deltaP `52.3397` edge `3.3099` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `43.2531` n `32` status `ready` deltaP `52.8542` edge `3.2672` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `43.2531` n `32` status `ready` deltaP `52.8542` edge `3.2672` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.4285` n `32` status `ready` deltaP `52.6863` edge `1.7678` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.4285` n `32` status `ready` deltaP `52.6863` edge `1.7678` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.6337` n `32` status `ready` deltaP `36.8609` edge `1.3332` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6337` n `32` status `ready` deltaP `36.8609` edge `1.3332` maxDD `-0.7574`
- `market_context_high->equity_24h` score `18.262` n `156` status `ready` deltaP `29.2628` edge `1.968` maxDD `-40.9667`
- `market_context_high->index_24h` score `14.0438` n `156` status `ready` deltaP `37.3017` edge `1.1433` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `13.6507` n `156` status `ready` deltaP `18.5053` edge `1.7873` maxDD `-54.8486`
- `risk_on_high->crypto_major_4h` score `13.1835` n `32` status `ready` deltaP `24.8476` edge `1.0452` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.1835` n `32` status `ready` deltaP `24.8476` edge `1.0452` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `9.1659` n `156` status `ready` deltaP `13.0305` edge `1.4812` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6034` n `156` status `ready` deltaP `30.9314` edge `1.2226` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.7381` n `32` status `ready` deltaP `5.2591` edge `0.5442` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.7381` n `32` status `ready` deltaP `5.2591` edge `0.5442` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.4175` n `32` status `ready` deltaP `13.9482` edge `0.4586` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

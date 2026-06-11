# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T15:37:30.373268+00:00`
- Price records: `672`
- Market context records: `3597`
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

- `risk_on_high->crypto_major_24h` score `46.6722` n `32` status `ready` deltaP `49.9079` edge `3.5609` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `46.6722` n `32` status `ready` deltaP `49.9079` edge `3.5609` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `43.0686` n `32` status `ready` deltaP `51.4731` edge `3.2459` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `43.0686` n `32` status `ready` deltaP `51.4731` edge `3.2459` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `40.1414` n `32` status `ready` deltaP `49.388` edge `3.031` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `40.1414` n `32` status `ready` deltaP `49.388` edge `3.031` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.18` n `32` status `ready` deltaP `52.3397` edge `1.7494` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.18` n `32` status `ready` deltaP `52.3397` edge `1.7494` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.2137` n `32` status `ready` deltaP `36.8609` edge `1.2982` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.2137` n `32` status `ready` deltaP `36.8609` edge `1.2982` maxDD `-0.7574`
- `market_context_high->equity_24h` score `17.4247` n `156` status `ready` deltaP `28.3962` edge `1.904` maxDD `-40.9667`
- `market_context_high->index_24h` score `13.7953` n `156` status `ready` deltaP `36.9551` edge `1.1249` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.4447` n `32` status `ready` deltaP `25.4573` edge `1.0629` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.4447` n `32` status `ready` deltaP `25.4573` edge `1.0629` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `11.2381` n `156` status `ready` deltaP `15.2124` edge `1.6082` maxDD `-54.8486`
- `market_context_high->metal_24h` score `7.3304` n `156` status `ready` deltaP `30.9314` edge `1.1876` maxDD `-25.9879`
- `market_context_high->crypto_alt_24h` score `6.0542` n `156` status `ready` deltaP `9.5643` edge `1.245` maxDD `-56.6728`
- `risk_on_high->crypto_alt_4h` score `5.2996` n `32` status `ready` deltaP `6.1738` edge `0.5849` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.2996` n `32` status `ready` deltaP `6.1738` edge `0.5849` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7345` n `32` status `ready` deltaP `15.3201` edge `0.4901` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

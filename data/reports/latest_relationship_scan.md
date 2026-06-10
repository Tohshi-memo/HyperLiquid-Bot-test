# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T03:37:34.115929+00:00`
- Price records: `672`
- Market context records: `3447`
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

- `risk_on_high->crypto_alt_24h` score `56.3876` n `32` status `ready` deltaP `59.8958` edge `4.3148` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `56.3876` n `32` status `ready` deltaP `59.8958` edge `4.3148` maxDD `-0.8779`
- `risk_on_high->crypto_major_24h` score `56.3397` n `32` status `ready` deltaP `58.5069` edge `4.3092` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.3397` n `32` status `ready` deltaP `58.5069` edge `4.3092` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `44.9681` n `32` status `ready` deltaP `56.0764` edge `3.3735` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.9681` n `32` status `ready` deltaP `56.0764` edge `3.3735` maxDD `0.0`
- `risk_on_high->index_24h` score `23.8523` n `32` status `ready` deltaP `51.3889` edge `1.6451` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.8523` n `32` status `ready` deltaP `51.3889` edge `1.6451` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.6133` n `154` status `ready` deltaP `20.813` edge `2.5416` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.4622` n `154` status `ready` deltaP `24.6189` edge `2.3975` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.7493` n `154` status `ready` deltaP `33.3491` edge `2.0647` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `15.276` n `32` status `ready` deltaP `28.3537` edge `1.1962` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.276` n `32` status `ready` deltaP `28.3537` edge `1.1962` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.5762` n `32` status `ready` deltaP `28.9931` edge `0.9642` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.5762` n `32` status `ready` deltaP `28.9931` edge `0.9642` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.6596` n `154` status `ready` deltaP `36.4538` edge `1.0336` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.0546` n `32` status `ready` deltaP `8.4604` edge `0.7159` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.0546` n `32` status `ready` deltaP `8.4604` edge `0.7159` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.5636` n `154` status `ready` deltaP `23.8795` edge `0.8799` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.4963` n `32` status `ready` deltaP `18.6738` edge `0.5654` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

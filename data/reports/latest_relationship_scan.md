# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T23:37:25.610388+00:00`
- Price records: `672`
- Market context records: `3430`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13160`

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

- `risk_on_high->crypto_alt_24h` score `56.7106` n `32` status `ready` deltaP `60.2431` edge `4.3394` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `56.7106` n `32` status `ready` deltaP `60.2431` edge `4.3394` maxDD `-0.8779`
- `risk_on_high->crypto_major_24h` score `56.3841` n `32` status `ready` deltaP `58.5069` edge `4.3129` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.3841` n `32` status `ready` deltaP `58.5069` edge `4.3129` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `45.4589` n `32` status `ready` deltaP `56.0764` edge `3.4144` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.4589` n `32` status `ready` deltaP `56.0764` edge `3.4144` maxDD `0.0`
- `risk_on_high->index_24h` score `23.9459` n `32` status `ready` deltaP `51.3889` edge `1.6529` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.9459` n `32` status `ready` deltaP `51.3889` edge `1.6529` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.9363` n `154` status `ready` deltaP `21.1603` edge `2.5662` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.5066` n `154` status `ready` deltaP `24.6189` edge `2.4012` maxDD `-54.8486`
- `market_context_high->equity_24h` score `20.2401` n `154` status `ready` deltaP `33.3491` edge `2.1056` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `14.747` n `32` status `ready` deltaP `26.6768` edge `1.1633` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.747` n `32` status `ready` deltaP `26.6768` edge `1.1633` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.3194` n `32` status `ready` deltaP `28.9931` edge `0.9428` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.3194` n `32` status `ready` deltaP `28.9931` edge `0.9428` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.7532` n `154` status `ready` deltaP `36.4538` edge `1.0414` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `6.4164` n `32` status `ready` deltaP `6.7835` edge `0.6739` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.4164` n `32` status `ready` deltaP `6.7835` edge `0.6739` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.3967` n `154` status `ready` deltaP `23.8795` edge `0.8585` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.2886` n `32` status `ready` deltaP `16.5396` edge `0.553` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

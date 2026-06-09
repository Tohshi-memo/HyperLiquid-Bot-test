# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T19:52:30.689197+00:00`
- Price records: `672`
- Market context records: `3414`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13116`

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

- `risk_on_high->crypto_major_24h` score `55.8554` n `32` status `ready` deltaP `58.3333` edge `4.27` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.8554` n `32` status `ready` deltaP `58.3333` edge `4.27` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `55.5868` n `32` status `ready` deltaP `57.9861` edge `4.2608` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `55.5868` n `32` status `ready` deltaP `57.9861` edge `4.2608` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.8645` n `32` status `ready` deltaP `56.0764` edge `3.4482` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.8645` n `32` status `ready` deltaP `56.0764` edge `3.4482` maxDD `0.0`
- `risk_on_high->index_24h` score `23.9063` n `32` status `ready` deltaP `51.3889` edge `1.6496` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.9063` n `32` status `ready` deltaP `51.3889` edge `1.6496` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.8125` n `154` status `ready` deltaP `18.9033` edge `2.4876` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `20.9779` n `154` status `ready` deltaP `24.4453` edge `2.3583` maxDD `-54.8486`
- `market_context_high->equity_24h` score `20.6457` n `154` status `ready` deltaP `33.3491` edge `2.1394` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `14.9696` n `32` status `ready` deltaP `27.1341` edge `1.1788` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.9696` n `32` status `ready` deltaP `27.1341` edge `1.1788` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.5066` n `32` status `ready` deltaP `28.9931` edge `0.9584` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.5066` n `32` status `ready` deltaP `28.9931` edge `0.9584` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.7136` n `154` status `ready` deltaP `36.4538` edge `1.0381` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `6.6906` n `32` status `ready` deltaP `7.2409` edge `0.6937` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.6906` n `32` status `ready` deltaP `7.2409` edge `0.6937` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.5342` n `32` status `ready` deltaP `17.4543` edge `0.5784` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.5342` n `32` status `ready` deltaP `17.4543` edge `0.5784` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

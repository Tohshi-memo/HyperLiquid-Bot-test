# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T22:37:31.409690+00:00`
- Price records: `672`
- Market context records: `3425`
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

- `risk_on_high->crypto_alt_24h` score `56.3178` n `32` status `ready` deltaP `59.5486` edge `4.3113` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `56.3178` n `32` status `ready` deltaP `59.5486` edge `4.3113` maxDD `-0.8779`
- `risk_on_high->crypto_major_24h` score `56.1326` n `32` status `ready` deltaP `58.3333` edge `4.2931` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.1326` n `32` status `ready` deltaP `58.3333` edge `4.2931` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `45.5633` n `32` status `ready` deltaP `56.0764` edge `3.4231` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.5633` n `32` status `ready` deltaP `56.0764` edge `3.4231` maxDD `0.0`
- `risk_on_high->index_24h` score `23.9387` n `32` status `ready` deltaP `51.3889` edge `1.6523` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.9387` n `32` status `ready` deltaP `51.3889` edge `1.6523` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.5435` n `154` status `ready` deltaP `20.4658` edge `2.5381` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.2551` n `154` status `ready` deltaP `24.4453` edge `2.3814` maxDD `-54.8486`
- `market_context_high->equity_24h` score `20.3445` n `154` status `ready` deltaP `33.3491` edge `2.1143` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `14.6468` n `32` status `ready` deltaP `26.2195` edge `1.158` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.6468` n `32` status `ready` deltaP `26.2195` edge `1.158` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.317` n `32` status `ready` deltaP `28.9931` edge `0.9426` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.317` n `32` status `ready` deltaP `28.9931` edge `0.9426` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.746` n `154` status `ready` deltaP `36.4538` edge `1.0408` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `6.2776` n `32` status `ready` deltaP `6.1738` edge `0.6664` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.2776` n `32` status `ready` deltaP `6.1738` edge `0.6664` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.3952` n `154` status `ready` deltaP `23.8795` edge `0.8583` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.2555` n `32` status `ready` deltaP `16.2348` edge `0.5508` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

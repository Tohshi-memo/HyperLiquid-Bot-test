# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T06:07:22.802999+00:00`
- Price records: `672`
- Market context records: `3355`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13101`

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

- `risk_on_high->crypto_major_24h` score `57.9488` n `32` status `ready` deltaP `61.8056` edge `4.4213` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `57.9488` n `32` status `ready` deltaP `61.8056` edge `4.4213` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.1185` n `32` status `ready` deltaP `56.5972` edge `4.1477` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.1185` n `32` status `ready` deltaP `56.5972` edge `4.1477` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.4205` n `32` status `ready` deltaP `56.7708` edge `3.4899` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.4205` n `32` status `ready` deltaP `56.7708` edge `3.4899` maxDD `0.0`
- `risk_on_high->index_24h` score `23.2178` n `32` status `ready` deltaP `50.8681` edge `1.5957` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.2178` n `32` status `ready` deltaP `50.8681` edge `1.5957` maxDD `0.0`
- `risk_on_high->metal_24h` score `15.7554` n `32` status `ready` deltaP `34.7222` edge `1.1076` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.7554` n `32` status `ready` deltaP `34.7222` edge `1.1076` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.7151` n `32` status `ready` deltaP `29.2683` edge `1.2267` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.7151` n `32` status `ready` deltaP `29.2683` edge `1.2267` maxDD `-5.9781`
- `market_context_high->index_24h` score `12.2904` n `165` status `ready` deltaP `36.3226` edge `1.0375` maxDD `-16.1026`
- `market_context_high->crypto_alt_24h` score `12.2193` n `165` status `ready` deltaP `17.298` edge `2.4354` maxDD `-70.3986`
- `market_context_high->equity_24h` score `10.9434` n `165` status `ready` deltaP `31.9223` edge `2.0318` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.6026` n `32` status `ready` deltaP `9.0701` edge `0.7575` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.6026` n `32` status `ready` deltaP `9.0701` edge `0.7575` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6576` n `32` status `ready` deltaP `14.7104` edge `0.4843` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6576` n `32` status `ready` deltaP `14.7104` edge `0.4843` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.9699` n `32` status `ready` deltaP `5.9693` edge `0.3197` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

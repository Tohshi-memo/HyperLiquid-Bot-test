# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T04:37:25.531227+00:00`
- Price records: `672`
- Market context records: `3550`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13201`

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

- `risk_on_high->crypto_major_24h` score `52.1577` n `32` status `ready` deltaP `57.187` edge `3.9695` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `52.1577` n `32` status `ready` deltaP `57.187` edge `3.9695` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `46.9223` n `32` status `ready` deltaP `56.8403` edge `3.5464` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `46.9223` n `32` status `ready` deltaP `56.8403` edge `3.5464` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.85` n `32` status `ready` deltaP `54.4194` edge `3.3747` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.85` n `32` status `ready` deltaP `54.4194` edge `3.3747` maxDD `0.0`
- `risk_on_high->index_24h` score `25.6144` n `32` status `ready` deltaP `53.8995` edge `1.7752` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.6144` n `32` status `ready` deltaP `53.8995` edge `1.7752` maxDD `0.0`
- `market_context_high->equity_24h` score `19.206` n `156` status `ready` deltaP `31.3425` edge `2.0328` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.6902` n `32` status `ready` deltaP `37.2075` edge `1.3356` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6902` n `32` status `ready` deltaP `37.2075` edge `1.3356` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `16.7236` n `156` status `ready` deltaP `22.4915` edge `2.0168` maxDD `-54.8486`
- `risk_on_high->crypto_major_4h` score `14.2844` n `32` status `ready` deltaP `27.1341` edge `1.1217` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.2844` n `32` status `ready` deltaP `27.1341` edge `1.1217` maxDD `-5.9781`
- `market_context_high->index_24h` score `14.2297` n `156` status `ready` deltaP `38.5149` edge `1.1507` maxDD `-15.0661`
- `market_context_high->crypto_alt_24h` score `12.8352` n `156` status `ready` deltaP `17.0166` edge `1.7604` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6401` n `156` status `ready` deltaP `31.278` edge `1.225` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `5.8988` n `32` status `ready` deltaP `7.3933` edge `0.6267` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.8988` n `32` status `ready` deltaP `7.3933` edge `0.6267` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.9087` n `32` status `ready` deltaP `16.5396` edge `0.5043` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

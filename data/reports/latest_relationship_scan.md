# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T12:22:27.072793+00:00`
- Price records: `672`
- Market context records: `3583`
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

- `risk_on_high->crypto_major_24h` score `48.2551` n `32` status `ready` deltaP `51.8143` edge `3.6801` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `48.2551` n `32` status `ready` deltaP `51.8143` edge `3.6801` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `43.6682` n `32` status `ready` deltaP `51.9931` edge `3.2924` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `43.6682` n `32` status `ready` deltaP `51.9931` edge `3.2924` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `42.1701` n `32` status `ready` deltaP `51.4677` edge `3.1862` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `42.1701` n `32` status `ready` deltaP `51.4677` edge `3.1862` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.381` n `32` status `ready` deltaP `52.513` edge `1.765` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.381` n `32` status `ready` deltaP `52.513` edge `1.765` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.6313` n `32` status `ready` deltaP `36.8609` edge `1.333` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6313` n `32` status `ready` deltaP `36.8609` edge `1.333` maxDD `-0.7574`
- `market_context_high->equity_24h` score `18.0243` n `156` status `ready` deltaP `28.9162` edge `1.9505` maxDD `-40.9667`
- `market_context_high->index_24h` score `13.9964` n `156` status `ready` deltaP `37.1284` edge `1.1405` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.4045` n `32` status `ready` deltaP `25.0` edge `1.0626` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.4045` n `32` status `ready` deltaP `25.0` edge `1.0626` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `12.821` n `156` status `ready` deltaP `17.1188` edge `1.7274` maxDD `-54.8486`
- `market_context_high->crypto_alt_24h` score `8.083` n `156` status `ready` deltaP `11.644` edge `1.4002` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6018` n `156` status `ready` deltaP `30.9314` edge `1.2224` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `5.0863` n `32` status `ready` deltaP `5.4116` edge `0.5722` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.0863` n `32` status `ready` deltaP `5.4116` edge `0.5722` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5245` n `32` status `ready` deltaP `14.1006` edge `0.4713` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

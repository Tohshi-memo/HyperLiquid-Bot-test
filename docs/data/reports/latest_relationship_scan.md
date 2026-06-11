# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T15:22:38.682030+00:00`
- Price records: `672`
- Market context records: `3596`
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

- `risk_on_high->crypto_major_24h` score `46.8205` n `32` status `ready` deltaP `50.0812` edge `3.5721` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `46.8205` n `32` status `ready` deltaP `50.0812` edge `3.5721` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `43.1881` n `32` status `ready` deltaP `51.6464` edge `3.2547` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `43.1881` n `32` status `ready` deltaP `51.6464` edge `3.2547` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `40.3364` n `32` status `ready` deltaP `49.5613` edge `3.0461` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `40.3364` n `32` status `ready` deltaP `49.5613` edge `3.0461` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.243` n `32` status `ready` deltaP `52.513` edge `1.7535` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.243` n `32` status `ready` deltaP `52.513` edge `1.7535` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.2785` n `32` status `ready` deltaP `36.8609` edge `1.3036` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.2785` n `32` status `ready` deltaP `36.8609` edge `1.3036` maxDD `-0.7574`
- `market_context_high->equity_24h` score `17.5442` n `156` status `ready` deltaP `28.5695` edge `1.9128` maxDD `-40.9667`
- `market_context_high->index_24h` score `13.8584` n `156` status `ready` deltaP `37.1284` edge `1.129` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.4277` n `32` status `ready` deltaP `25.3049` edge `1.0625` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.4277` n `32` status `ready` deltaP `25.3049` edge `1.0625` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `11.3864` n `156` status `ready` deltaP `15.3857` edge `1.6194` maxDD `-54.8486`
- `market_context_high->metal_24h` score `7.3725` n `156` status `ready` deltaP `30.9314` edge `1.193` maxDD `-25.9879`
- `market_context_high->crypto_alt_24h` score `6.2493` n `156` status `ready` deltaP `9.7376` edge `1.2601` maxDD `-56.6728`
- `risk_on_high->crypto_alt_4h` score `5.2984` n `32` status `ready` deltaP `6.1738` edge `0.5848` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.2984` n `32` status `ready` deltaP `6.1738` edge `0.5848` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7361` n `32` status `ready` deltaP `15.3201` edge `0.4903` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

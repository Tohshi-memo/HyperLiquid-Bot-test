# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T12:37:41.306309+00:00`
- Price records: `672`
- Market context records: `3584`
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

- `risk_on_high->crypto_major_24h` score `48.1668` n `32` status `ready` deltaP `51.641` edge `3.6739` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `48.1668` n `32` status `ready` deltaP `51.641` edge `3.6739` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `43.6754` n `32` status `ready` deltaP `51.9931` edge `3.293` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `43.6754` n `32` status `ready` deltaP `51.9931` edge `3.293` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `42.0567` n `32` status `ready` deltaP `51.2944` edge `3.1779` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `42.0567` n `32` status `ready` deltaP `51.2944` edge `3.1779` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.4081` n `32` status `ready` deltaP `52.6863` edge `1.7661` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.4081` n `32` status `ready` deltaP `52.6863` edge `1.7661` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.6481` n `32` status `ready` deltaP `36.8609` edge `1.3344` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6481` n `32` status `ready` deltaP `36.8609` edge `1.3344` maxDD `-0.7574`
- `market_context_high->equity_24h` score `18.0315` n `156` status `ready` deltaP `28.9162` edge `1.9511` maxDD `-40.9667`
- `market_context_high->index_24h` score `14.0234` n `156` status `ready` deltaP `37.3017` edge `1.1416` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.4515` n `32` status `ready` deltaP `25.1524` edge `1.0655` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.4515` n `32` status `ready` deltaP `25.1524` edge `1.0655` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `12.7328` n `156` status `ready` deltaP `16.9455` edge `1.7212` maxDD `-54.8486`
- `market_context_high->crypto_alt_24h` score `7.9695` n `156` status `ready` deltaP `11.4707` edge `1.3919` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6128` n `156` status `ready` deltaP `30.9314` edge `1.2238` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `5.1573` n `32` status `ready` deltaP `5.564` edge `0.5771` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.1573` n `32` status `ready` deltaP `5.564` edge `0.5771` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5613` n `32` status `ready` deltaP `14.253` edge `0.475` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

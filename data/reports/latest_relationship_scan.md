# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T14:22:36.053257+00:00`
- Price records: `672`
- Market context records: `3592`
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

- `risk_on_high->crypto_major_24h` score `47.3715` n `32` status `ready` deltaP `50.7745` edge `3.6134` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `47.3715` n `32` status `ready` deltaP `50.7745` edge `3.6134` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `43.4257` n `32` status `ready` deltaP `51.6464` edge `3.2745` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `43.4257` n `32` status `ready` deltaP `51.6464` edge `3.2745` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `41.0111` n `32` status `ready` deltaP `50.2545` edge `3.0977` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `41.0111` n `32` status `ready` deltaP `50.2545` edge `3.0977` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.3661` n `32` status `ready` deltaP `52.6863` edge `1.7626` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.3661` n `32` status `ready` deltaP `52.6863` edge `1.7626` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.4765` n `32` status `ready` deltaP `36.8609` edge `1.3201` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.4765` n `32` status `ready` deltaP `36.8609` edge `1.3201` maxDD `-0.7574`
- `market_context_high->equity_24h` score `17.7818` n `156` status `ready` deltaP `28.5695` edge `1.9326` maxDD `-40.9667`
- `market_context_high->index_24h` score `13.9814` n `156` status `ready` deltaP `37.3017` edge `1.1381` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.4361` n `32` status `ready` deltaP `25.3049` edge `1.0632` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.4361` n `32` status `ready` deltaP `25.3049` edge `1.0632` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `11.9374` n `156` status `ready` deltaP `16.079` edge `1.6607` maxDD `-54.8486`
- `market_context_high->metal_24h` score `7.5012` n `156` status `ready` deltaP `30.9314` edge `1.2095` maxDD `-25.9879`
- `market_context_high->crypto_alt_24h` score `6.9239` n `156` status `ready` deltaP `10.4308` edge `1.3117` maxDD `-56.6728`
- `risk_on_high->crypto_alt_4h` score `5.2816` n `32` status `ready` deltaP `6.1738` edge `0.5834` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.2816` n `32` status `ready` deltaP `6.1738` edge `0.5834` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6906` n `32` status `ready` deltaP `15.0152` edge `0.4865` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

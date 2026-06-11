# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T09:37:38.537455+00:00`
- Price records: `672`
- Market context records: `3572`
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

- `risk_on_high->crypto_major_24h` score `49.3856` n `32` status `ready` deltaP `53.7208` edge `3.7616` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `49.3856` n `32` status `ready` deltaP `53.7208` edge `3.7616` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `44.0412` n `32` status `ready` deltaP `52.8596` edge `3.3177` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.0412` n `32` status `ready` deltaP `52.8596` edge `3.3177` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `43.615` n `32` status `ready` deltaP `53.3741` edge `3.2939` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `43.615` n `32` status `ready` deltaP `53.3741` edge `3.2939` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.4857` n `32` status `ready` deltaP `53.2062` edge `1.7691` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.4857` n `32` status `ready` deltaP `53.2062` edge `1.7691` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.6433` n `32` status `ready` deltaP `36.8609` edge `1.334` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6433` n `32` status `ready` deltaP `36.8609` edge `1.334` maxDD `-0.7574`
- `market_context_high->equity_24h` score `18.3972` n `156` status `ready` deltaP `29.7827` edge `1.9758` maxDD `-40.9667`
- `market_context_high->index_24h` score `14.101` n `156` status `ready` deltaP `37.8216` edge `1.1446` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `13.9515` n `156` status `ready` deltaP `19.0253` edge `1.8089` maxDD `-54.8486`
- `risk_on_high->crypto_major_4h` score `13.1065` n `32` status `ready` deltaP `24.6951` edge `1.0398` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.1065` n `32` status `ready` deltaP `24.6951` edge `1.0398` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `9.5279` n `156` status `ready` deltaP `13.5504` edge `1.5079` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6096` n `156` status `ready` deltaP `30.9314` edge `1.2234` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.6457` n `32` status `ready` deltaP `5.2591` edge `0.5365` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.6457` n `32` status `ready` deltaP `5.2591` edge `0.5365` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.4206` n `32` status `ready` deltaP `13.9482` edge `0.459` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

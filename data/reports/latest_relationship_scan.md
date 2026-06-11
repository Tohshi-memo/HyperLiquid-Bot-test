# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T11:22:32.078880+00:00`
- Price records: `672`
- Market context records: `3579`
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

- `risk_on_high->crypto_major_24h` score `48.6898` n `32` status `ready` deltaP `52.5076` edge `3.7117` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `48.6898` n `32` status `ready` deltaP `52.5076` edge `3.7117` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `43.8328` n `32` status `ready` deltaP `52.3397` edge `3.3038` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `43.8328` n `32` status `ready` deltaP `52.3397` edge `3.3038` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `42.7356` n `32` status `ready` deltaP `52.161` edge `3.2287` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `42.7356` n `32` status `ready` deltaP `52.161` edge `3.2287` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.405` n `32` status `ready` deltaP `52.513` edge `1.767` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.405` n `32` status `ready` deltaP `52.513` edge `1.767` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.6541` n `32` status `ready` deltaP `36.8609` edge `1.3349` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6541` n `32` status `ready` deltaP `36.8609` edge `1.3349` maxDD `-0.7574`
- `market_context_high->equity_24h` score `18.1888` n `156` status `ready` deltaP `29.2628` edge `1.9619` maxDD `-40.9667`
- `market_context_high->index_24h` score `14.0204` n `156` status `ready` deltaP `37.1284` edge `1.1425` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.2975` n `32` status `ready` deltaP `24.8476` edge `1.0547` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.2975` n `32` status `ready` deltaP `24.8476` edge `1.0547` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `13.2557` n `156` status `ready` deltaP `17.8121` edge `1.759` maxDD `-54.8486`
- `market_context_high->crypto_alt_24h` score `8.6485` n `156` status `ready` deltaP `12.3373` edge `1.4427` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6167` n `156` status `ready` deltaP `30.9314` edge `1.2243` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.8785` n `32` status `ready` deltaP `5.2591` edge `0.5559` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.8785` n `32` status `ready` deltaP `5.2591` edge `0.5559` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.4518` n `32` status `ready` deltaP `13.9482` edge `0.463` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

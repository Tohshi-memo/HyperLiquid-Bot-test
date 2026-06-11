# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T10:07:28.720356+00:00`
- Price records: `672`
- Market context records: `3574`
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

- `risk_on_high->crypto_major_24h` score `49.1839` n `32` status `ready` deltaP `53.3741` edge `3.7471` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `49.1839` n `32` status `ready` deltaP `53.3741` edge `3.7471` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `43.9534` n `32` status `ready` deltaP `52.513` edge `3.3127` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `43.9534` n `32` status `ready` deltaP `52.513` edge `3.3127` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `43.3737` n `32` status `ready` deltaP `53.0275` edge `3.2761` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `43.3737` n `32` status `ready` deltaP `53.0275` edge `3.2761` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.4484` n `32` status `ready` deltaP `52.8596` edge `1.7683` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.4484` n `32` status `ready` deltaP `52.8596` edge `1.7683` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.6325` n `32` status `ready` deltaP `36.8609` edge `1.3331` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6325` n `32` status `ready` deltaP `36.8609` edge `1.3331` maxDD `-0.7574`
- `market_context_high->equity_24h` score `18.3095` n `156` status `ready` deltaP `29.4361` edge `1.9708` maxDD `-40.9667`
- `market_context_high->index_24h` score `14.0637` n `156` status `ready` deltaP `37.475` edge `1.1438` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `13.7498` n `156` status `ready` deltaP `18.6786` edge `1.7944` maxDD `-54.8486`
- `risk_on_high->crypto_major_4h` score `13.1353` n `32` status `ready` deltaP `24.6951` edge `1.0422` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.1353` n `32` status `ready` deltaP `24.6951` edge `1.0422` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `9.2866` n `156` status `ready` deltaP `13.2038` edge `1.4901` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6026` n `156` status `ready` deltaP `30.9314` edge `1.2225` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.6985` n `32` status `ready` deltaP `5.2591` edge `0.5409` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.6985` n `32` status `ready` deltaP `5.2591` edge `0.5409` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.4175` n `32` status `ready` deltaP `13.9482` edge `0.4586` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

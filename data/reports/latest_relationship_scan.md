# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T09:22:31.682374+00:00`
- Price records: `672`
- Market context records: `3571`
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

- `risk_on_high->crypto_major_24h` score `49.4871` n `32` status `ready` deltaP `53.8941` edge `3.7689` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `49.4871` n `32` status `ready` deltaP `53.8941` edge `3.7689` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `44.0592` n `32` status `ready` deltaP `52.8596` edge `3.3192` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.0592` n `32` status `ready` deltaP `52.8596` edge `3.3192` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `43.7513` n `32` status `ready` deltaP `53.5474` edge `3.3041` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `43.7513` n `32` status `ready` deltaP `53.5474` edge `3.3041` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.4857` n `32` status `ready` deltaP `53.2062` edge `1.7691` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.4857` n `32` status `ready` deltaP `53.2062` edge `1.7691` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.6361` n `32` status `ready` deltaP `36.8609` edge `1.3334` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6361` n `32` status `ready` deltaP `36.8609` edge `1.3334` maxDD `-0.7574`
- `market_context_high->equity_24h` score `18.4152` n `156` status `ready` deltaP `29.7827` edge `1.9773` maxDD `-40.9667`
- `market_context_high->index_24h` score `14.101` n `156` status `ready` deltaP `37.8216` edge `1.1446` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `14.053` n `156` status `ready` deltaP `19.1986` edge `1.8162` maxDD `-54.8486`
- `risk_on_high->crypto_major_4h` score `13.1089` n `32` status `ready` deltaP `24.6951` edge `1.04` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.1089` n `32` status `ready` deltaP `24.6951` edge `1.04` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `9.6642` n `156` status `ready` deltaP `13.7237` edge `1.5181` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.605` n `156` status `ready` deltaP `30.9314` edge `1.2228` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.6373` n `32` status `ready` deltaP `5.2591` edge `0.5358` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.6373` n `32` status `ready` deltaP `5.2591` edge `0.5358` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.419` n `32` status `ready` deltaP `13.9482` edge `0.4588` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

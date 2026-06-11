# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T10:37:30.940870+00:00`
- Price records: `672`
- Market context records: `3576`
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

- `risk_on_high->crypto_major_24h` score `48.9846` n `32` status `ready` deltaP `53.0275` edge `3.7328` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `48.9846` n `32` status `ready` deltaP `53.0275` edge `3.7328` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `43.8856` n `32` status `ready` deltaP `52.3397` edge `3.3082` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `43.8856` n `32` status `ready` deltaP `52.3397` edge `3.3082` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `43.1264` n `32` status `ready` deltaP `52.6809` edge `3.2578` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `43.1264` n `32` status `ready` deltaP `52.6809` edge `3.2578` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.4122` n `32` status `ready` deltaP `52.513` edge `1.7676` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.4122` n `32` status `ready` deltaP `52.513` edge `1.7676` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.6373` n `32` status `ready` deltaP `36.8609` edge `1.3335` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6373` n `32` status `ready` deltaP `36.8609` edge `1.3335` maxDD `-0.7574`
- `market_context_high->equity_24h` score `18.2416` n `156` status `ready` deltaP `29.2628` edge `1.9663` maxDD `-40.9667`
- `market_context_high->index_24h` score `14.0276` n `156` status `ready` deltaP `37.1284` edge `1.1431` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `13.5505` n `156` status `ready` deltaP `18.332` edge `1.7801` maxDD `-54.8486`
- `risk_on_high->crypto_major_4h` score `13.2099` n `32` status `ready` deltaP `24.8476` edge `1.0474` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.2099` n `32` status `ready` deltaP `24.8476` edge `1.0474` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `9.0393` n `156` status `ready` deltaP `12.8572` edge `1.4718` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6057` n `156` status `ready` deltaP `30.9314` edge `1.2229` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.7705` n `32` status `ready` deltaP `5.2591` edge `0.5469` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.7705` n `32` status `ready` deltaP `5.2591` edge `0.5469` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.419` n `32` status `ready` deltaP `13.9482` edge `0.4588` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

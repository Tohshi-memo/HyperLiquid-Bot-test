# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T03:52:29.136463+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9566`

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

- `risk_on_high->commodity_24h` score `7.6215` n `54` status `ready` deltaP `39.1986` edge `0.3738` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.6215` n `54` status `ready` deltaP `39.1986` edge `0.3738` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.5709` n `117` status `ready` deltaP `19.2034` edge `0.6473` maxDD `-9.2196`
- `market_context_high->crypto_major_4h` score `6.34` n `117` status `ready` deltaP `21.4249` edge `0.5414` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.1662` n `54` status `ready` deltaP `21.4826` edge `0.4153` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.1662` n `54` status `ready` deltaP `21.4826` edge `0.4153` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6608` n `54` status `ready` deltaP `34.5303` edge `0.4526` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6608` n `54` status `ready` deltaP `34.5303` edge `0.4526` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8794` n `119` status `ready` deltaP `13.658` edge `0.172` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1384` n `119` status `ready` deltaP `4.8634` edge `0.143` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3954` n `117` status `ready` deltaP `13.9176` edge `0.0447` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2821` n `54` status `ready` deltaP `1.2531` edge `0.0277` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2821` n `54` status `ready` deltaP `1.2531` edge `0.0277` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.3064` n `119` status `ready` deltaP `7.8914` edge `0.0088` maxDD `-0.9556`
- `risk_on_high->crypto_alt_1h` score `-0.3613` n `54` status `ready` deltaP `4.5077` edge `0.0259` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3613` n `54` status `ready` deltaP `4.5077` edge `0.0259` maxDD `-5.8485`
- `risk_on_high->metal_1h` score `-0.4033` n `54` status `ready` deltaP `2.6004` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4033` n `54` status `ready` deltaP `2.6004` edge `0.0041` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.4395` n `119` status `ready` deltaP `0.1779` edge `0.0002` maxDD `-0.3742`
- `market_context_high->index_1h` score `-0.4794` n `119` status `ready` deltaP `1.7425` edge `0.0017` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T01:37:30.030585+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9422`

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

- `risk_on_high->commodity_24h` score `7.3509` n `54` status `ready` deltaP `37.6307` edge `0.3617` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.3509` n `54` status `ready` deltaP `37.6307` edge `0.3617` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.2767` n `117` status `ready` deltaP `19.051` edge `0.6238` maxDD `-9.2196`
- `market_context_high->crypto_major_4h` score `6.2656` n `117` status `ready` deltaP `21.4249` edge `0.5352` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.872` n `54` status `ready` deltaP `21.3302` edge `0.3918` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.872` n `54` status `ready` deltaP `21.3302` edge `0.3918` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6124` n `54` status `ready` deltaP `34.5303` edge `0.4464` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6124` n `54` status `ready` deltaP `34.5303` edge `0.4464` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.9751` n `117` status `ready` deltaP `14.7641` edge `0.1726` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.2838` n `117` status `ready` deltaP `5.8115` edge `0.1488` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5348` n `117` status `ready` deltaP `14.9847` edge `0.0492` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2835` n `117` status `ready` deltaP `8.1632` edge `0.0089` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.3219` n `54` status `ready` deltaP `1.2531` edge `0.0226` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3219` n `54` status `ready` deltaP `1.2531` edge `0.0226` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.372` n `117` status `ready` deltaP `0.9471` edge `0.0007` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.3986` n `54` status `ready` deltaP `2.7501` edge `0.0037` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3986` n `54` status `ready` deltaP `2.7501` edge `0.0037` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.4334` n `54` status `ready` deltaP `2.5915` edge `0.0317` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.4334` n `54` status `ready` deltaP `2.5915` edge `0.0317` maxDD `-1.6961`
- `risk_on_high->crypto_alt_1h` score `-0.444` n `54` status `ready` deltaP `4.5077` edge `0.0153` maxDD `-5.8485`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

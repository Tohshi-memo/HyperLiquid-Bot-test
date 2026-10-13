# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T16:07:44.887966+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9582`

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

- `market_context_high->crypto_alt_4h` score `8.0598` n `117` status `ready` deltaP `20.2705` edge `0.6814` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `7.0117` n `117` status `ready` deltaP `24.0163` edge `0.5801` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.6487` n `54` status `ready` deltaP `22.5497` edge `0.4485` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.6487` n `54` status `ready` deltaP `22.5497` edge `0.4485` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `6.2377` n `48` status `ready` deltaP `32.0557` edge `0.3061` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2377` n `48` status `ready` deltaP `32.0557` edge `0.3061` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.0974` n `54` status `ready` deltaP `37.1217` edge `0.4913` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.0974` n `54` status `ready` deltaP `37.1217` edge `0.4913` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.191` n `117` status `ready` deltaP `-3.467` edge `0.437` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.1632` n `117` status `ready` deltaP `15.2132` edge `0.1856` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.605` n `117` status `ready` deltaP `8.2067` edge `0.1596` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2752` n `117` status `ready` deltaP `13.7652` edge `0.0357` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1131` n `54` status `ready` deltaP `3.6483` edge `0.0334` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1131` n `54` status `ready` deltaP `3.6483` edge `0.0334` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3167` n `117` status `ready` deltaP `1.3976` edge `0.0023` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.3271` n `54` status `ready` deltaP `4.9568` edge `0.0276` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.3271` n `54` status `ready` deltaP `4.9568` edge `0.0276` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.3494` n `117` status `ready` deltaP `7.5644` edge `0.0074` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4415` n `54` status `ready` deltaP `2.1513` edge `0.0022` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4415` n `54` status `ready` deltaP `2.1513` edge `0.0022` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

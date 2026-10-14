# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T17:22:30.276498+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9370`

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

- `market_context_high->crypto_alt_4h` score `7.0881` n `117` status `ready` deltaP `18.5937` edge `0.6116` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.3637` n `54` status `ready` deltaP `32.5217` edge `0.3135` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3637` n `54` status `ready` deltaP `32.5217` edge `0.3135` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.1992` n `117` status `ready` deltaP `21.12` edge `0.5317` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.677` n `54` status `ready` deltaP `20.8729` edge `0.3787` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.677` n `54` status `ready` deltaP `20.8729` edge `0.3787` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.5692` n `54` status `ready` deltaP `34.2254` edge `0.4429` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.5692` n `54` status `ready` deltaP `34.2254` edge `0.4429` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7327` n `117` status `ready` deltaP `13.4168` edge `0.1617` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2406` n `117` status `ready` deltaP `5.8115` edge `0.1452` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3546` n `117` status `ready` deltaP `13.9176` edge `0.0413` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2583` n `117` status `ready` deltaP `8.4626` edge `0.009` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.35` n `54` status `ready` deltaP `1.2531` edge `0.019` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.35` n `54` status `ready` deltaP `1.2531` edge `0.019` maxDD `-3.7781`
- `risk_on_high->metal_1h` score `-0.3823` n `54` status `ready` deltaP `3.0495` edge `0.0038` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3823` n `54` status `ready` deltaP `3.0495` edge `0.0038` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.3912` n `117` status `ready` deltaP `0.4967` edge `0.0021` maxDD `-0.3742`
- `risk_on_high->metal_4h` score `-0.5505` n `54` status `ready` deltaP `1.5244` edge `0.0238` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.5505` n `54` status `ready` deltaP `1.5244` edge `0.0238` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.5961` n `117` status `ready` deltaP `-0.1271` edge `-0.0008` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

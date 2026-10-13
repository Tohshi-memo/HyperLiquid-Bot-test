# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T23:07:30.813141+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9318`

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

- `market_context_high->crypto_alt_4h` score `7.5353` n `117` status `ready` deltaP `17.9136` edge `0.6534` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.7271` n `117` status `ready` deltaP `22.4096` edge `0.5671` maxDD `-7.4722`
- `risk_on_high->commodity_24h` score `6.1276` n `48` status `ready` deltaP `32.0` edge `0.2973` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1276` n `48` status `ready` deltaP `32.0` edge `0.2973` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.1242` n `54` status `ready` deltaP `20.1928` edge `0.4205` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.1242` n `54` status `ready` deltaP `20.1928` edge `0.4205` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.9124` n `54` status `ready` deltaP `35.515` edge `0.4783` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.9124` n `54` status `ready` deltaP `35.515` edge `0.4783` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.2043` n `117` status `ready` deltaP `-3.9457` edge `0.4413` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.0147` n `117` status `ready` deltaP `14.6909` edge `0.1767` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5173` n `117` status `ready` deltaP `7.8303` edge `0.1548` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3926` n `117` status `ready` deltaP `14.7524` edge `0.0389` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1701` n `54` status `ready` deltaP `3.2719` edge `0.0286` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1701` n `54` status `ready` deltaP `3.2719` edge `0.0286` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.304` n `117` status `ready` deltaP `8.0871` edge `0.0077` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.3355` n `117` status `ready` deltaP `1.1777` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.412` n `54` status `ready` deltaP `2.674` edge `0.0025` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.412` n `54` status `ready` deltaP `2.674` edge `0.0025` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.4237` n `54` status `ready` deltaP `4.4345` edge `0.0187` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.4237` n `54` status `ready` deltaP `4.4345` edge `0.0187` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

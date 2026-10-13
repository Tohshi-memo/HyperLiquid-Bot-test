# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T21:37:38.160103+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9402`

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

- `market_context_high->crypto_alt_4h` score `7.6495` n `117` status `ready` deltaP `18.4412` edge `0.6594` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.8135` n `117` status `ready` deltaP `22.9493` edge `0.5707` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.2384` n `54` status `ready` deltaP `20.7204` edge `0.4265` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.2384` n `54` status `ready` deltaP `20.7204` edge `0.4265` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `6.1849` n `48` status `ready` deltaP `32.0557` edge `0.3017` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1849` n `48` status `ready` deltaP `32.0557` edge `0.3017` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.9686` n `54` status `ready` deltaP `36.0547` edge `0.4819` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.9686` n `54` status `ready` deltaP `36.0547` edge `0.4819` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.4487` n `117` status `ready` deltaP `-3.7719` edge `0.4605` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.9918` n `117` status `ready` deltaP `14.4647` edge `0.1763` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5127` n `117` status `ready` deltaP `7.7576` edge `0.1549` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4184` n `117` status `ready` deltaP `14.9847` edge `0.0395` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1731` n `54` status `ready` deltaP `3.1992` edge `0.0287` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1731` n `54` status `ready` deltaP `3.1992` edge `0.0287` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2927` n `117` status `ready` deltaP `1.6979` edge `0.0023` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.3218` n `117` status `ready` deltaP `7.8638` edge `0.0077` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4236` n `54` status `ready` deltaP `2.4507` edge `0.0025` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4236` n `54` status `ready` deltaP `2.4507` edge `0.0025` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.4386` n `54` status `ready` deltaP `4.2083` edge `0.0183` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.4386` n `54` status `ready` deltaP `4.2083` edge `0.0183` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

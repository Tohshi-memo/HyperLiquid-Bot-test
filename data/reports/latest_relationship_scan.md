# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T22:07:31.463455+00:00`
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

- `market_context_high->crypto_alt_4h` score `7.6145` n `117` status `ready` deltaP `18.2888` edge `0.6575` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.7869` n `117` status `ready` deltaP `22.7968` edge `0.5695` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.2034` n `54` status `ready` deltaP `20.568` edge `0.4246` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.2034` n `54` status `ready` deltaP `20.568` edge `0.4246` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `6.1669` n `48` status `ready` deltaP `32.0557` edge `0.3002` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1669` n `48` status `ready` deltaP `32.0557` edge `0.3002` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.9513` n `54` status `ready` deltaP `35.9022` edge `0.4807` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.9513` n `54` status `ready` deltaP `35.9022` edge `0.4807` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.2697` n `117` status `ready` deltaP `-3.9243` edge `0.4466` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.9894` n `117` status `ready` deltaP `14.4647` edge `0.1761` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5091` n `117` status `ready` deltaP `7.7576` edge `0.1546` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4026` n `117` status `ready` deltaP `14.8322` edge `0.0392` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1755` n `54` status `ready` deltaP `3.1992` edge `0.0284` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1755` n `54` status `ready` deltaP `3.1992` edge `0.0284` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2927` n `117` status `ready` deltaP `1.6979` edge `0.0023` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.3099` n `117` status `ready` deltaP `8.0135` edge `0.0077` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4158` n `54` status `ready` deltaP `2.6004` edge `0.0025` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4158` n `54` status `ready` deltaP `2.6004` edge `0.0025` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.4401` n `54` status `ready` deltaP `4.2083` edge `0.0181` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.4401` n `54` status `ready` deltaP `4.2083` edge `0.0181` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

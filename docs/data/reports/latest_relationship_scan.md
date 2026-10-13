# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T22:22:26.425092+00:00`
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

- `market_context_high->crypto_alt_4h` score `7.5927` n `117` status `ready` deltaP `18.1364` edge `0.6567` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.7675` n `117` status `ready` deltaP `22.6444` edge `0.5689` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.1816` n `54` status `ready` deltaP `20.4156` edge `0.4238` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.1816` n `54` status `ready` deltaP `20.4156` edge `0.4238` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `6.1597` n `48` status `ready` deltaP `32.0557` edge `0.2996` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1597` n `48` status `ready` deltaP `32.0557` edge `0.2996` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.9387` n `54` status `ready` deltaP `35.7498` edge `0.4801` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.9387` n `54` status `ready` deltaP `35.7498` edge `0.4801` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.2193` n `117` status `ready` deltaP `-3.9243` edge `0.4424` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.9906` n `117` status `ready` deltaP `14.4647` edge `0.1762` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5103` n `117` status `ready` deltaP `7.7576` edge `0.1547` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4014` n `117` status `ready` deltaP `14.8322` edge `0.0391` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1747` n `54` status `ready` deltaP `3.1992` edge `0.0285` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1747` n `54` status `ready` deltaP `3.1992` edge `0.0285` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3047` n `117` status `ready` deltaP `1.5477` edge `0.0023` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.3099` n `117` status `ready` deltaP `8.0135` edge `0.0077` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4158` n `54` status `ready` deltaP `2.6004` edge `0.0025` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4158` n `54` status `ready` deltaP `2.6004` edge `0.0025` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.4394` n `54` status `ready` deltaP `4.2083` edge `0.0182` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.4394` n `54` status `ready` deltaP `4.2083` edge `0.0182` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

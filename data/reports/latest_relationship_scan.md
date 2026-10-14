# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T20:37:28.208263+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9338`

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

- `market_context_high->crypto_alt_4h` score `7.2047` n `117` status `ready` deltaP `19.051` edge `0.6178` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `6.7597` n `54` status `ready` deltaP `34.2609` edge `0.3349` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.7597` n `54` status `ready` deltaP `34.2609` edge `0.3349` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.2448` n `117` status `ready` deltaP `21.12` edge `0.5355` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.8` n `54` status `ready` deltaP `21.3302` edge `0.3858` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.8` n `54` status `ready` deltaP `21.3302` edge `0.3858` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.5989` n `54` status `ready` deltaP `34.2254` edge `0.4467` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.5989` n `54` status `ready` deltaP `34.2254` edge `0.4467` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7916` n `117` status `ready` deltaP `13.7162` edge `0.1643` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.2191` n `117` status `ready` deltaP `5.5121` edge `0.1454` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4298` n `117` status `ready` deltaP `14.5273` edge `0.0435` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2763` n `117` status `ready` deltaP `8.3129` edge `0.0085` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.3431` n `117` status `ready` deltaP `1.0973` edge `0.0021` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.364` n `54` status `ready` deltaP `0.9537` edge `0.0192` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.364` n `54` status `ready` deltaP `0.9537` edge `0.0192` maxDD `-3.7781`
- `risk_on_high->metal_1h` score `-0.394` n `54` status `ready` deltaP `2.8998` edge `0.0033` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.394` n `54` status `ready` deltaP `2.8998` edge `0.0033` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.5016` n `54` status `ready` deltaP `2.1341` edge `0.026` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.5016` n `54` status `ready` deltaP `2.1341` edge `0.026` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.561` n `117` status `ready` deltaP `0.4735` edge `-0.0003` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

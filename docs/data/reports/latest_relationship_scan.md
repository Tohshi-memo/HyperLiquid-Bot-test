# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T04:37:28.467474+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9586`

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

- `market_context_high->crypto_alt_4h` score `7.7355` n `117` status `ready` deltaP `19.3559` edge `0.66` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `7.6981` n `54` status `ready` deltaP `39.7213` edge `0.3767` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.6981` n `54` status `ready` deltaP `39.7213` edge `0.3767` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.4108` n `117` status `ready` deltaP `21.4249` edge `0.5473` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.3308` n `54` status `ready` deltaP `21.6351` edge `0.428` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.3308` n `54` status `ready` deltaP `21.6351` edge `0.428` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.7068` n `54` status `ready` deltaP `34.5303` edge `0.4585` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.7068` n `54` status `ready` deltaP `34.5303` edge `0.4585` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7103` n `120` status `ready` deltaP `12.9691` edge `0.1625` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9826` n `120` status `ready` deltaP `4.1018` edge `0.1351` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3712` n `117` status `ready` deltaP `13.7652` edge `0.0437` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3281` n `54` status `ready` deltaP `0.9537` edge `0.0238` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3281` n `54` status `ready` deltaP `0.9537` edge `0.0238` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.3553` n `120` status `ready` deltaP `7.4152` edge `0.0079` maxDD `-0.9556`
- `risk_on_high->crypto_alt_1h` score `-0.3972` n `54` status `ready` deltaP `4.358` edge `0.0223` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3972` n `54` status `ready` deltaP `4.358` edge `0.0223` maxDD `-5.8485`
- `risk_on_high->metal_1h` score `-0.4017` n `54` status `ready` deltaP `2.6004` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4017` n `54` status `ready` deltaP `2.6004` edge `0.0043` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.4669` n `120` status `ready` deltaP `-0.1202` edge `-0.0001` maxDD `-0.3742`
- `market_context_high->index_1h` score `-0.4935` n `120` status `ready` deltaP `1.4865` edge `0.0016` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

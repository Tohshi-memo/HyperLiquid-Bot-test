# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T04:52:25.583763+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9608`

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

- `market_context_high->crypto_alt_4h` score `7.7933` n `117` status `ready` deltaP `19.5083` edge `0.6638` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `7.7216` n `54` status `ready` deltaP `39.8955` edge `0.3775` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.7216` n `54` status `ready` deltaP `39.8955` edge `0.3775` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.4422` n `117` status `ready` deltaP `21.5773` edge `0.5489` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.3886` n `54` status `ready` deltaP `21.7875` edge `0.4318` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.3886` n `54` status `ready` deltaP `21.7875` edge `0.4318` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.7272` n `54` status `ready` deltaP `34.6827` edge `0.4601` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.7272` n `54` status `ready` deltaP `34.6827` edge `0.4601` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7043` n `120` status `ready` deltaP `12.9691` edge `0.162` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.973` n `120` status `ready` deltaP `4.1018` edge `0.1343` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3688` n `117` status `ready` deltaP `13.7652` edge `0.0435` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3344` n `54` status `ready` deltaP `0.9537` edge `0.023` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3344` n `54` status `ready` deltaP `0.9537` edge `0.023` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.3685` n `120` status `ready` deltaP `7.2655` edge `0.0078` maxDD `-0.9556`
- `risk_on_high->crypto_alt_1h` score `-0.4011` n `54` status `ready` deltaP `4.358` edge `0.0218` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.4011` n `54` status `ready` deltaP `4.358` edge `0.0218` maxDD `-5.8485`
- `risk_on_high->metal_1h` score `-0.4103` n `54` status `ready` deltaP `2.4507` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4103` n `54` status `ready` deltaP `2.4507` edge `0.0042` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.4549` n `120` status `ready` deltaP `0.03` edge `-0.0001` maxDD `-0.3742`
- `market_context_high->index_1h` score `-0.495` n `120` status `ready` deltaP `1.4865` edge `0.0014` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

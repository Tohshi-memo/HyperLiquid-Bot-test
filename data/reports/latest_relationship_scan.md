# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T04:07:27.028753+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9566`

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

- `market_context_high->crypto_alt_4h` score `7.6479` n `117` status `ready` deltaP `19.3559` edge `0.6527` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `7.6474` n `54` status `ready` deltaP `39.3728` edge `0.3748` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.6474` n `54` status `ready` deltaP `39.3728` edge `0.3748` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.3736` n `117` status `ready` deltaP `21.4249` edge `0.5442` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.2432` n `54` status `ready` deltaP `21.6351` edge `0.4207` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.2432` n `54` status `ready` deltaP `21.6351` edge `0.4207` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6826` n `54` status `ready` deltaP `34.5303` edge `0.4554` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6826` n `54` status `ready` deltaP `34.5303` edge `0.4554` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.763` n `120` status `ready` deltaP `13.1188` edge `0.1659` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0486` n `120` status `ready` deltaP `4.4012` edge `0.1386` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3784` n `117` status `ready` deltaP `13.7652` edge `0.0443` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2853` n `54` status `ready` deltaP `1.2531` edge `0.0273` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2853` n `54` status `ready` deltaP `1.2531` edge `0.0273` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.3565` n `120` status `ready` deltaP `7.4152` edge `0.0078` maxDD `-0.9556`
- `risk_on_high->crypto_alt_1h` score `-0.3629` n `54` status `ready` deltaP `4.5077` edge `0.0257` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3629` n `54` status `ready` deltaP `4.5077` edge `0.0257` maxDD `-5.8485`
- `risk_on_high->metal_1h` score `-0.4025` n `54` status `ready` deltaP `2.6004` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4025` n `54` status `ready` deltaP `2.6004` edge `0.0042` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.4802` n `120` status `ready` deltaP `-0.2703` edge `-0.0002` maxDD `-0.3742`
- `market_context_high->index_1h` score `-0.4927` n `120` status `ready` deltaP `1.4865` edge `0.0017` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

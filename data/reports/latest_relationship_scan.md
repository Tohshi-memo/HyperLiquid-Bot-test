# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T19:52:33.330559+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9671`

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

- `market_context_high->crypto_alt_4h` score `7.1879` n `117` status `ready` deltaP `19.051` edge `0.6164` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `6.6615` n `54` status `ready` deltaP `33.7391` edge `0.3302` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.6615` n `54` status `ready` deltaP `33.7391` edge `0.3302` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.252` n `117` status `ready` deltaP `21.12` edge `0.5361` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.7832` n `54` status `ready` deltaP `21.3302` edge `0.3844` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.7832` n `54` status `ready` deltaP `21.3302` edge `0.3844` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6036` n `54` status `ready` deltaP `34.2254` edge `0.4473` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6036` n `54` status `ready` deltaP `34.2254` edge `0.4473` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7952` n `117` status `ready` deltaP `13.7162` edge `0.1646` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.2502` n `117` status `ready` deltaP `5.8115` edge `0.146` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3896` n `117` status `ready` deltaP `14.07` edge `0.0432` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2907` n `117` status `ready` deltaP `8.1632` edge `0.0083` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.3431` n `117` status `ready` deltaP `1.0973` edge `0.0021` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.3438` n `54` status `ready` deltaP `1.2531` edge `0.0198` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3438` n `54` status `ready` deltaP `1.2531` edge `0.0198` maxDD `-3.7781`
- `risk_on_high->metal_1h` score `-0.4033` n `54` status `ready` deltaP `2.7501` edge `0.0031` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4033` n `54` status `ready` deltaP `2.7501` edge `0.0031` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.5277` n `54` status `ready` deltaP `1.6768` edge `0.0257` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.5277` n `54` status `ready` deltaP `1.6768` edge `0.0257` maxDD `-1.6961`
- `risk_on_high->crypto_alt_1h` score `-0.5609` n `54` status `ready` deltaP `3.4598` edge `0.0073` maxDD `-5.8485`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

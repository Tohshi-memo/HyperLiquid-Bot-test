# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T03:37:27.076646+00:00`
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

- `risk_on_high->commodity_24h` score `7.5932` n `54` status `ready` deltaP `39.0244` edge `0.3726` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.5932` n `54` status `ready` deltaP `39.0244` edge `0.3726` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.4951` n `117` status `ready` deltaP `19.051` edge `0.642` maxDD `-9.2196`
- `market_context_high->crypto_major_4h` score `6.3088` n `117` status `ready` deltaP `21.4249` edge `0.5388` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.0904` n `54` status `ready` deltaP `21.3302` edge `0.41` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.0904` n `54` status `ready` deltaP `21.3302` edge `0.41` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6405` n `54` status `ready` deltaP `34.5303` edge `0.45` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6405` n `54` status `ready` deltaP `34.5303` edge `0.45` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `2.0024` n `118` status `ready` deltaP `14.2063` edge `0.1786` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.2432` n `118` status `ready` deltaP `5.3334` edge `0.1486` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4136` n `117` status `ready` deltaP `14.07` edge `0.0452` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2593` n `118` status `ready` deltaP `8.3756` edge `0.0095` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.2782` n `54` status `ready` deltaP `1.2531` edge `0.0282` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2782` n `54` status `ready` deltaP `1.2531` edge `0.0282` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3582` n `54` status `ready` deltaP `4.5077` edge `0.0263` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3582` n `54` status `ready` deltaP `4.5077` edge `0.0263` maxDD `-5.8485`
- `market_context_high->fx_1h` score `-0.3982` n `118` status `ready` deltaP `0.6337` edge `0.0006` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.4041` n `54` status `ready` deltaP `2.6004` edge `0.004` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4041` n `54` status `ready` deltaP `2.6004` edge `0.004` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.4556` n `118` status `ready` deltaP `2.1555` edge `0.002` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

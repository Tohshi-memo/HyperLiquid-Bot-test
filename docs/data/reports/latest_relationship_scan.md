# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T10:37:35.677060+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8638`

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

- `risk_on_high->commodity_24h` score `8.1235` n `54` status `ready` deltaP `43.554` edge `0.3866` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.1235` n `54` status `ready` deltaP `43.554` edge `0.3866` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.9451` n `126` status `ready` deltaP `18.1063` edge `0.5495` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.6766` n `126` status `ready` deltaP `21.1817` edge `0.464` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.8406` n `54` status `ready` deltaP `19.9582` edge `0.315` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.8406` n `54` status `ready` deltaP `19.9582` edge `0.315` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.933` n `54` status `ready` deltaP `33.6156` edge `0.3654` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.933` n `54` status `ready` deltaP `33.6156` edge `0.3654` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.4039` n `127` status `ready` deltaP `13.0699` edge `0.1363` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.8953` n `127` status `ready` deltaP `6.0552` edge `0.1148` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2294` n `126` status `ready` deltaP `11.6628` edge `0.0459` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2064` n `127` status `ready` deltaP `9.2767` edge `0.0079` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3613` n `54` status `ready` deltaP `3.6483` edge `0.0025` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3613` n `54` status `ready` deltaP `3.6483` edge `0.0025` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.4299` n `127` status `ready` deltaP `3.1366` edge `-0.0012` maxDD `-1.3195`
- `market_context_high->fx_1h` score `-0.4346` n `127` status `ready` deltaP `-0.3204` edge `-0.0018` maxDD `-0.4757`
- `risk_on_high->index_1h` score `-0.4404` n `54` status `ready` deltaP `-2.3023` edge `-0.0027` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.4404` n `54` status `ready` deltaP `-2.3023` edge `-0.0027` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.4647` n `54` status `ready` deltaP `2.0016` edge `-0.0007` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4647` n `54` status `ready` deltaP `2.0016` edge `-0.0007` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

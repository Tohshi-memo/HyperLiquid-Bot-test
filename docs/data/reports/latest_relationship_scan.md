# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T17:07:32.536630+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7164`

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

- `risk_on_high->commodity_24h` score `7.9033` n `54` status `ready` deltaP `41.9861` edge `0.3787` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9033` n `54` status `ready` deltaP `41.9861` edge `0.3787` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.2834` n `127` status `ready` deltaP `19.2145` edge `0.5703` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.7687` n `127` status `ready` deltaP `20.9681` edge `0.4731` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.3024` n `54` status `ready` deltaP `21.6351` edge `0.3423` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.3024` n `54` status `ready` deltaP `21.6351` edge `0.3423` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.0013` n `54` status `ready` deltaP `33.1583` edge `0.3772` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.0013` n `54` status `ready` deltaP `33.1583` edge `0.3772` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6102` n `127` status `ready` deltaP `13.8184` edge `0.1485` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0093` n `127` status `ready` deltaP `6.3546` edge `0.1223` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5077` n `127` status `ready` deltaP `14.5417` edge `0.0499` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.1381` n `127` status `ready` deltaP `9.8755` edge `0.0096` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3169` n `54` status `ready` deltaP `4.2471` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3169` n `54` status `ready` deltaP `4.2471` edge `0.0042` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.3907` n `54` status `ready` deltaP `2.301` edge `0.0068` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3907` n `54` status `ready` deltaP `2.301` edge `0.0068` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.3987` n `127` status `ready` deltaP `3.4369` edge `0.0008` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.4092` n `54` status `ready` deltaP `-2.002` edge `-0.0007` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.4092` n `54` status `ready` deltaP `-2.002` edge `-0.0007` maxDD `-0.7394`
- `market_context_high->fx_1h` score `-0.4518` n `127` status `ready` deltaP `-0.6207` edge `-0.002` maxDD `-0.4757`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

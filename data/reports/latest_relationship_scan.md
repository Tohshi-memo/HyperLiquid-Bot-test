# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T17:37:30.979526+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7180`

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

- `risk_on_high->commodity_24h` score `7.8514` n `54` status `ready` deltaP `41.6376` edge `0.3767` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.8514` n `54` status `ready` deltaP `41.6376` edge `0.3767` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.3614` n `127` status `ready` deltaP `19.2145` edge `0.5768` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.8203` n `127` status `ready` deltaP `20.9681` edge `0.4774` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.3804` n `54` status `ready` deltaP `21.6351` edge `0.3488` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.3804` n `54` status `ready` deltaP `21.6351` edge `0.3488` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.0348` n `54` status `ready` deltaP `33.1583` edge `0.3815` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.0348` n `54` status `ready` deltaP `33.1583` edge `0.3815` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6678` n `127` status `ready` deltaP `13.9681` edge `0.1523` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.05` n `127` status `ready` deltaP `6.5043` edge `0.1247` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5393` n `127` status `ready` deltaP `14.8466` edge `0.0505` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.1105` n `127` status `ready` deltaP `10.1749` edge `0.0099` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.299` n `54` status `ready` deltaP `4.5465` edge `0.0045` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.299` n `54` status `ready` deltaP `4.5465` edge `0.0045` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.3642` n `54` status `ready` deltaP `2.4507` edge `0.0092` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3642` n `54` status `ready` deltaP `2.4507` edge `0.0092` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.387` n `127` status `ready` deltaP `3.5871` edge `0.0013` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.3974` n `54` status `ready` deltaP `-1.8518` edge `-0.0002` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.3974` n `54` status `ready` deltaP `-1.8518` edge `-0.0002` maxDD `-0.7394`
- `market_context_high->fx_1h` score `-0.444` n `127` status `ready` deltaP `-0.4706` edge `-0.002` maxDD `-0.4757`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

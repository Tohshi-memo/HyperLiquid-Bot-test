# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T17:38:29.863817+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9208`

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

- `risk_on_high->commodity_24h` score `7.9457` n `54` status `ready` deltaP `41.8118` edge `0.3834` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9457` n `54` status `ready` deltaP `41.8118` edge `0.3834` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.9169` n `122` status `ready` deltaP `17.3481` edge `0.5522` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.4211` n `122` status `ready` deltaP `18.9474` edge `0.4576` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.7232` n `54` status `ready` deltaP `20.1107` edge `0.3042` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.7232` n `54` status `ready` deltaP `20.1107` edge `0.3042` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.7339` n `54` status `ready` deltaP `32.3961` edge `0.348` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.7339` n `54` status `ready` deltaP `32.3961` edge `0.348` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.0915` n `122` status `ready` deltaP `12.2092` edge `0.116` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.589` n `122` status `ready` deltaP `4.4616` edge `0.0999` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0351` n `122` status `ready` deltaP `10.3134` edge `0.0387` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2592` n `115` status `ready` deltaP `13.9857` edge `0.1517` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3868` n `122` status `ready` deltaP `-1.3637` edge `-0.0021` maxDD `-0.4047`
- `risk_on_high->metal_1h` score `-0.5061` n `54` status `ready` deltaP `1.1034` edge `0.0009` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5061` n `54` status `ready` deltaP `1.1034` edge `0.0009` maxDD `-0.8513`
- `market_context_high->metal_1h` score `-0.5246` n `122` status `ready` deltaP `5.8089` edge `0.0045` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.5607` n `122` status `ready` deltaP `0.7631` edge `-0.0022` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.5911` n `54` status `ready` deltaP `-5.005` edge `-0.004` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.5911` n `54` status `ready` deltaP `-5.005` edge `-0.004` maxDD `-0.7394`
- `market_context_high->commodity_1h` score `-0.7019` n `122` status `ready` deltaP `1.9273` edge `-0.0211` maxDD `-2.8718`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T14:07:32.887136+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8300`

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

- `risk_on_high->commodity_24h` score `8.0039` n `54` status `ready` deltaP `42.5087` edge `0.3836` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.0039` n `54` status `ready` deltaP `42.5087` edge `0.3836` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.8932` n `127` status `ready` deltaP `18.1474` edge `0.5449` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.5478` n `127` status `ready` deltaP `20.8157` edge `0.4557` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.9122` n `54` status `ready` deltaP `20.568` edge `0.3169` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.9122` n `54` status `ready` deltaP `20.568` edge `0.3169` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.8577` n `54` status `ready` deltaP `33.0059` edge `0.3598` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.8577` n `54` status `ready` deltaP `33.0059` edge `0.3598` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.4039` n `127` status `ready` deltaP `12.9202` edge `0.1373` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9313` n `127` status `ready` deltaP `6.2049` edge `0.1168` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4082` n `127` status `ready` deltaP `13.6271` edge `0.0477` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.1717` n `127` status `ready` deltaP `9.5761` edge `0.0088` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3387` n `54` status `ready` deltaP `3.9477` edge `0.0034` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3387` n `54` status `ready` deltaP `3.9477` edge `0.0034` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.4414` n `54` status `ready` deltaP `2.1513` edge `0.0013` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4414` n `54` status `ready` deltaP `2.1513` edge `0.0013` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.4424` n `127` status `ready` deltaP `2.8363` edge `-0.0008` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.4529` n `54` status `ready` deltaP `-2.6026` edge `-0.0023` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.4529` n `54` status `ready` deltaP `-2.6026` edge `-0.0023` maxDD `-0.7394`
- `market_context_high->fx_1h` score `-0.4603` n `127` status `ready` deltaP `-0.7709` edge `-0.0021` maxDD `-0.4757`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

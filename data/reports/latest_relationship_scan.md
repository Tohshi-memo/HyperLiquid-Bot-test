# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T23:07:33.649323+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7032`

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

- `market_context_high->crypto_alt_4h` score `8.1593` n `127` status `ready` deltaP `21.0437` edge `0.6311` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.3913` n `54` status `ready` deltaP `38.676` edge `0.3581` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.3913` n `54` status `ready` deltaP `38.676` edge `0.3581` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.1783` n `54` status `ready` deltaP `23.4643` edge `0.4031` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.1783` n `54` status `ready` deltaP `23.4643` edge `0.4031` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.1555` n `127` status `ready` deltaP `22.1876` edge `0.4972` maxDD `-5.906`
- `risk_on_high->crypto_major_4h` score `4.2527` n `54` status `ready` deltaP `34.3778` edge `0.4013` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2527` n `54` status `ready` deltaP `34.3778` edge `0.4013` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7037` n `127` status `ready` deltaP `14.1178` edge `0.1543` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9505` n `127` status `ready` deltaP `5.7558` edge `0.1214` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.6327` n `127` status `ready` deltaP `15.6088` edge `0.0532` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.1117` n `127` status `ready` deltaP `10.1749` edge `0.0098` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.2998` n `54` status `ready` deltaP `4.5465` edge `0.0044` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.2998` n `54` status `ready` deltaP `4.5465` edge `0.0044` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.3159` n `127` status `ready` deltaP `4.7883` edge `0.0024` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.3264` n `54` status `ready` deltaP `-0.6506` edge `0.0009` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.3264` n `54` status `ready` deltaP `-0.6506` edge `0.0009` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.4288` n `54` status `ready` deltaP `1.7022` edge `0.0059` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4288` n `54` status `ready` deltaP `1.7022` edge `0.0059` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.4361` n `127` status `ready` deltaP `-0.3204` edge `-0.002` maxDD `-0.4757`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

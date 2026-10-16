# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T22:37:25.273585+00:00`
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

- `market_context_high->crypto_alt_4h` score `8.1581` n `127` status `ready` deltaP `21.0437` edge `0.631` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.4057` n `54` status `ready` deltaP `38.676` edge `0.3593` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.4057` n `54` status `ready` deltaP `38.676` edge `0.3593` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.1819` n `127` status `ready` deltaP `22.1876` edge `0.4994` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `6.1771` n `54` status `ready` deltaP `23.4643` edge `0.403` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.1771` n `54` status `ready` deltaP `23.4643` edge `0.403` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.2699` n `54` status `ready` deltaP `34.3778` edge `0.4035` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2699` n `54` status `ready` deltaP `34.3778` edge `0.4035` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6965` n `127` status `ready` deltaP `14.1178` edge `0.1537` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9661` n `127` status `ready` deltaP `5.9055` edge `0.1217` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.6351` n `127` status `ready` deltaP `15.6088` edge `0.0534` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.1369` n `127` status `ready` deltaP `9.8755` edge `0.0097` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3161` n `54` status `ready` deltaP `4.2471` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3161` n `54` status `ready` deltaP `4.2471` edge `0.0043` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.3238` n `127` status `ready` deltaP `4.6381` edge `0.0024` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.3342` n `54` status `ready` deltaP `-0.8008` edge `0.0009` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.3342` n `54` status `ready` deltaP `-0.8008` edge `0.0009` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.4187` n `54` status `ready` deltaP `1.8519` edge `0.0062` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4187` n `54` status `ready` deltaP `1.8519` edge `0.0062` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.444` n `127` status `ready` deltaP `-0.4706` edge `-0.002` maxDD `-0.4757`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

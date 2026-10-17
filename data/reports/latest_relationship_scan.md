# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T03:07:28.871384+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7056`

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

- `market_context_high->crypto_alt_4h` score `8.3347` n `127` status `ready` deltaP `22.1108` edge `0.6386` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.2269` n `54` status `ready` deltaP `38.676` edge `0.3444` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.2269` n `54` status `ready` deltaP `38.676` edge `0.3444` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.3537` n `54` status `ready` deltaP `24.5314` edge `0.4106` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.3537` n `54` status `ready` deltaP `24.5314` edge `0.4106` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.3133` n `127` status `ready` deltaP `23.5596` edge `0.5012` maxDD `-5.906`
- `risk_on_high->crypto_major_4h` score `4.3552` n `54` status `ready` deltaP `35.7498` edge `0.4053` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.3552` n `54` status `ready` deltaP `35.7498` edge `0.4053` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8225` n `127` status `ready` deltaP `14.7166` edge `0.1602` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0656` n `127` status `ready` deltaP `6.654` edge `0.125` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.6583` n `127` status `ready` deltaP `15.9136` edge `0.0533` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.0614` n `127` status `ready` deltaP `10.7737` edge `0.01` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.2671` n `54` status `ready` deltaP `5.1453` edge `0.0046` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.2671` n `54` status `ready` deltaP `5.1453` edge `0.0046` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.3152` n `127` status `ready` deltaP `4.7883` edge `0.0025` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.3256` n `54` status `ready` deltaP `-0.6506` edge `0.001` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.3256` n `54` status `ready` deltaP `-0.6506` edge `0.001` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.354` n `54` status `ready` deltaP `2.6004` edge `0.0095` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.354` n `54` status `ready` deltaP `2.6004` edge `0.0095` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3833` n `54` status `ready` deltaP `5.7053` edge `0.0151` maxDD `-5.8485`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

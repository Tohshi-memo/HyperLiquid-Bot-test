# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T06:52:26.844038+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8268`

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

- `market_context_high->crypto_alt_4h` score `8.0937` n `127` status `ready` deltaP `20.434` edge `0.6297` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.0701` n `54` status `ready` deltaP `38.5017` edge `0.3325` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0701` n `54` status `ready` deltaP `38.5017` edge `0.3325` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.2965` n `127` status `ready` deltaP `23.5596` edge `0.4998` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `6.1127` n `54` status `ready` deltaP `22.8546` edge `0.4017` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.1127` n `54` status `ready` deltaP `22.8546` edge `0.4017` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.3443` n `54` status `ready` deltaP `35.7498` edge `0.4039` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.3443` n `54` status `ready` deltaP `35.7498` edge `0.4039` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.5731` n `139` status `ready` deltaP `13.3094` edge `0.1488` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0416` n `139` status `ready` deltaP `7.2836` edge `0.1188` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5437` n `127` status `ready` deltaP `14.5417` edge `0.0529` maxDD `-1.6961`
- `risk_on_high->index_1h` score `-0.1026` n `65` status `ready` deltaP `3.8485` edge `0.0042` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.1026` n `65` status `ready` deltaP `3.8485` edge `0.0042` maxDD `-0.7394`
- `market_context_high->metal_1h` score `-0.1694` n `139` status `ready` deltaP `9.5291` edge `0.0093` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.2144` n `139` status `ready` deltaP `6.5159` edge `0.0039` maxDD `-1.3195`
- `risk_on_high->crypto_major_1h` score `-0.2199` n `65` status `ready` deltaP `4.2953` edge `0.0154` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2199` n `65` status `ready` deltaP `4.2953` edge `0.0154` maxDD `-3.7781`
- `risk_on_high->metal_1h` score `-0.3592` n `65` status `ready` deltaP `3.4638` edge `0.004` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3592` n `65` status `ready` deltaP `3.4638` edge `0.004` maxDD `-0.8513`
- `risk_on_high->equity_1h` score `-0.4402` n `65` status `ready` deltaP `8.4269` edge `0.017` maxDD `-5.3696`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

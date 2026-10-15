# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T14:37:33.032203+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8978`

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

- `risk_on_high->commodity_24h` score `7.8895` n `54` status `ready` deltaP `41.2892` edge `0.3822` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.8895` n `54` status `ready` deltaP `41.2892` edge `0.3822` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.8622` n `122` status `ready` deltaP `18.1103` edge `0.6259` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `6.0329` n `122` status `ready` deltaP `19.7096` edge `0.5035` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.6686` n `54` status `ready` deltaP `20.8729` edge `0.3779` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.6686` n `54` status `ready` deltaP `20.8729` edge `0.3779` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.1316` n `54` status `ready` deltaP `33.1583` edge `0.3939` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.1316` n `54` status `ready` deltaP `33.1583` edge `0.3939` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8604` n `122` status `ready` deltaP `13.7062` edge `0.1701` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1492` n `122` status `ready` deltaP `5.6592` edge `0.1386` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0023` n `122` status `ready` deltaP `10.0085` edge `0.038` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2957` n `115` status `ready` deltaP `13.4631` edge `0.1505` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3454` n `122` status `ready` deltaP `-0.613` edge `-0.0018` maxDD `-0.4047`
- `risk_on_high->crypto_major_1h` score `-0.3461` n `54` status `ready` deltaP `0.9537` edge `0.0215` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3461` n `54` status `ready` deltaP `0.9537` edge `0.0215` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.366` n `54` status `ready` deltaP `4.5077` edge `0.0253` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.366` n `54` status `ready` deltaP `4.5077` edge `0.0253` maxDD `-5.8485`
- `market_context_high->index_1h` score `-0.4827` n `122` status `ready` deltaP `1.8142` edge `0.0008` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.5038` n `54` status `ready` deltaP `1.1034` edge `0.0012` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5038` n `54` status `ready` deltaP `1.1034` edge `0.0012` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

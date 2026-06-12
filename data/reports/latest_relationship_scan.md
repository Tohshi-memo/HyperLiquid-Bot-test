# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T03:37:31.102541+00:00`
- Price records: `672`
- Market context records: `3649`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `36.8667` n `32` status `ready` deltaP `42.0139` edge `2.7964` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `36.8667` n `32` status `ready` deltaP `42.0139` edge `2.7964` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `33.0874` n `32` status `ready` deltaP `44.0972` edge `2.4633` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `33.0874` n `32` status `ready` deltaP `44.0972` edge `2.4633` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `29.0456` n `32` status `ready` deltaP `41.1458` edge `2.1613` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `29.0456` n `32` status `ready` deltaP `41.1458` edge `2.1613` maxDD `-0.8779`
- `risk_on_high->index_24h` score `18.8194` n `32` status `ready` deltaP `44.0972` edge `1.2743` maxDD `0.0`
- `risk_on_and_context->index_24h` score `18.8194` n `32` status `ready` deltaP `44.0972` edge `1.2743` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.5188` n `32` status `ready` deltaP `20.8841` edge `0.9329` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.5188` n `32` status `ready` deltaP `20.8841` edge `0.9329` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `10.7194` n `32` status `ready` deltaP `29.6875` edge `0.7215` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `10.7194` n `32` status `ready` deltaP `29.6875` edge `0.7215` maxDD `-0.7574`
- `market_context_high->equity_24h` score `8.7994` n `157` status `ready` deltaP `21.1673` edge `1.1586` maxDD `-35.3144`
- `market_context_high->index_24h` score `8.4233` n `157` status `ready` deltaP `29.4475` edge `0.6772` maxDD `-11.3924`
- `market_context_high->metal_24h` score `3.1867` n `157` status `ready` deltaP `23.9948` edge `0.6438` maxDD `-21.6171`
- `risk_on_high->crypto_alt_4h` score `2.9038` n `32` status `ready` deltaP `0.9909` edge `0.4198` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.9038` n `32` status `ready` deltaP `0.9909` edge `0.4198` maxDD `-11.7537`
- `market_context_high->crypto_major_24h` score `2.8617` n `157` status `ready` deltaP `8.1962` edge `0.8905` maxDD `-49.5335`
- `risk_on_high->equity_4h` score `2.4636` n `32` status `ready` deltaP `9.375` edge `0.3668` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4636` n `32` status `ready` deltaP `9.375` edge `0.3668` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

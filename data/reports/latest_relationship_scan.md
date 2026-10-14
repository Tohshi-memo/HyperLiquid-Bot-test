# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T17:37:29.586874+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9370`

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

- `market_context_high->crypto_alt_4h` score `7.1219` n `117` status `ready` deltaP `18.7461` edge `0.6134` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.3745` n `54` status `ready` deltaP `32.5217` edge `0.3144` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3745` n `54` status `ready` deltaP `32.5217` edge `0.3144` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.2172` n `117` status `ready` deltaP `21.12` edge `0.5332` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.7108` n `54` status `ready` deltaP `21.0253` edge `0.3805` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.7108` n `54` status `ready` deltaP `21.0253` edge `0.3805` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.5809` n `54` status `ready` deltaP `34.2254` edge `0.4444` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.5809` n `54` status `ready` deltaP `34.2254` edge `0.4444` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7112` n `117` status `ready` deltaP `13.2671` edge `0.1609` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2202` n `117` status `ready` deltaP `5.6618` edge `0.1445` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3606` n `117` status `ready` deltaP `13.9176` edge `0.0418` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2583` n `117` status `ready` deltaP `8.4626` edge `0.009` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.3632` n `54` status `ready` deltaP `1.1034` edge `0.0183` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3632` n `54` status `ready` deltaP `1.1034` edge `0.0183` maxDD `-3.7781`
- `risk_on_high->metal_1h` score `-0.3823` n `54` status `ready` deltaP `3.0495` edge `0.0038` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3823` n `54` status `ready` deltaP `3.0495` edge `0.0038` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.4044` n `117` status `ready` deltaP `0.3465` edge `0.002` maxDD `-0.3742`
- `risk_on_high->metal_4h` score `-0.5466` n `54` status `ready` deltaP `1.5244` edge `0.0243` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.5466` n `54` status `ready` deltaP `1.5244` edge `0.0243` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.5875` n `117` status `ready` deltaP `0.0231` edge `-0.0007` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

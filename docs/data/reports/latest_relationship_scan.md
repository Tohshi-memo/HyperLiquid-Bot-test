# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T17:07:25.818946+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9338`

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

- `market_context_high->crypto_alt_4h` score `7.0893` n `117` status `ready` deltaP `18.5937` edge `0.6117` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.3366` n `54` status `ready` deltaP `32.3478` edge `0.3124` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3366` n `54` status `ready` deltaP `32.3478` edge `0.3124` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.1968` n `117` status `ready` deltaP `21.12` edge `0.5315` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.6782` n `54` status `ready` deltaP `20.8729` edge `0.3788` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.6782` n `54` status `ready` deltaP `20.8729` edge `0.3788` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.5677` n `54` status `ready` deltaP `34.2254` edge `0.4427` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.5677` n `54` status `ready` deltaP `34.2254` edge `0.4427` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7651` n `117` status `ready` deltaP `13.5665` edge `0.1634` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.267` n `117` status `ready` deltaP `5.9612` edge `0.1464` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.351` n `117` status `ready` deltaP `13.9176` edge `0.041` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2703` n `117` status `ready` deltaP `8.3129` edge `0.009` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.3329` n `54` status `ready` deltaP `1.4028` edge `0.0202` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3329` n `54` status `ready` deltaP `1.4028` edge `0.0202` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.378` n `117` status `ready` deltaP `0.6468` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.3901` n `54` status `ready` deltaP `2.8998` edge `0.0038` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3901` n `54` status `ready` deltaP `2.8998` edge `0.0038` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.5528` n `54` status `ready` deltaP `1.5244` edge `0.0235` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.5528` n `54` status `ready` deltaP `1.5244` edge `0.0235` maxDD `-1.6961`
- `risk_on_high->crypto_alt_1h` score `-0.5859` n `54` status `ready` deltaP `3.3101` edge `0.0054` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

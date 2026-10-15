# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T12:22:37.990784+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9006`

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

- `market_context_high->crypto_alt_4h` score `8.501` n `122` status `ready` deltaP `18.4152` edge `0.6771` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.9111` n `54` status `ready` deltaP `41.2892` edge `0.384` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9111` n `54` status `ready` deltaP `41.2892` edge `0.384` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.4797` n `122` status `ready` deltaP `20.0145` edge `0.5387` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `6.3074` n `54` status `ready` deltaP `21.1778` edge `0.4291` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.3074` n `54` status `ready` deltaP `21.1778` edge `0.4291` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.422` n `54` status `ready` deltaP `33.4632` edge `0.4291` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.422` n `54` status `ready` deltaP `33.4632` edge `0.4291` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8017` n `122` status `ready` deltaP `13.4068` edge `0.1672` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0773` n `122` status `ready` deltaP `5.2101` edge `0.1356` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0752` n `122` status `ready` deltaP `10.7707` edge `0.039` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2817` n `115` status `ready` deltaP `13.4631` edge `0.1523` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3625` n `122` status `ready` deltaP `-0.9133` edge `-0.002` maxDD `-0.4047`
- `risk_on_high->crypto_major_1h` score `-0.3928` n `54` status `ready` deltaP `0.5046` edge `0.0185` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3928` n `54` status `ready` deltaP `0.5046` edge `0.0185` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.4042` n `54` status `ready` deltaP `4.2083` edge `0.0224` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.4042` n `54` status `ready` deltaP `4.2083` edge `0.0224` maxDD `-5.8485`
- `risk_on_high->metal_1h` score `-0.503` n `54` status `ready` deltaP `1.1034` edge `0.0013` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.503` n `54` status `ready` deltaP `1.1034` edge `0.0013` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.5147` n `122` status `ready` deltaP `1.2136` edge `0.0007` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

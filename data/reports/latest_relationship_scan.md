# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T16:52:32.592200+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9290`

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

- `market_context_high->crypto_alt_4h` score `7.0869` n `117` status `ready` deltaP `18.5937` edge `0.6115` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.3174` n `54` status `ready` deltaP `32.3478` edge `0.3108` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3174` n `54` status `ready` deltaP `32.3478` edge `0.3108` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.1932` n `117` status `ready` deltaP `21.12` edge `0.5312` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.6758` n `54` status `ready` deltaP `20.8729` edge `0.3786` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.6758` n `54` status `ready` deltaP `20.8729` edge `0.3786` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.5653` n `54` status `ready` deltaP `34.2254` edge `0.4424` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.5653` n `54` status `ready` deltaP `34.2254` edge `0.4424` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7975` n `117` status `ready` deltaP `13.7162` edge `0.1651` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2898` n `117` status `ready` deltaP `6.1109` edge `0.1473` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3474` n `117` status `ready` deltaP `13.9176` edge `0.0407` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2835` n `117` status `ready` deltaP `8.1632` edge `0.0089` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.3181` n `54` status `ready` deltaP `1.5525` edge `0.0211` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3181` n `54` status `ready` deltaP `1.5525` edge `0.0211` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.378` n `117` status `ready` deltaP `0.6468` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.3986` n `54` status `ready` deltaP `2.7501` edge `0.0037` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3986` n `54` status `ready` deltaP `2.7501` edge `0.0037` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.5551` n `54` status `ready` deltaP `1.5244` edge `0.0232` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.5551` n `54` status `ready` deltaP `1.5244` edge `0.0232` maxDD `-1.6961`
- `risk_on_high->crypto_alt_1h` score `-0.5649` n `54` status `ready` deltaP `3.4598` edge `0.0071` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

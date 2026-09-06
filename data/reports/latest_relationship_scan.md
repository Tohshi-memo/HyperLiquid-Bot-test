# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T13:07:24.964978+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10511`

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

- `risk_on_high->unknown_24h` score `102.5813` n `110` status `ready` deltaP `20.9849` edge `8.4342` maxDD `-0.7193`
- `risk_on_and_context->unknown_24h` score `102.5813` n `110` status `ready` deltaP `20.9849` edge `8.4342` maxDD `-0.7193`
- `risk_on_high->crypto_major_24h` score `5.9542` n `110` status `ready` deltaP `18.9079` edge `1.0082` maxDD `-41.7122`
- `risk_on_and_context->crypto_major_24h` score `5.9542` n `110` status `ready` deltaP `18.9079` edge `1.0082` maxDD `-41.7122`
- `market_context_high->equity_24h` score `1.5244` n `196` status `ready` deltaP `13.3291` edge `0.3337` maxDD `-13.9754`
- `risk_on_high->index_1h` score `-0.1408` n `141` status `ready` deltaP `4.4921` edge `-0.0033` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1408` n `141` status `ready` deltaP `4.4921` edge `-0.0033` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.174` n `141` status `ready` deltaP `7.4149` edge `-0.0005` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.174` n `141` status `ready` deltaP `7.4149` edge `-0.0005` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.4872` n `141` status `ready` deltaP `5.746` edge `-0.0133` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4872` n `141` status `ready` deltaP `5.746` edge `-0.0133` maxDD `-2.6638`
- `risk_on_high->crypto_alt_1h` score `-0.492` n `141` status `ready` deltaP `1.049` edge `0.0537` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.492` n `141` status `ready` deltaP `1.049` edge `0.0537` maxDD `-5.4685`
- `risk_on_high->commodity_1h` score `-0.5802` n `141` status `ready` deltaP `0.3005` edge `0.0` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.5802` n `141` status `ready` deltaP `0.3005` edge `0.0` maxDD `-1.0281`
- `market_context_high->commodity_1h` score `-0.7699` n `250` status `ready` deltaP `0.3629` edge `-0.0016` maxDD `-1.5315`
- `risk_on_high->crypto_major_1h` score `-0.8995` n `141` status `ready` deltaP `-0.1412` edge `0.0157` maxDD `-7.4065`
- `risk_on_and_context->crypto_major_1h` score `-0.8995` n `141` status `ready` deltaP `-0.1412` edge `0.0157` maxDD `-7.4065`
- `market_context_high->metal_1h` score `-0.9671` n `250` status `ready` deltaP `3.2958` edge `-0.0068` maxDD `-2.9947`
- `market_context_high->index_1h` score `-1.1125` n `250` status `ready` deltaP `2.5545` edge `0.0007` maxDD `-3.1683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

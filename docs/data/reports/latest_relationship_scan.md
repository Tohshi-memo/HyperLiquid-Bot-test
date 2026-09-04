# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T14:52:31.671880+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10928`

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

- `risk_on_high->unknown_4h` score `20.3476` n `133` status `ready` deltaP `7.779` edge `1.7056` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.3476` n `133` status `ready` deltaP `7.779` edge `1.7056` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.3553` n `133` status `ready` deltaP `-1.353` edge `1.013` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.3553` n `133` status `ready` deltaP `-1.353` edge `1.013` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.8593` n `204` status `ready` deltaP `8.7668` edge `0.8327` maxDD `-2.563`
- `market_context_high->unknown_1h` score `9.1798` n `212` status `ready` deltaP `-0.7288` edge `0.8329` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `1.4042` n `58` status `ready` deltaP `11.1911` edge `0.0625` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `1.073` n `58` status `ready` deltaP `10.71` edge `0.0353` maxDD `-0.0495`
- `news_risk_high->crypto_alt_24h` score `0.5529` n `58` status `ready` deltaP `15.4214` edge `-0.0004` maxDD `-3.1734`
- `market_context_high->equity_24h` score `0.2173` n `167` status `ready` deltaP `13.3317` edge `0.3638` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.1561` n `133` status `ready` deltaP `12.8619` edge `0.0055` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1561` n `133` status `ready` deltaP `12.8619` edge `0.0055` maxDD `-1.699`
- `news_risk_high->index_1h` score `0.1353` n `58` status `ready` deltaP `6.6746` edge `-0.0019` maxDD `-0.6867`
- `news_risk_high->commodity_1h` score `-0.0969` n `58` status `ready` deltaP `5.3325` edge `0.001` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1707` n `133` status `ready` deltaP `3.693` edge `-0.002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1707` n `133` status `ready` deltaP `3.693` edge `-0.002` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.2616` n `133` status `ready` deltaP `3.7031` edge `0.0552` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2616` n `133` status `ready` deltaP `3.7031` edge `0.0552` maxDD `-5.4685`
- `news_risk_high->equity_1h` score `-0.2963` n `58` status `ready` deltaP `4.8834` edge `0.0019` maxDD `-3.4625`
- `risk_on_high->commodity_1h` score `-0.4002` n `133` status `ready` deltaP `0.4064` edge `0.0005` maxDD `-1.0281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

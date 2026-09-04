# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T14:22:26.593150+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10926`

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

- `risk_on_high->unknown_4h` score `20.2384` n `133` status `ready` deltaP `7.779` edge `1.6965` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.2384` n `133` status `ready` deltaP `7.779` edge `1.6965` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.3192` n `133` status `ready` deltaP `-1.2033` edge `1.009` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.3192` n `133` status `ready` deltaP `-1.2033` edge `1.009` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.1158` n `202` status `ready` deltaP `8.5532` edge `0.8555` maxDD `-2.563`
- `market_context_high->unknown_1h` score `9.1438` n `212` status `ready` deltaP `-0.5791` edge `0.8289` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `1.4666` n `60` status `ready` deltaP `12.2256` edge `0.0608` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `0.994` n `60` status `ready` deltaP `10.9375` edge `0.0272` maxDD `-0.0495`
- `market_context_high->equity_24h` score `0.3927` n `167` status `ready` deltaP `13.6789` edge `0.3761` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.167` n `133` status `ready` deltaP `13.0116` edge `0.0059` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.167` n `133` status `ready` deltaP `13.0116` edge `0.0059` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0536` n `60` status `ready` deltaP `4.8703` edge `-0.004` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.1027` n `60` status `ready` deltaP `5.0799` edge `0.0022` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1614` n `133` status `ready` deltaP `3.8427` edge `-0.0018` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1614` n `133` status `ready` deltaP `3.8427` edge `-0.0018` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.2604` n `133` status `ready` deltaP `3.7031` edge `0.0553` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2604` n `133` status `ready` deltaP `3.7031` edge `0.0553` maxDD `-5.4685`
- `risk_on_high->commodity_1h` score `-0.3854` n `133` status `ready` deltaP `0.5561` edge `0.0014` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.3854` n `133` status `ready` deltaP `0.5561` edge `0.0014` maxDD `-1.0281`
- `market_context_high->metal_1h` score `-0.4207` n `212` status `ready` deltaP `6.649` edge `-0.0025` maxDD `-2.9947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

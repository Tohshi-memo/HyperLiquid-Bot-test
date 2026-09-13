# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T08:07:28.618049+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12880`

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

- `market_context_high->unknown_24h` score `16552.2472` n `59` status `ready` deltaP `13.6241` edge `1379.2683` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.1567` n `82` status `ready` deltaP `-5.2505` edge `32.0069` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.6527` n `82` status `ready` deltaP `31.5379` edge `1.3096` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.644` n `82` status `ready` deltaP `37.589` edge `1.3668` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `9.933` n `59` status `ready` deltaP `21.4925` edge `0.7672` maxDD `-3.9523`
- `market_context_high->equity_24h` score `8.4066` n `59` status `ready` deltaP `42.3935` edge `0.4939` maxDD `-4.4114`
- `news_risk_high->equity_24h` score `7.0843` n `82` status `ready` deltaP `20.3803` edge `0.6325` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.4316` n `82` status `ready` deltaP `45.6046` edge `0.2496` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5493` n `82` status `ready` deltaP `23.7043` edge `0.2665` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2472` n `59` status `ready` deltaP `41.8403` edge `0.075` maxDD `0.0`
- `market_context_high->index_24h` score `3.5823` n `59` status `ready` deltaP `39.4244` edge `0.0778` maxDD `-0.7014`
- `market_context_high->metal_24h` score `0.8928` n `59` status `ready` deltaP `12.9767` edge `0.1154` maxDD `-1.9958`
- `news_risk_high->index_4h` score `0.3494` n `82` status `ready` deltaP `11.5853` edge `0.0304` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.291` n `65` status `ready` deltaP `10.0` edge `0.1381` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.291` n `65` status `ready` deltaP `10.0` edge `0.1381` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `0.146` n `65` status `ready` deltaP `5.152` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.146` n `65` status `ready` deltaP `5.152` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.1239` n `65` status `ready` deltaP `3.1644` edge `0.0016` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.1239` n `65` status `ready` deltaP `3.1644` edge `0.0016` maxDD `-0.3081`
- `risk_on_high->commodity_1h` score `-0.2514` n `65` status `ready` deltaP `0.8522` edge `-0.002` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

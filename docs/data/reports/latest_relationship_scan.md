# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T12:37:26.011430+00:00`
- Price records: `672`
- Market context records: `7565`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `market_context_high->commodity_4h` score `0.0229` n `173` status `ready` deltaP `7.8777` edge `0.0254` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.0773` n `173` status `ready` deltaP `6.2048` edge `0.0083` maxDD `-1.7657`
- `market_context_high->fx_1h` score `-0.2453` n `173` status `ready` deltaP `2.6689` edge `0.0007` maxDD `-0.6615`
- `market_context_high->commodity_24h` score `-0.3511` n `153` status `ready` deltaP `11.923` edge `0.0496` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.3591` n `173` status `ready` deltaP `3.7945` edge `0.002` maxDD `-1.5775`
- `market_context_high->unknown_1h` score `-0.3885` n `173` status `ready` deltaP `2.7716` edge `0.0115` maxDD `-1.3217`
- `market_context_high->unknown_4h` score `-0.443` n `173` status `ready` deltaP `11.6524` edge `0.1014` maxDD `-6.2031`
- `market_context_high->crypto_major_1h` score `-0.6118` n `173` status `ready` deltaP `5.3416` edge `0.027` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.6226` n `173` status `ready` deltaP `0.4595` edge `0.021` maxDD `-5.9775`
- `market_context_high->fx_24h` score `-0.7461` n `153` status `ready` deltaP `9.9075` edge `0.0158` maxDD `-3.8554`
- `market_context_high->index_4h` score `-0.7562` n `173` status `ready` deltaP `9.9777` edge `0.0258` maxDD `-4.8079`
- `market_context_high->metal_1h` score `-1.0753` n `173` status `ready` deltaP `0.9709` edge `0.0143` maxDD `-1.4971`
- `market_context_high->fx_4h` score `-1.2509` n `173` status `ready` deltaP `0.6584` edge `0.0037` maxDD `-2.1439`
- `market_context_high->equity_1h` score `-1.4092` n `173` status `ready` deltaP `4.6209` edge `0.0296` maxDD `-14.6193`
- `market_context_high->metal_4h` score `-1.5027` n `173` status `ready` deltaP `1.0257` edge `0.0487` maxDD `-4.8549`
- `market_context_high->unknown_24h` score `-1.6927` n `154` status `ready` deltaP `4.5117` edge `0.0278` maxDD `-9.9917`
- `market_context_high->crypto_alt_4h` score `-1.823` n `173` status `ready` deltaP `0.6573` edge `0.0362` maxDD `-15.2776`
- `market_context_high->crypto_major_4h` score `-2.4169` n `173` status `ready` deltaP `4.9767` edge `0.0464` maxDD `-23.4879`
- `market_context_high->equity_4h` score `-3.4501` n `173` status `ready` deltaP `2.0717` edge `0.1487` maxDD `-35.387`
- `market_context_high->index_24h` score `-4.4089` n `153` status `ready` deltaP `-19.7604` edge `-0.015` maxDD `-18.8138`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

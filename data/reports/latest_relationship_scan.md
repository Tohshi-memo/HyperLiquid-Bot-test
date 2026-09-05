# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T00:22:29.534208+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10422`

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

- `risk_on_high->unknown_4h` score `19.9519` n `133` status `ready` deltaP `8.9985` edge `1.6645` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.9519` n `133` status `ready` deltaP `8.9985` edge `1.6645` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.4544` n `217` status `ready` deltaP `9.4351` edge `0.7945` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `5.4621` n `42` status `ready` deltaP `20.5853` edge `0.3449` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `3.1321` n `42` status `ready` deltaP `14.322` edge `0.2096` maxDD `-1.1927`
- `news_risk_high->commodity_24h` score `2.844` n `42` status `ready` deltaP `17.0387` edge `0.1406` maxDD `-0.042`
- `news_risk_high->metal_4h` score `1.9791` n `42` status `ready` deltaP `20.151` edge `0.0527` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.5966` n `42` status `ready` deltaP `10.2061` edge `0.0851` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5179` n `42` status `ready` deltaP `13.4945` edge `0.0756` maxDD `-0.7924`
- `news_risk_high->index_1h` score `1.4795` n `42` status `ready` deltaP `18.5843` edge `0.0128` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.9163` n `42` status `ready` deltaP `11.306` edge `0.0203` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `0.8003` n `42` status `ready` deltaP `2.6661` edge `0.0672` maxDD `-0.4628`
- `news_risk_high->crypto_alt_4h` score `0.5932` n `42` status `ready` deltaP `4.5296` edge `0.0521` maxDD `-1.296`
- `news_risk_high->crypto_alt_1h` score `0.5262` n `42` status `ready` deltaP `5.1825` edge `0.0358` maxDD `-0.7867`
- `risk_on_high->metal_1h` score `0.1451` n `133` status `ready` deltaP `13.311` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1451` n `133` status `ready` deltaP `13.311` edge `0.0011` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.1099` n `42` status `ready` deltaP `8.2977` edge `0.0034` maxDD `-0.9036`
- `news_risk_high->fx_4h` score `0.0552` n `42` status `ready` deltaP `7.7744` edge `-0.002` maxDD `-0.9514`
- `risk_on_high->index_1h` score `-0.2291` n `133` status `ready` deltaP `2.7948` edge `-0.0035` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.2291` n `133` status `ready` deltaP `2.7948` edge `-0.0035` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

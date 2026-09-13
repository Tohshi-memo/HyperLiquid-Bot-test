# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T22:07:24.211538+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12657`

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

- `market_context_high->unknown_24h` score `10017.9744` n `56` status `ready` deltaP `10.2093` edge `834.7833` maxDD `-0.613`
- `news_risk_high->unknown_1h` score `436.1152` n `82` status `ready` deltaP `-5.4002` edge `36.4211` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.7501` n `82` status `ready` deltaP `36.3751` edge `1.3688` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.2872` n `82` status `ready` deltaP `38.0236` edge `1.4175` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.9934` n `82` status `ready` deltaP `29.6846` edge `0.8129` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.415` n `82` status `ready` deltaP `53.4566` edge `0.2792` maxDD `-0.0797`
- `risk_on_high->commodity_24h` score `4.9034` n `33` status `ready` deltaP `39.8276` edge `0.1431` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9034` n `33` status `ready` deltaP `39.8276` edge `0.1431` maxDD `0.0`
- `news_risk_high->metal_24h` score `4.8965` n `82` status `ready` deltaP `27.8638` edge `0.2677` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.8578` n `56` status `ready` deltaP `39.8276` edge `0.1393` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `3.1773` n `56` status `ready` deltaP `3.4483` edge `0.4079` maxDD `-9.6226`
- `risk_on_high->crypto_alt_24h` score `2.8932` n `33` status `ready` deltaP `-1.0972` edge `0.382` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `2.8932` n `33` status `ready` deltaP `-1.0972` edge `0.382` maxDD `-7.0204`
- `risk_on_high->fx_24h` score `2.7773` n `33` status `ready` deltaP `52.4347` edge `0.035` maxDD `-0.613`
- `risk_on_and_context->fx_24h` score `2.7773` n `33` status `ready` deltaP `52.4347` edge `0.035` maxDD `-0.613`
- `risk_on_high->commodity_4h` score `1.6288` n `55` status `ready` deltaP `22.8464` edge `0.0184` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.6288` n `55` status `ready` deltaP `22.8464` edge `0.0184` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.1861` n `129` status `ready` deltaP `18.308` edge `0.0186` maxDD `-0.345`
- `market_context_high->fx_24h` score `1.0159` n `56` status `ready` deltaP `33.6576` edge `0.0106` maxDD `-2.3796`
- `news_risk_high->index_4h` score `0.4299` n `82` status `ready` deltaP `12.6524` edge `0.0336` maxDD `-0.6935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

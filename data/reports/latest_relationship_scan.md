# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T22:52:12.213711+00:00`
- Price records: `672`
- Market context records: `1058`
- Flow alert records: `4953`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8668`

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

- `market_context_high->crypto_major_24h` score `14.9361` n `177` status `ready` deltaP `34.1739` edge `1.0632` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.8256` n `177` status `ready` deltaP `11.7503` edge `0.4472` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.5589` n `177` status `ready` deltaP `11.4999` edge `0.2779` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.8132` n `177` status `ready` deltaP `10.7707` edge `0.2226` maxDD `-2.1308`
- `market_context_high->metal_24h` score `2.1283` n `177` status `ready` deltaP `-6.6127` edge `0.3996` maxDD `-7.2523`
- `market_context_high->fx_1h` score `-0.1104` n `179` status `ready` deltaP `4.6976` edge `0.0001` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.3532` n `179` status `ready` deltaP `7.0819` edge `0.0167` maxDD `-5.4676`
- `market_context_high->index_1h` score `-0.4755` n `179` status `ready` deltaP `3.8947` edge `0.0124` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5176` n `179` status `ready` deltaP `0.4223` edge `0.0268` maxDD `-4.1532`
- `market_context_high->fx_4h` score `-0.7558` n `179` status `ready` deltaP `0.126` edge `0.0019` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7578` n `179` status `ready` deltaP `0.4399` edge `0.0147` maxDD `-3.7959`
- `market_context_high->index_4h` score `-1.004` n `179` status `ready` deltaP `0.5714` edge `0.0415` maxDD `-5.6512`
- `market_context_high->crypto_alt_1h` score `-1.0907` n `179` status `ready` deltaP `1.3641` edge `0.0086` maxDD `-5.3538`
- `market_context_high->equity_4h` score `-1.129` n `179` status `ready` deltaP `2.1963` edge `0.0737` maxDD `-9.5939`
- `market_context_high->metal_1h` score `-1.4163` n `179` status `ready` deltaP `3.6388` edge `-0.0331` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `-2.7201` n `179` status `ready` deltaP `7.3366` edge `0.0554` maxDD `-19.4788`
- `market_context_high->crypto_alt_4h` score `-2.8133` n `179` status `ready` deltaP `0.9325` edge `0.0348` maxDD `-15.0367`
- `market_context_high->fx_24h` score `-3.1464` n `177` status `ready` deltaP `3.8018` edge `-0.0211` maxDD `-19.2774`
- `market_context_high->metal_4h` score `-3.3107` n `179` status `ready` deltaP `0.0716` edge `-0.1479` maxDD `-15.8287`
- `market_context_high->commodity_4h` score `-3.675` n `179` status `ready` deltaP `-5.6079` edge `0.0479` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

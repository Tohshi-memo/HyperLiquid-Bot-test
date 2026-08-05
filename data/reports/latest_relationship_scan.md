# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T05:52:24.586409+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11824`

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

- `market_context_high->unknown_24h` score `14.883` n `88` status `ready` deltaP `13.4469` edge `1.1549` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.7231` n `90` status `ready` deltaP `2.815` edge `0.5577` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.581` n `90` status `ready` deltaP `17.2324` edge `0.1015` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.2249` n `88` status `ready` deltaP `2.9671` edge `0.2541` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.1476` n `88` status `ready` deltaP `27.2096` edge `0.0863` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2845` n `90` status `ready` deltaP `5.642` edge `0.0277` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0979` n `90` status `ready` deltaP `7.006` edge `-0.0037` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0735` n `90` status `ready` deltaP `13.1572` edge `0.0077` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5504` n `90` status `ready` deltaP `-1.4571` edge `-0.0114` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6554` n `90` status `ready` deltaP `-1.3539` edge `-0.0216` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7616` n `90` status `ready` deltaP `3.1843` edge `0.0046` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.8653` n `90` status `ready` deltaP `-3.2069` edge `-0.0185` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-0.9659` n `88` status `ready` deltaP `4.435` edge `-0.0091` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.3153` n `90` status `ready` deltaP `1.8089` edge `-0.0417` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8817` n `90` status `ready` deltaP `2.5549` edge `-0.1047` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.941` n `88` status `ready` deltaP `-6.8497` edge `0.0163` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1295` n `90` status `ready` deltaP `-13.0454` edge `-0.0606` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3076` n `90` status `ready` deltaP `2.1989` edge `-0.2456` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3793` n `90` status `ready` deltaP `-11.1111` edge `-0.0702` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.6248` n `88` status `ready` deltaP `7.0076` edge `-0.0999` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

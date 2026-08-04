# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T22:37:26.527846+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9857`

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

- `market_context_high->unknown_24h` score `18.3618` n `79` status `ready` deltaP `18.3523` edge `1.4121` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4109` n `90` status `ready` deltaP `1.7479` edge `0.5388` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.6272` n `90` status `ready` deltaP `17.6897` edge `0.1023` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9505` n `79` status `ready` deltaP `-0.5252` edge `0.2422` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7901` n `79` status `ready` deltaP `21.6398` edge `0.0776` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3145` n `90` status `ready` deltaP `5.9414` edge `0.0282` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1111` n `90` status `ready` deltaP `7.1557` edge `-0.0036` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.102` n `90` status `ready` deltaP `13.7669` edge `0.0073` maxDD `-1.8797`
- `market_context_high->crypto_alt_24h` score `-0.3727` n `79` status `ready` deltaP `5.8984` edge `0.0572` maxDD `-4.5445`
- `market_context_high->metal_1h` score `-0.5597` n `90` status `ready` deltaP `-1.9062` edge `-0.0096` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5736` n `90` status `ready` deltaP `-0.1563` edge `-0.0191` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.714` n `90` status `ready` deltaP `3.1843` edge `0.0107` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7429` n `90` status `ready` deltaP `-2.3087` edge `-0.0088` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-0.9559` n `90` status `ready` deltaP `3.4857` edge `-0.0068` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7032` n `90` status `ready` deltaP `4.501` edge `-0.0948` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.9493` n `79` status `ready` deltaP `-7.173` edge `0.0174` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.0216` n `90` status `ready` deltaP `-11.8259` edge `-0.0549` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.414` n `90` status `ready` deltaP `-11.4105` edge `-0.0711` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4264` n `90` status `ready` deltaP `1.8995` edge `-0.2535` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-5.0712` n `79` status `ready` deltaP `7.2806` edge `-0.0846` maxDD `-38.1268`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

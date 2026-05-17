# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T18:52:12.916414+00:00`
- Price records: `672`
- Market context records: `1041`
- Flow alert records: `4902`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8652`

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

- `market_context_high->crypto_major_24h` score `14.3468` n `182` status `ready` deltaP `33.1833` edge `1.0332` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5904` n `182` status `ready` deltaP `11.4505` edge `0.4296` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.2351` n `182` status `ready` deltaP `11.0277` edge `0.2749` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.443` n `182` status `ready` deltaP `10.3182` edge `0.2156` maxDD `-2.1308`
- `market_context_high->metal_24h` score `0.8766` n `182` status `ready` deltaP `-6.582` edge `0.3888` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0524` n `183` status `ready` deltaP `5.723` edge `0.0007` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4292` n `183` status `ready` deltaP `4.4288` edge `0.0127` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6021` n `183` status `ready` deltaP `0.0572` edge `0.0251` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6663` n `183` status `ready` deltaP `1.1788` edge `0.0174` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-1.018` n `183` status `ready` deltaP `5.8277` edge `0.0003` maxDD `-7.9187`
- `market_context_high->fx_4h` score `-1.0763` n `182` status `ready` deltaP `1.1626` edge `0.0022` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.3106` n `183` status `ready` deltaP `0.1465` edge `-0.0016` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.3616` n `182` status `ready` deltaP `-0.2144` edge `0.0356` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.5395` n `182` status `ready` deltaP `1.9515` edge `0.0739` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.9138` n `183` status `ready` deltaP `2.931` edge `-0.0342` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.7375` n `182` status `ready` deltaP `1.573` edge `0.0392` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.0471` n `182` status `ready` deltaP `7.5114` edge `0.0666` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.1844` n `182` status `ready` deltaP `2.9512` edge `-0.0203` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.589` n `182` status `ready` deltaP `-4.9836` edge `0.0509` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.941` n `182` status `ready` deltaP `-0.8443` edge `-0.1563` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

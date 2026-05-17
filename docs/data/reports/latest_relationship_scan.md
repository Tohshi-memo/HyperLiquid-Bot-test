# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T19:22:15.129246+00:00`
- Price records: `672`
- Market context records: `1043`
- Flow alert records: `4908`
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

- `market_context_high->crypto_major_24h` score `14.3218` n `182` status `ready` deltaP `33.1399` edge `1.0314` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5887` n `182` status `ready` deltaP `11.489` edge `0.4292` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.141` n `182` status `ready` deltaP `10.7668` edge `0.2688` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.3885` n `182` status `ready` deltaP `10.0568` edge `0.2128` maxDD `-2.1308`
- `market_context_high->metal_24h` score `0.7544` n `182` status `ready` deltaP `-6.8342` edge `0.3803` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0438` n `183` status `ready` deltaP `5.8727` edge `0.0008` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4136` n `183` status `ready` deltaP `4.5785` edge `0.013` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5961` n `183` status `ready` deltaP `0.0572` edge `0.0256` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6807` n `183` status `ready` deltaP `1.0291` edge `0.0172` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-1.0288` n `183` status `ready` deltaP `5.8277` edge `-0.0006` maxDD `-7.9187`
- `market_context_high->fx_4h` score `-1.1019` n `182` status `ready` deltaP `0.8577` edge `0.0021` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.3081` n `183` status `ready` deltaP `0.1465` edge `-0.0014` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.3532` n `182` status `ready` deltaP `-0.2144` edge `0.0363` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.5455` n `182` status `ready` deltaP `1.9515` edge `0.0734` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.8791` n `183` status `ready` deltaP `3.2304` edge `-0.0333` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.7097` n `182` status `ready` deltaP `1.7254` edge `0.0405` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.0821` n `182` status `ready` deltaP `7.359` edge `0.0647` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.1961` n `182` status `ready` deltaP `2.7719` edge `-0.0206` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.6218` n `182` status `ready` deltaP `-5.2885` edge `0.0502` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9425` n `182` status `ready` deltaP `-0.8443` edge `-0.1565` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

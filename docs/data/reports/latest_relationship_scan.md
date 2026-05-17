# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T19:07:13.840308+00:00`
- Price records: `672`
- Market context records: `1042`
- Flow alert records: `4905`
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

- `market_context_high->crypto_major_24h` score `14.3419` n `182` status `ready` deltaP `33.2418` edge `1.0324` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5908` n `182` status `ready` deltaP `11.4697` edge `0.4295` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.1863` n `182` status `ready` deltaP `10.8974` edge `0.2717` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.4146` n `182` status `ready` deltaP `10.1877` edge `0.2141` maxDD `-2.1308`
- `market_context_high->metal_24h` score `0.8125` n `182` status `ready` deltaP `-6.7079` edge `0.3843` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0438` n `183` status `ready` deltaP `5.8727` edge `0.0008` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.428` n `183` status `ready` deltaP `4.4288` edge `0.0128` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5985` n `183` status `ready` deltaP `0.0572` edge `0.0254` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6663` n `183` status `ready` deltaP `1.1788` edge `0.0174` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-1.018` n `183` status `ready` deltaP `5.8277` edge `0.0003` maxDD `-7.9187`
- `market_context_high->fx_4h` score `-1.0885` n `182` status `ready` deltaP `1.0101` edge `0.0022` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.3021` n `183` status `ready` deltaP `0.1465` edge `-0.0009` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.358` n `182` status `ready` deltaP `-0.2144` edge `0.0359` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.5431` n `182` status `ready` deltaP `1.9515` edge `0.0736` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.8983` n `183` status `ready` deltaP `3.0807` edge `-0.0339` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.7109` n `182` status `ready` deltaP `1.7254` edge `0.0404` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.0531` n `182` status `ready` deltaP `7.5114` edge `0.0661` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.1899` n `182` status `ready` deltaP `2.8617` edge `-0.0204` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.6048` n `182` status `ready` deltaP `-5.1361` edge `0.0506` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9441` n `182` status `ready` deltaP `-0.8443` edge `-0.1567` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

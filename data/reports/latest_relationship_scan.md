# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T17:37:19.671814+00:00`
- Price records: `672`
- Market context records: `1034`
- Flow alert records: `4887`
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

- `market_context_high->crypto_major_24h` score `14.3028` n `182` status `ready` deltaP `33.0525` edge `1.0304` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5324` n `182` status `ready` deltaP `11.3553` edge `0.4254` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.4451` n `182` status `ready` deltaP `11.6728` edge `0.2881` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.5715` n `182` status `ready` deltaP `10.9645` edge `0.222` maxDD `-2.1308`
- `market_context_high->metal_24h` score `1.1965` n `182` status `ready` deltaP `-5.9585` edge `0.4113` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0765` n `183` status `ready` deltaP `5.2739` edge `0.0006` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.44` n `183` status `ready` deltaP `4.4288` edge `0.0118` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6537` n `183` status `ready` deltaP `-0.0925` edge `0.0218` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6687` n `183` status `ready` deltaP `1.1788` edge `0.0172` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0105` n `182` status `ready` deltaP `1.9247` edge `0.0026` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.1344` n `183` status `ready` deltaP `5.678` edge `-0.0084` maxDD `-7.9187`
- `market_context_high->index_4h` score `-1.4112` n `182` status `ready` deltaP `-0.5193` edge `0.0335` maxDD `-6.1444`
- `market_context_high->crypto_alt_1h` score `-1.4401` n `183` status `ready` deltaP `-0.1529` edge `-0.0104` maxDD `-5.3538`
- `market_context_high->equity_4h` score `-1.5961` n `182` status `ready` deltaP `1.7991` edge `0.0702` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-2.0091` n `183` status `ready` deltaP `1.9355` edge `-0.0355` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.9833` n `182` status `ready` deltaP `0.8108` edge `0.0238` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.1583` n `182` status `ready` deltaP `3.3944` edge `-0.0199` maxDD `-19.2774`
- `market_context_high->crypto_major_4h` score `-3.2177` n `182` status `ready` deltaP `7.359` edge `0.0534` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.5454` n `182` status `ready` deltaP `-4.6787` edge `0.0525` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9758` n `182` status `ready` deltaP `-1.454` edge `-0.1567` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

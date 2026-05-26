# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T13:25:50.010211+00:00`
- Price records: `672`
- Market context records: `1942`
- Flow alert records: `7486`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7547`

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

- `market_context_high->crypto_alt_4h` score `7.1027` n `227` status `ready` deltaP `22.2394` edge `0.5581` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4624` n `227` status `ready` deltaP `25.8804` edge `0.4906` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.5824` n `227` status `ready` deltaP `14.2044` edge `0.3229` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0116` n `227` status `ready` deltaP `13.8282` edge `0.1849` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `0.6967` n `232` status `ready` deltaP `7.7811` edge `0.1048` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `0.6716` n `199` status `ready` deltaP `14.5367` edge `0.4911` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.5308` n `232` status `ready` deltaP `7.0963` edge `0.1083` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.2258` n `199` status `ready` deltaP `11.9871` edge `0.1815` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1525` n `199` status `ready` deltaP `4.1922` edge `0.1076` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.131` n `227` status `ready` deltaP `8.4477` edge `0.0635` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1578` n `232` status `ready` deltaP `5.0139` edge `0.0328` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2759` n `199` status `ready` deltaP `9.9323` edge `0.0157` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6082` n `232` status `ready` deltaP `0.6585` edge `0.0081` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6394` n `232` status `ready` deltaP `-2.8278` edge `0.0001` maxDD `-0.3914`
- `market_context_high->equity_24h` score `-0.846` n `199` status `ready` deltaP `8.782` edge `0.3608` maxDD `-33.1875`
- `market_context_high->fx_4h` score `-0.9799` n `227` status `ready` deltaP `-5.2957` edge `-0.0015` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.1462` n `232` status `ready` deltaP `3.6551` edge `0.0137` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4504` n `232` status `ready` deltaP `0.6481` edge `-0.03` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.6484` n `227` status `ready` deltaP `6.8733` edge `0.086` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.9872` n `232` status `ready` deltaP `1.0689` edge `-0.0061` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

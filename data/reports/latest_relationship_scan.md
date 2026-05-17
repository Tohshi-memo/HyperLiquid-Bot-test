# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T15:07:12.489257+00:00`
- Price records: `672`
- Market context records: `1023`
- Flow alert records: `4854`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8635`

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

- `market_context_high->crypto_major_24h` score `13.774` n `190` status `ready` deltaP `32.6233` edge `0.9892` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.3814` n `190` status `ready` deltaP `11.1925` edge `0.4139` maxDD `-9.5387`
- `market_context_high->equity_24h` score `1.8118` n `190` status `ready` deltaP `9.0461` edge `0.2351` maxDD `-6.2204`
- `market_context_high->index_24h` score `1.3939` n `190` status `ready` deltaP `8.3635` edge `0.1894` maxDD `-3.3198`
- `market_context_high->fx_1h` score `-0.1238` n `190` status `ready` deltaP `4.3792` edge `0.0005` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5547` n `190` status `ready` deltaP `2.0186` edge `0.0211` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5748` n `190` status `ready` deltaP `3.224` edge `0.0086` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6552` n `190` status `ready` deltaP `0.1434` edge `0.0201` maxDD `-4.3858`
- `market_context_high->fx_4h` score `-0.9114` n `190` status `ready` deltaP `3.0744` edge `0.0032` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.2387` n `190` status `ready` deltaP `4.7463` edge `-0.0229` maxDD `-11.404`
- `market_context_high->crypto_alt_1h` score `-1.3225` n `190` status `ready` deltaP `-1.0242` edge `-0.0219` maxDD `-7.9323`
- `market_context_high->index_4h` score `-1.3436` n `190` status `ready` deltaP `0.4156` edge `0.0329` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.353` n `190` status `ready` deltaP `2.078` edge `0.0886` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.7495` n `190` status `ready` deltaP `0.7769` edge `-0.0392` maxDD `-8.5553`
- `market_context_high->crypto_alt_4h` score `-2.6676` n `190` status `ready` deltaP `0.767` edge `0.0504` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-2.7935` n `190` status `ready` deltaP `7.5465` edge `0.0875` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.2427` n `190` status `ready` deltaP `1.7846` edge `-0.02` maxDD `-19.2774`
- `market_context_high->metal_24h` score `-3.3904` n `190` status `ready` deltaP `-7.7714` edge `0.3025` maxDD `-33.6581`
- `market_context_high->commodity_4h` score `-3.4215` n `190` status `ready` deltaP `-3.4451` edge `0.0546` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-4.0841` n `190` status `ready` deltaP `-1.8469` edge `-0.1581` maxDD `-21.5883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

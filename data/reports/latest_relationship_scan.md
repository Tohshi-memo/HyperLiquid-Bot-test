# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T20:07:16.140551+00:00`
- Price records: `672`
- Market context records: `1047`
- Flow alert records: `4918`
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

- `market_context_high->crypto_major_24h` score `14.2443` n `182` status `ready` deltaP `32.8323` edge `1.027` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.555` n `182` status `ready` deltaP `11.5473` edge `0.426` maxDD `-9.5387`
- `market_context_high->equity_24h` score `2.987` n `182` status `ready` deltaP `10.3722` edge `0.2586` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.3017` n `182` status `ready` deltaP `9.6614` edge `0.2082` maxDD `-2.1308`
- `market_context_high->metal_24h` score `0.5631` n `182` status `ready` deltaP `-7.2155` edge `0.3669` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0792` n `184` status `ready` deltaP `5.2526` edge `0.0004` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4243` n `184` status `ready` deltaP `4.4454` edge `0.013` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5905` n `184` status `ready` deltaP `0.0976` edge `0.0258` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.7054` n `184` status `ready` deltaP `0.7648` edge `0.0169` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-0.9961` n `184` status `ready` deltaP `5.9067` edge `0.0016` maxDD `-7.9187`
- `market_context_high->fx_4h` score `-1.1409` n `182` status `ready` deltaP `0.4004` edge `0.0019` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.2807` n `184` status `ready` deltaP `0.2343` edge `0.0003` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.3424` n `182` status `ready` deltaP `-0.2144` edge `0.0372` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.6133` n `182` status `ready` deltaP `1.4942` edge `0.0708` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.8782` n `184` status `ready` deltaP `3.2121` edge `-0.0331` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.7279` n `182` status `ready` deltaP `1.573` edge `0.04` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.2003` n `182` status `ready` deltaP `6.9017` edge `0.0579` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.2133` n `182` status `ready` deltaP `2.5009` edge `-0.021` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.5964` n `182` status `ready` deltaP `-5.1361` edge `0.0513` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9613` n `182` status `ready` deltaP `-0.8443` edge `-0.1589` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

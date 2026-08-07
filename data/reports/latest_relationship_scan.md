# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T03:37:19.008955+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11765`

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

- `market_context_high->commodity_4h` score `1.2169` n `120` status `ready` deltaP `13.7906` edge `0.0941` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8644` n `109` status `ready` deltaP `3.7004` edge `0.1642` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5753` n `109` status `ready` deltaP `21.4854` edge `0.0511` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.5063` n `120` status `ready` deltaP `8.0988` edge `0.0298` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0234` n `120` status `ready` deltaP `6.3024` edge `-0.004` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2921` n `120` status `ready` deltaP `6.9817` edge `0.002` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5389` n `120` status `ready` deltaP `-1.9261` edge `-0.0068` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7871` n `120` status `ready` deltaP `-3.1437` edge `-0.0089` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9677` n `120` status `ready` deltaP `-2.0758` edge `-0.0134` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.1112` n `109` status `ready` deltaP `-1.0461` edge `0.084` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2875` n `120` status `ready` deltaP `4.0968` edge `-0.0359` maxDD `-10.5179`
- `market_context_high->metal_4h` score `-1.4116` n `120` status `ready` deltaP `0.3354` edge `0.0036` maxDD `-3.211`
- `market_context_high->index_4h` score `-1.5462` n `120` status `ready` deltaP `-6.1484` edge `-0.0318` maxDD `-4.7021`
- `market_context_high->unknown_24h` score `-1.6278` n `109` status `ready` deltaP `3.7571` edge `-0.1564` maxDD `-0.0104`
- `market_context_high->crypto_alt_4h` score `-1.872` n `120` status `ready` deltaP `2.1138` edge `-0.0311` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.5926` n `120` status `ready` deltaP `-6.4521` edge `-0.0357` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.5061` n `109` status `ready` deltaP `-8.6505` edge `-0.0902` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8369` n `120` status `ready` deltaP `0.8028` edge `-0.2248` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3384` n `109` status `ready` deltaP `9.8099` edge `-0.0015` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.1845` n `120` status `ready` deltaP `-5.7317` edge `-0.1393` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

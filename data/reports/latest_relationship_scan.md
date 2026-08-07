# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T01:52:29.034708+00:00`
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

- `market_context_high->unknown_24h` score `14.2158` n `109` status `ready` deltaP `3.7571` edge `1.1639` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.2143` n `120` status `ready` deltaP `13.6382` edge `0.0949` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8992` n `109` status `ready` deltaP `3.7004` edge `0.1671` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5668` n `109` status `ready` deltaP `21.4854` edge `0.05` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.5194` n `120` status `ready` deltaP `8.2485` edge `0.0299` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0312` n `120` status `ready` deltaP `6.4521` edge `-0.004` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3663` n `120` status `ready` deltaP `5.9146` edge `-0.0004` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.535` n `120` status `ready` deltaP `-1.9261` edge `-0.0063` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7918` n `120` status `ready` deltaP `-3.1437` edge `-0.0095` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9689` n `120` status `ready` deltaP `-2.0758` edge `-0.0135` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.1938` n `109` status `ready` deltaP `-2.2147` edge `0.0812` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2851` n `120` status `ready` deltaP `4.0968` edge `-0.0356` maxDD `-10.5179`
- `market_context_high->metal_4h` score `-1.2951` n `120` status `ready` deltaP `1.4024` edge `0.0062` maxDD `-3.211`
- `market_context_high->index_4h` score `-1.643` n `120` status `ready` deltaP `-7.2155` edge `-0.0371` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.838` n `120` status `ready` deltaP `2.4187` edge `-0.0303` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6477` n `120` status `ready` deltaP `-6.9012` edge `-0.0373` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.2314` n `109` status `ready` deltaP `-7.4818` edge `-0.0751` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.9635` n `120` status `ready` deltaP `0.4979` edge `-0.239` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3298` n `109` status `ready` deltaP `9.8099` edge `-0.0004` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2257` n `120` status `ready` deltaP `-6.0366` edge `-0.1407` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

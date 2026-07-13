# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T15:52:28.978189+00:00`
- Price records: `672`
- Market context records: `6617`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_24h` score `3.1633` n `175` status `ready` deltaP `0.8413` edge `0.5312` maxDD `-12.5228`
- `market_context_high->unknown_1h` score `2.1262` n `204` status `ready` deltaP `-6.1671` edge `0.3084` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.181` n `175` status `ready` deltaP `7.6352` edge `0.151` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2014` n `204` status `ready` deltaP `7.1768` edge `0.0268` maxDD `-4.704`
- `market_context_high->fx_1h` score `-0.2559` n `204` status `ready` deltaP `2.5977` edge `0.0006` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.576` n `204` status `ready` deltaP `-0.7632` edge `0.0032` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5856` n `204` status `ready` deltaP `-0.3111` edge `-0.0047` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5933` n `204` status `ready` deltaP `4.4264` edge `0.0183` maxDD `-3.7803`
- `market_context_high->index_4h` score `-0.8764` n `204` status `ready` deltaP `9.9025` edge `0.0096` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.112` n `204` status `ready` deltaP `1.8933` edge `-0.0014` maxDD `-3.978`
- `market_context_high->commodity_4h` score `-1.2363` n `204` status `ready` deltaP `-0.3348` edge `-0.0068` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.2476` n `204` status `ready` deltaP `-4.0184` edge `-0.0016` maxDD `-1.7126`
- `market_context_high->unknown_4h` score `-1.4198` n `204` status `ready` deltaP `-17.5275` edge `0.2391` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.592` n `204` status `ready` deltaP `8.3333` edge `0.0718` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.6097` n `204` status `ready` deltaP `2.3613` edge `-0.0009` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.9906` n `204` status `ready` deltaP `5.1859` edge `0.0504` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.115` n `204` status `ready` deltaP `-0.81` edge `0.0203` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.0143` n `204` status `ready` deltaP `8.2885` edge `-0.0148` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-4.0243` n `175` status `ready` deltaP `-1.4751` edge `0.0475` maxDD `-14.2886`
- `market_context_high->fx_24h` score `-5.7673` n `175` status `ready` deltaP `-7.5304` edge `-0.0013` maxDD `-9.3282`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T06:52:25.332577+00:00`
- Price records: `672`
- Market context records: `2740`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `market_context_high->crypto_alt_24h` score `10.9543` n `111` status `ready` deltaP `16.3523` edge `1.1532` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.4366` n `111` status `ready` deltaP `17.3048` edge `0.6205` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.4053` n `111` status `ready` deltaP `6.5175` edge `0.893` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.1707` n `143` status `ready` deltaP `7.4685` edge `0.1531` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0964` n `143` status `ready` deltaP `10.2465` edge `0.0282` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1028` n `143` status `ready` deltaP `3.3479` edge `0.0422` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1955` n `143` status `ready` deltaP `2.6015` edge `0.007` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5087` n `143` status `ready` deltaP `-0.1978` edge `0.0033` maxDD `-0.2164`
- `market_context_high->crypto_alt_4h` score `-0.5781` n `143` status `ready` deltaP `16.5157` edge `0.2758` maxDD `-28.7261`
- `market_context_high->commodity_1h` score `-0.5943` n `143` status `ready` deltaP `0.2021` edge `-0.0022` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6196` n `143` status `ready` deltaP `6.1451` edge `0.0556` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7645` n `143` status `ready` deltaP `-1.25` edge `-0.0051` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9549` n `143` status `ready` deltaP `3.6473` edge `0.0402` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0749` n `143` status `ready` deltaP `-3.0307` edge `0.0085` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2285` n `111` status `ready` deltaP `-0.1173` edge `-0.0144` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.3454` n `143` status `ready` deltaP `-5.2834` edge `0.0064` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.5158` n `143` status `ready` deltaP `0.4467` edge `-0.0053` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.7322` n `111` status `ready` deltaP `2.5807` edge `0.0701` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0531` n `143` status `ready` deltaP `-1.2493` edge `-0.0248` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.2741` n `143` status `ready` deltaP `6.9046` edge `0.153` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

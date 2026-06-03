# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T05:15:43.762458+00:00`
- Price records: `672`
- Market context records: `2733`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `11.3623` n `111` status `ready` deltaP `16.3523` edge `1.1872` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5782` n `111` status `ready` deltaP `17.3048` edge `0.6323` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.3874` n `111` status `ready` deltaP `6.5175` edge `0.8907` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.2614` n `143` status `ready` deltaP `8.0782` edge `0.1566` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0538` n `143` status `ready` deltaP `9.6367` edge `0.0268` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1471` n `143` status `ready` deltaP `3.0485` edge `0.0405` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1861` n `143` status `ready` deltaP `2.7512` edge `0.0072` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.3581` n `143` status `ready` deltaP `16.8206` edge `0.2921` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.4943` n `143` status `ready` deltaP `-0.0481` edge `0.0035` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5475` n `143` status `ready` deltaP `0.8009` edge `-0.0002` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.5853` n `143` status `ready` deltaP `6.1451` edge `0.06` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7473` n `143` status `ready` deltaP `-1.25` edge `-0.0029` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9378` n `143` status `ready` deltaP `3.6473` edge `0.0424` maxDD `-9.622`
- `market_context_high->fx_4h` score `-0.9922` n `143` status `ready` deltaP `-2.1161` edge `0.0093` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.1199` n `111` status `ready` deltaP `0.9244` edge `-0.0123` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.319` n `143` status `ready` deltaP `-4.984` edge `0.0066` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.4083` n `143` status `ready` deltaP `1.2089` edge `0.0034` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.6558` n `111` status `ready` deltaP `2.5807` edge `0.0799` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0819` n `143` status `ready` deltaP `-1.2493` edge `-0.0272` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.2296` n `143` status `ready` deltaP `6.9046` edge `0.1587` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

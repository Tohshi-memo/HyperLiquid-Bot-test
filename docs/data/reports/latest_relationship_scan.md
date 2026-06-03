# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T05:07:24.352204+00:00`
- Price records: `672`
- Market context records: `2732`
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

- `market_context_high->crypto_alt_24h` score `11.4019` n `111` status `ready` deltaP `16.3523` edge `1.1905` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5926` n `111` status `ready` deltaP `17.3048` edge `0.6335` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.3726` n `111` status `ready` deltaP `6.5175` edge `0.8888` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.2276` n `143` status `ready` deltaP `7.9258` edge `0.1548` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0522` n `143` status `ready` deltaP `9.6367` edge `0.0266` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1171` n `143` status `ready` deltaP `3.0485` edge `0.043` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1775` n `143` status `ready` deltaP `2.9009` edge `0.0073` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.3377` n `143` status `ready` deltaP `16.8206` edge `0.2938` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.5075` n `143` status `ready` deltaP `-0.1978` edge `0.0034` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5467` n `143` status `ready` deltaP `0.8009` edge `-0.0001` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.565` n `143` status `ready` deltaP `6.1451` edge `0.0626` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7419` n `143` status `ready` deltaP `-1.25` edge `-0.0022` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9229` n `143` status `ready` deltaP `3.6473` edge `0.0443` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0043` n `143` status `ready` deltaP `-2.2685` edge `0.0093` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.1036` n `111` status `ready` deltaP `1.098` edge `-0.0121` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.3011` n `143` status `ready` deltaP `-4.8343` edge `0.0071` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.3974` n `143` status `ready` deltaP `1.2089` edge `0.0048` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.6464` n `111` status `ready` deltaP `2.5807` edge `0.0811` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0831` n `143` status `ready` deltaP `-1.2493` edge `-0.0273` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.2273` n `143` status `ready` deltaP `6.9046` edge `0.159` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

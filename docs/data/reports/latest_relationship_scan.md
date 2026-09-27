# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T03:22:26.697162+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11492`

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

- `news_risk_high->unknown_24h` score `2578.266` n `105` status `ready` deltaP `1.2153` edge `214.8474` maxDD `0.0`
- `market_context_high->unknown_1h` score `77.2395` n `44` status `ready` deltaP `10.1524` edge `6.3736` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `51.6974` n `44` status `ready` deltaP `28.8037` edge `4.1512` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.9186` n `44` status `ready` deltaP `14.9148` edge `2.2651` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.7984` n `44` status `ready` deltaP `36.0954` edge `2.1073` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7807` n `44` status `ready` deltaP `32.6231` edge `0.4397` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.7725` n `44` status `ready` deltaP `33.0019` edge `0.1182` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.3202` n `44` status `ready` deltaP `37.2228` edge `0.0356` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.9153` n `44` status `ready` deltaP `17.5166` edge `0.1638` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.2292` n `44` status `ready` deltaP `8.8553` edge `0.106` maxDD `-3.3417`
- `market_context_high->crypto_major_1h` score `1.0508` n `44` status `ready` deltaP `8.8187` edge `0.1022` maxDD `-4.5405`
- `market_context_high->equity_1h` score `1.0359` n `44` status `ready` deltaP `11.7175` edge `0.0485` maxDD `-1.5564`
- `news_risk_high->index_24h` score `0.9314` n `105` status `ready` deltaP `14.8958` edge `0.0395` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.9004` n `105` status `ready` deltaP `22.3959` edge `0.1309` maxDD `-6.8481`
- `market_context_high->crypto_major_4h` score `0.862` n `44` status `ready` deltaP `6.7628` edge `0.1172` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.7745` n `44` status `ready` deltaP `11.8672` edge `0.0091` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.2575` n `44` status `ready` deltaP `6.3146` edge `0.011` maxDD `-0.1976`
- `market_context_high->fx_1h` score `0.1469` n `44` status `ready` deltaP `7.2128` edge `0.0064` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `0.0103` n `44` status `ready` deltaP `4.0011` edge `0.0631` maxDD `-5.7799`
- `news_risk_high->index_1h` score `-0.1287` n `142` status `ready` deltaP `2.2961` edge `0.0031` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T16:07:37.899918+00:00`
- Price records: `672`
- Market context records: `8107`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11809`

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

- `market_context_high->equity_24h` score `21.2305` n `87` status `ready` deltaP `38.4649` edge `1.6038` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.9845` n `87` status `ready` deltaP `33.64` edge `0.5724` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.4008` n `87` status `ready` deltaP `35.8752` edge `0.4609` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8638` n `43` status `ready` deltaP `31.2075` edge `0.4678` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.0313` n `43` status `ready` deltaP `15.6126` edge `0.2924` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.7919` n `43` status `ready` deltaP `29.5293` edge `0.15` maxDD `-1.1366`
- `market_context_high->index_4h` score `3.4267` n `87` status `ready` deltaP `32.0455` edge `0.0907` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.3572` n `87` status `ready` deltaP `21.4785` edge `0.2036` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.8595` n `43` status `ready` deltaP `5.2047` edge `0.2314` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.6007` n `88` status `ready` deltaP `15.1266` edge `0.1592` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.4767` n `43` status `ready` deltaP `21.4868` edge `0.0822` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.4224` n `87` status `ready` deltaP `22.2158` edge `0.116` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.9769` n `87` status `ready` deltaP `27.389` edge `0.0525` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.5315` n `87` status `ready` deltaP `8.3158` edge `0.1839` maxDD `-3.9374`
- `news_risk_high->metal_4h` score `1.3219` n `43` status `ready` deltaP `13.8223` edge `0.0648` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2602` n `88` status `ready` deltaP `16.1473` edge `0.0241` maxDD `-0.4716`
- `market_context_high->crypto_major_4h` score `1.2571` n `87` status `ready` deltaP `10.2397` edge `0.2083` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.0753` n `87` status `ready` deltaP `28.7854` edge `0.2345` maxDD `-15.7497`
- `news_risk_high->crypto_major_1h` score `0.9782` n `43` status `ready` deltaP `4.0872` edge `0.094` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.889` n `88` status `ready` deltaP `12.2278` edge `0.0304` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

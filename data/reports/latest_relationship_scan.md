# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T17:13:47.860222+00:00`
- Price records: `672`
- Market context records: `8112`
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

- `market_context_high->equity_24h` score `21.6603` n `87` status `ready` deltaP `39.1582` edge `1.635` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.1081` n `87` status `ready` deltaP `33.64` edge `0.5827` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.4332` n `87` status `ready` deltaP `35.8752` edge `0.4636` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.9874` n `43` status `ready` deltaP `31.2075` edge `0.4781` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.1301` n `43` status `ready` deltaP `15.9175` edge `0.2986` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.7823` n `43` status `ready` deltaP `29.5293` edge `0.1492` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.4882` n `87` status `ready` deltaP `22.1717` edge `0.2099` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.4555` n `87` status `ready` deltaP `32.0455` edge `0.0931` maxDD `-0.5022`
- `news_risk_high->unknown_1h` score `2.8356` n `43` status `ready` deltaP `5.055` edge `0.2304` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.5911` n `88` status `ready` deltaP `15.1266` edge `0.1584` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.5055` n `43` status `ready` deltaP `21.4868` edge `0.0846` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.386` n `87` status `ready` deltaP `21.9109` edge `0.115` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.9895` n `87` status `ready` deltaP `27.5623` edge `0.0524` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.6894` n `87` status `ready` deltaP `8.9256` edge `0.193` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.3559` n `87` status `ready` deltaP `10.5446` edge `0.2145` maxDD `-6.7444`
- `news_risk_high->metal_4h` score `1.2855` n `43` status `ready` deltaP `13.5174` edge `0.0638` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2614` n `88` status `ready` deltaP `16.1473` edge `0.0242` maxDD `-0.4716`
- `market_context_high->commodity_24h` score `1.1777` n `87` status `ready` deltaP `29.4786` edge `0.243` maxDD `-15.7497`
- `news_risk_high->crypto_major_1h` score `0.9926` n `43` status `ready` deltaP `4.2369` edge `0.0942` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.8734` n `88` status `ready` deltaP `12.0781` edge `0.0301` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

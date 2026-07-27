# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T17:22:35.096600+00:00`
- Price records: `672`
- Market context records: `8113`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11825`

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

- `market_context_high->equity_24h` score `21.769` n `87` status `ready` deltaP `39.3315` edge `1.6429` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.1309` n `87` status `ready` deltaP `33.64` edge `0.5846` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.4428` n `87` status `ready` deltaP `35.8752` edge `0.4644` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.0102` n `43` status `ready` deltaP `31.2075` edge `0.48` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.1373` n `43` status `ready` deltaP `15.9175` edge `0.2992` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.7643` n `43` status `ready` deltaP `29.3796` edge `0.1487` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.5201` n `87` status `ready` deltaP `22.345` edge `0.2114` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.4615` n `87` status `ready` deltaP `32.0455` edge `0.0936` maxDD `-0.5022`
- `news_risk_high->unknown_1h` score `2.8296` n `43` status `ready` deltaP `5.055` edge `0.2299` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.5731` n `88` status `ready` deltaP `14.9769` edge `0.1579` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.5115` n `43` status `ready` deltaP `21.4868` edge `0.0851` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.3848` n `87` status `ready` deltaP `21.9109` edge `0.1149` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.0034` n `87` status `ready` deltaP `27.7356` edge `0.0524` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.722` n `87` status `ready` deltaP `9.078` edge `0.1947` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.3631` n `87` status `ready` deltaP `10.5446` edge `0.2151` maxDD `-6.7444`
- `news_risk_high->metal_4h` score `1.2843` n `43` status `ready` deltaP `13.5174` edge `0.0637` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2602` n `88` status `ready` deltaP `16.1473` edge `0.0241` maxDD `-0.4716`
- `market_context_high->commodity_24h` score `1.2039` n `87` status `ready` deltaP `29.6519` edge `0.2452` maxDD `-15.7497`
- `news_risk_high->crypto_major_1h` score `0.9662` n `43` status `ready` deltaP `4.0872` edge `0.093` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.8746` n `88` status `ready` deltaP `12.0781` edge `0.0302` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

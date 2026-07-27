# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T18:07:27.608282+00:00`
- Price records: `672`
- Market context records: `8116`
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

- `market_context_high->equity_24h` score `22.0687` n `87` status `ready` deltaP `39.7629` edge `1.665` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.1813` n `87` status `ready` deltaP `33.64` edge `0.5888` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.4802` n `87` status `ready` deltaP `35.9375` edge `0.4671` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.0606` n `43` status `ready` deltaP `31.2075` edge `0.4842` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.1985` n `43` status `ready` deltaP `15.9175` edge `0.3043` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.7691` n `43` status `ready` deltaP `29.3796` edge `0.1491` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.6069` n `87` status `ready` deltaP `22.7849` edge `0.2157` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.4735` n `87` status `ready` deltaP `32.0455` edge `0.0946` maxDD `-0.5022`
- `news_risk_high->unknown_1h` score `2.8703` n `43` status `ready` deltaP `5.3544` edge `0.2313` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.5779` n `88` status `ready` deltaP `14.9769` edge `0.1583` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.5235` n `43` status `ready` deltaP `21.4868` edge `0.0861` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.3702` n `87` status `ready` deltaP `21.7585` edge `0.1147` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.0422` n `87` status `ready` deltaP `28.1908` edge `0.0526` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.8402` n `87` status `ready` deltaP `9.5353` edge `0.2015` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.4243` n `87` status `ready` deltaP `10.5446` edge `0.2202` maxDD `-6.7444`
- `news_risk_high->metal_4h` score `1.2697` n `43` status `ready` deltaP `13.365` edge `0.0635` maxDD `-0.7433`
- `market_context_high->commodity_24h` score `1.2674` n `87` status `ready` deltaP `30.0945` edge `0.2504` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.259` n `88` status `ready` deltaP `16.1473` edge `0.024` maxDD `-0.4716`
- `news_risk_high->crypto_major_1h` score `0.9782` n `43` status `ready` deltaP `4.2369` edge `0.093` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.865` n `88` status `ready` deltaP `11.9284` edge `0.0304` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

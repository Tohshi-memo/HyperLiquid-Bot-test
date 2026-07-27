# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T11:22:27.343875+00:00`
- Price records: `672`
- Market context records: `8086`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.2885` n `87` status `ready` deltaP `36.9051` edge `1.5357` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.4106` n `87` status `ready` deltaP `32.4205` edge `0.5327` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2712` n `87` status `ready` deltaP `35.8752` edge `0.4501` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8631` n `42` status `ready` deltaP `32.0921` edge `0.4518` maxDD `-0.1727`
- `news_risk_high->crypto_major_4h` score `3.635` n `42` status `ready` deltaP `15.3891` edge `0.2554` maxDD `-2.0729`
- `news_risk_high->equity_1h` score `3.4858` n `43` status `ready` deltaP `28.4814` edge `0.1322` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.3061` n `87` status `ready` deltaP `31.5881` edge `0.0837` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0721` n `87` status `ready` deltaP `19.7454` edge `0.1914` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7625` n `43` status `ready` deltaP `4.4562` edge `0.2282` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.5507` n `42` status `ready` deltaP `22.9674` edge `0.0785` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.4006` n `87` status `ready` deltaP `14.8754` edge `0.1442` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.2756` n `87` status `ready` deltaP `30.5085` edge `0.0566` maxDD `-0.6283`
- `market_context_high->metal_4h` score `2.2719` n `87` status `ready` deltaP `20.8438` edge `0.1126` maxDD `-0.979`
- `news_risk_high->metal_4h` score `1.3498` n `42` status `ready` deltaP `14.1115` edge `0.0652` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.1721` n `87` status `ready` deltaP `15.4209` edge `0.0216` maxDD `-0.4716`
- `market_context_high->crypto_alt_4h` score `0.7901` n `87` status `ready` deltaP `5.7244` edge `0.1394` maxDD `-3.9374`
- `market_context_high->metal_1h` score `0.7715` n `87` status `ready` deltaP `10.9247` edge `0.0293` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.7108` n `43` status `ready` deltaP `3.189` edge `0.0777` maxDD `-1.1783`
- `market_context_high->commodity_24h` score `0.6467` n `87` status `ready` deltaP `25.4925` edge `0.2015` maxDD `-15.7497`
- `market_context_high->crypto_major_4h` score `0.5612` n `87` status `ready` deltaP `8.4105` edge `0.1625` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T18:37:27.972416+00:00`
- Price records: `672`
- Market context records: `8118`
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

- `market_context_high->equity_24h` score `22.3053` n `87` status `ready` deltaP `40.1102` edge `1.6824` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.1451` n `87` status `ready` deltaP `33.4875` edge `0.5868` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.4994` n `87` status `ready` deltaP `35.9375` edge `0.4687` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.0244` n `43` status `ready` deltaP `31.055` edge `0.4822` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.2287` n `43` status `ready` deltaP `16.0699` edge `0.3058` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.7703` n `43` status `ready` deltaP `29.3796` edge `0.1492` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.6767` n `87` status `ready` deltaP `23.1322` edge `0.2192` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.4723` n `87` status `ready` deltaP `32.0455` edge `0.0945` maxDD `-0.5022`
- `news_risk_high->unknown_1h` score `2.8919` n `43` status `ready` deltaP `5.5041` edge `0.2321` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.5791` n `88` status `ready` deltaP `14.9769` edge `0.1584` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.5223` n `43` status `ready` deltaP `21.4868` edge `0.086` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.3532` n `87` status `ready` deltaP `21.606` edge `0.1143` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.0573` n `87` status `ready` deltaP `28.3644` edge `0.0527` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.8764` n `87` status `ready` deltaP `9.6878` edge `0.2035` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.4545` n `87` status `ready` deltaP `10.697` edge `0.2217` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.319` n `87` status `ready` deltaP `30.4418` edge `0.2547` maxDD `-15.7497`
- `news_risk_high->metal_4h` score `1.2527` n `43` status `ready` deltaP `13.2125` edge `0.0631` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2447` n `88` status `ready` deltaP `15.9976` edge `0.0238` maxDD `-0.4716`
- `news_risk_high->crypto_major_1h` score `1.0322` n `43` status `ready` deltaP `4.5363` edge `0.0955` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.8638` n `88` status `ready` deltaP `11.9284` edge `0.0303` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

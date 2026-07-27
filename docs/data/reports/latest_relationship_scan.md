# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T09:22:30.974444+00:00`
- Price records: `672`
- Market context records: `8078`
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

- `market_context_high->equity_24h` score `20.1872` n `85` status `ready` deltaP `36.6887` edge `1.5287` maxDD `-4.9489`
- `news_risk_high->equity_4h` score `8.7959` n `34` status `ready` deltaP `35.7335` edge `0.4994` maxDD `-0.037`
- `market_context_high->equity_4h` score `8.3878` n `87` status `ready` deltaP `32.4205` edge `0.5308` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.264` n `85` status `ready` deltaP `35.8752` edge `0.4495` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.9968` n `34` status `ready` deltaP `27.7797` edge `0.3495` maxDD `-0.7975`
- `news_risk_high->equity_1h` score `3.3912` n `42` status `ready` deltaP `27.6447` edge `0.1299` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2929` n `87` status `ready` deltaP `31.5881` edge `0.0826` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.9993` n `85` status `ready` deltaP `19.0152` edge `0.1902` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7572` n `42` status `ready` deltaP `2.8443` edge `0.2385` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.5911` n `34` status `ready` deltaP `21.987` edge `0.0884` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.38` n `87` status `ready` deltaP `21.9109` edge `0.1145` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.3313` n `85` status `ready` deltaP `31.0837` edge `0.0574` maxDD `-0.6283`
- `market_context_high->equity_1h` score `2.3263` n `87` status `ready` deltaP `14.4263` edge `0.141` maxDD `-2.1322`
- `news_risk_high->crypto_alt_4h` score `1.8872` n `34` status `ready` deltaP `19.566` edge `0.1732` maxDD `-2.6022`
- `news_risk_high->fx_4h` score `1.6781` n `34` status `ready` deltaP `22.6327` edge `0.0196` maxDD `-0.1179`
- `news_risk_high->metal_4h` score `1.1639` n `34` status `ready` deltaP `11.3971` edge `0.0678` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.1278` n `87` status `ready` deltaP `14.9718` edge `0.0209` maxDD `-0.4716`
- `market_context_high->commodity_24h` score `0.9228` n `85` status `ready` deltaP `25.864` edge `0.2092` maxDD `-14.3993`
- `market_context_high->metal_1h` score `0.7715` n `87` status `ready` deltaP `10.9247` edge `0.0293` maxDD `-0.6936`
- `market_context_high->crypto_alt_4h` score `0.5764` n `87` status `ready` deltaP `4.6573` edge `0.1287` maxDD `-3.9374`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

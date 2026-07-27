# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T08:22:29.001284+00:00`
- Price records: `672`
- Market context records: `8073`
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

- `market_context_high->equity_24h` score `20.1092` n `82` status `ready` deltaP `36.3444` edge `1.5245` maxDD `-4.9489`
- `news_risk_high->equity_4h` score `8.7176` n `30` status `ready` deltaP `34.9492` edge `0.4981` maxDD `-0.037`
- `market_context_high->equity_4h` score `8.3662` n `87` status `ready` deltaP `32.4205` edge `0.529` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2748` n `82` status `ready` deltaP `35.8752` edge `0.4504` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `7.8851` n `30` status `ready` deltaP `38.1504` edge `0.4134` maxDD `-0.1847`
- `news_risk_high->crypto_alt_4h` score `5.1106` n `30` status `ready` deltaP `28.7601` edge `0.2553` maxDD `-0.6922`
- `news_risk_high->equity_1h` score `3.4475` n `42` status `ready` deltaP `28.2435` edge `0.1306` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2857` n `87` status `ready` deltaP `31.5881` edge `0.082` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.8859` n `82` status `ready` deltaP `17.8531` edge `0.1885` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.726` n `42` status `ready` deltaP `2.5449` edge `0.2379` maxDD `-0.8826`
- `market_context_high->commodity_24h` score `2.6456` n `82` status `ready` deltaP `28.4884` edge `0.247` maxDD `-11.6496`
- `market_context_high->metal_4h` score `2.414` n `87` status `ready` deltaP `22.2158` edge `0.1153` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.3957` n `30` status `ready` deltaP `19.6341` edge `0.0878` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.3826` n `87` status `ready` deltaP `15.0251` edge `0.1417` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.257` n `82` status `ready` deltaP `30.4857` edge `0.0552` maxDD `-0.6283`
- `news_risk_high->fx_4h` score `1.6277` n `30` status `ready` deltaP `21.7174` edge `0.0215` maxDD `-0.1179`
- `market_context_high->index_1h` score `1.1422` n `87` status `ready` deltaP `15.1215` edge `0.0211` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.7871` n `87` status `ready` deltaP `11.0744` edge `0.0296` maxDD `-0.6936`
- `news_risk_high->metal_4h` score `0.7448` n `30` status `ready` deltaP `7.3882` edge `0.0596` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `0.5154` n `42` status `ready` deltaP `1.7822` edge `0.0708` maxDD `-1.1783`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

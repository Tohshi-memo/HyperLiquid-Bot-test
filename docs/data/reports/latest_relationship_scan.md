# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T10:22:29.238865+00:00`
- Price records: `672`
- Market context records: `8082`
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

- `market_context_high->equity_24h` score `20.2487` n `86` status `ready` deltaP `36.7982` edge `1.5331` maxDD `-4.9489`
- `news_risk_high->equity_4h` score `8.7759` n `38` status `ready` deltaP `36.3527` edge `0.4936` maxDD `-0.037`
- `market_context_high->equity_4h` score `8.4106` n `87` status `ready` deltaP `32.4205` edge `0.5327` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2652` n `86` status `ready` deltaP `35.8752` edge `0.4496` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `4.8764` n `38` status `ready` deltaP `22.1999` edge `0.3006` maxDD `-1.3785`
- `news_risk_high->equity_1h` score `3.4258` n `43` status `ready` deltaP `28.0323` edge `0.1302` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.3001` n `87` status `ready` deltaP `31.5881` edge `0.0832` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0373` n `86` status `ready` deltaP `19.3846` edge `0.1909` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.723` n `43` status `ready` deltaP `4.0071` edge `0.2279` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.6905` n `38` status `ready` deltaP `23.8446` edge `0.0843` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.3407` n `87` status `ready` deltaP `14.4263` edge `0.1422` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.3168` n `87` status `ready` deltaP `21.3011` edge `0.1133` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.3038` n `86` status `ready` deltaP `30.8009` edge `0.057` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.4259` n `38` status `ready` deltaP `14.1928` edge `0.071` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.1326` n `87` status `ready` deltaP `14.9718` edge `0.0213` maxDD `-0.4716`
- `news_risk_high->fx_4h` score `1.0936` n `38` status `ready` deltaP `15.8215` edge `0.0163` maxDD `-0.1179`
- `market_context_high->metal_1h` score `0.7847` n `87` status `ready` deltaP `11.0744` edge `0.0294` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `0.7803` n `86` status `ready` deltaP `25.6681` edge `0.205` maxDD `-15.0865`
- `news_risk_high->crypto_alt_4h` score `0.768` n `38` status `ready` deltaP `12.4358` edge `0.1152` maxDD `-4.3051`
- `market_context_high->crypto_alt_4h` score `0.7151` n `87` status `ready` deltaP `5.267` edge `0.1362` maxDD `-3.9374`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

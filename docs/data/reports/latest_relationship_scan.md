# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T10:52:24.561244+00:00`
- Price records: `672`
- Market context records: `8084`
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

- `market_context_high->equity_24h` score `20.2657` n `87` status `ready` deltaP `36.9051` edge `1.5338` maxDD `-4.9489`
- `news_risk_high->equity_4h` score `8.6107` n `40` status `ready` deltaP `36.4634` edge `0.4791` maxDD `-0.037`
- `market_context_high->equity_4h` score `8.4056` n `87` status `ready` deltaP `32.268` edge `0.5333` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2604` n `87` status `ready` deltaP `35.8752` edge `0.4492` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `4.2449` n `40` status `ready` deltaP `18.689` edge `0.2764` maxDD `-1.78`
- `news_risk_high->equity_1h` score `3.4438` n `43` status `ready` deltaP `28.182` edge `0.1307` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.3049` n `87` status `ready` deltaP `31.5881` edge `0.0836` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0661` n `87` status `ready` deltaP `19.7454` edge `0.1909` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7481` n `43` status `ready` deltaP `4.3065` edge `0.228` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.7273` n `40` status `ready` deltaP `24.6341` edge `0.0821` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.3586` n `87` status `ready` deltaP `14.576` edge `0.1427` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.3106` n `87` status `ready` deltaP `30.8552` edge `0.0572` maxDD `-0.6283`
- `market_context_high->metal_4h` score `2.2877` n `87` status `ready` deltaP `20.9963` edge `0.1129` maxDD `-0.979`
- `news_risk_high->metal_4h` score `1.5197` n `40` status `ready` deltaP `15.3354` edge `0.0712` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.1446` n `87` status `ready` deltaP `15.1215` edge `0.0213` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.7715` n `87` status `ready` deltaP `10.9247` edge `0.0293` maxDD `-0.6936`
- `market_context_high->crypto_alt_4h` score `0.7659` n `87` status `ready` deltaP `5.5719` edge `0.1384` maxDD `-3.9374`
- `news_risk_high->crypto_major_1h` score `0.694` n `43` status `ready` deltaP `3.0393` edge `0.0773` maxDD `-1.1783`
- `market_context_high->commodity_24h` score `0.6022` n `87` status `ready` deltaP `25.1459` edge `0.1981` maxDD `-15.7497`
- `market_context_high->crypto_major_4h` score `0.549` n `87` status `ready` deltaP `8.258` edge `0.1625` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T02:52:31.233823+00:00`
- Price records: `672`
- Market context records: `8155`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `21.7939` n `75` status `ready` deltaP `44.368` edge `1.6114` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0281` n `76` status `ready` deltaP `37.476` edge `0.6093` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.7057` n `75` status `ready` deltaP `39.2361` edge `0.4639` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.4881` n `43` status `ready` deltaP `32.427` edge `0.5117` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `5.1986` n `43` status `ready` deltaP `19.1187` edge `0.3663` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9662` n `76` status `ready` deltaP `35.8953` edge `0.0955` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.9361` n `76` status `ready` deltaP `20.8084` edge `0.2096` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.8243` n `43` status `ready` deltaP `29.5293` edge `0.1527` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.6837` n `75` status `ready` deltaP `23.8958` edge `0.2147` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.6965` n `43` status `ready` deltaP `22.5538` edge `0.0934` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.5201` n `76` status `ready` deltaP `23.9169` edge `0.1128` maxDD `-0.979`
- `market_context_high->crypto_alt_4h` score `2.261` n `76` status `ready` deltaP `10.085` edge `0.2329` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `2.1078` n `76` status `ready` deltaP `12.2031` edge `0.2661` maxDD `-6.7444`
- `market_context_high->fx_24h` score `2.0854` n `75` status `ready` deltaP `28.0556` edge `0.0571` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.7536` n `76` status `ready` deltaP `20.6035` edge `0.0284` maxDD `-0.2368`
- `market_context_high->commodity_24h` score `1.6796` n `75` status `ready` deltaP `32.125` edge `0.2897` maxDD `-15.7497`
- `market_context_high->crypto_major_1h` score `1.5272` n `76` status `ready` deltaP `14.387` edge `0.0724` maxDD `-1.6171`
- `news_risk_high->metal_4h` score `1.5235` n `43` status `ready` deltaP `14.7369` edge `0.0755` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.3031` n `43` status `ready` deltaP `6.0333` edge `0.1081` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.1547` n `76` status `ready` deltaP `15.0095` edge `0.034` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

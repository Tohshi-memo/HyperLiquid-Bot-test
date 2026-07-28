# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T02:22:35.953583+00:00`
- Price records: `672`
- Market context records: `8153`
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

- `market_context_high->equity_24h` score `22.4159` n `77` status `ready` deltaP `44.2979` edge `1.6637` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.1083` n `78` status `ready` deltaP `37.3397` edge `0.6169` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.8063` n `77` status `ready` deltaP `38.8889` edge `0.4746` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.3593` n `43` status `ready` deltaP `32.1221` edge `0.503` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `5.1034` n `43` status `ready` deltaP `18.8139` edge `0.3604` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9575` n `78` status `ready` deltaP `35.7255` edge `0.0959` maxDD `-0.0092`
- `market_context_high->index_24h` score `3.8184` n `77` status `ready` deltaP `24.4837` edge `0.222` maxDD `-1.3621`
- `market_context_high->equity_1h` score `3.8044` n `78` status `ready` deltaP `20.0177` edge `0.2039` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.7943` n `43` status `ready` deltaP `29.3796` edge `0.1512` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6541` n `43` status `ready` deltaP `22.249` edge `0.0919` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.5905` n `78` status `ready` deltaP `24.1518` edge `0.1171` maxDD `-0.979`
- `market_context_high->crypto_alt_4h` score `2.4697` n `78` status `ready` deltaP `10.8935` edge `0.2449` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `2.2604` n `78` status `ready` deltaP `12.9105` edge `0.2741` maxDD `-6.7444`
- `market_context_high->fx_24h` score `2.1311` n `77` status `ready` deltaP `28.7473` edge `0.0563` maxDD `-0.6283`
- `market_context_high->commodity_24h` score `1.7518` n `77` status `ready` deltaP `32.5397` edge `0.2962` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.6948` n `78` status `ready` deltaP `19.914` edge `0.0281` maxDD `-0.2368`
- `market_context_high->crypto_major_1h` score `1.4813` n `78` status `ready` deltaP `13.9337` edge `0.0716` maxDD `-1.6171`
- `news_risk_high->metal_4h` score `1.4739` n `43` status `ready` deltaP `14.432` edge `0.0734` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.2875` n `43` status `ready` deltaP `5.8836` edge `0.1078` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.2186` n `78` status `ready` deltaP `15.5535` edge `0.0357` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

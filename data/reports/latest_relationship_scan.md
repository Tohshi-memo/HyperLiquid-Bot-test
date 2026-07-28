# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T06:37:29.187866+00:00`
- Price records: `672`
- Market context records: `8170`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11746`

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

- `news_risk_high->unknown_24h` score `8585.995` n `39` status `ready` deltaP `37.1528` edge `715.2519` maxDD `0.0`
- `market_context_high->equity_24h` score `18.7769` n `60` status `ready` deltaP `44.3056` edge `1.3604` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.2428` n `61` status `ready` deltaP `38.1448` edge `0.5394` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `9.1931` n `43` status `ready` deltaP `34.7136` edge `0.5552` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.092` n `60` status `ready` deltaP `41.8403` edge `0.3954` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.5571` n `43` status `ready` deltaP `20.7956` edge `0.385` maxDD `-2.1767`
- `market_context_high->index_4h` score `4.0468` n `61` status `ready` deltaP `36.8877` edge `0.0956` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.5363` n `61` status `ready` deltaP `20.9262` edge `0.1755` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.2882` n `48` status `ready` deltaP `24.239` edge `0.1433` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.9574` n `43` status `ready` deltaP `24.8404` edge `0.0999` maxDD `-0.191`
- `news_risk_high->metal_4h` score `1.8516` n `43` status `ready` deltaP `17.0235` edge `0.0876` maxDD `-0.7433`
- `market_context_high->index_24h` score `1.8247` n `60` status `ready` deltaP `17.5` edge `0.1843` maxDD `-1.3621`
- `market_context_high->index_1h` score `1.8224` n `61` status `ready` deltaP `21.0906` edge `0.0251` maxDD `-0.1069`
- `market_context_high->metal_4h` score `1.6481` n `61` status `ready` deltaP `21.0266` edge `0.0594` maxDD `-0.979`
- `news_risk_high->crypto_major_1h` score `1.6163` n `48` status `ready` deltaP `9.6931` edge `0.1098` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.3909` n `48` status `ready` deltaP `10.5913` edge `0.0887` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.1761` n `43` status `ready` deltaP `12.8651` edge `0.2042` maxDD `-5.8012`
- `market_context_high->commodity_24h` score `0.9789` n `60` status `ready` deltaP `27.3958` edge `0.2314` maxDD `-15.7497`
- `market_context_high->fx_24h` score `0.9358` n `60` status `ready` deltaP `20.6597` edge `0.0526` maxDD `-0.6283`
- `market_context_high->metal_1h` score `0.5414` n `61` status `ready` deltaP `9.7575` edge `0.0179` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

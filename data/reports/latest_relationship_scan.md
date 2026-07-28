# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T00:52:31.851562+00:00`
- Price records: `672`
- Market context records: `8146`
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

- `market_context_high->equity_24h` score `23.8904` n `82` status `ready` deltaP `43.8897` edge `1.7893` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.1201` n `83` status `ready` deltaP `36.8113` edge `0.6214` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.8742` n `82` status `ready` deltaP `37.8472` edge `0.4872` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.9814` n `43` status `ready` deltaP `31.2075` edge `0.4776` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.735` n `43` status `ready` deltaP `17.8992` edge `0.3358` maxDD `-2.1767`
- `market_context_high->index_24h` score `4.1521` n `82` status `ready` deltaP `25.5801` edge `0.2425` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.9594` n `83` status `ready` deltaP `35.1197` edge `0.1001` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.6899` n `43` status `ready` deltaP `28.9305` edge `0.1455` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.2783` n `83` status `ready` deltaP `17.4988` edge `0.1868` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.651` n `83` status `ready` deltaP `24.4729` edge `0.12` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.5173` n `43` status `ready` deltaP `21.3343` edge `0.0866` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.49` n `83` status `ready` deltaP `12.5276` edge `0.2357` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `2.2406` n `83` status `ready` deltaP `14.3127` edge `0.2631` maxDD `-6.7444`
- `market_context_high->fx_24h` score `2.2235` n `82` status `ready` deltaP `30.0813` edge `0.0551` maxDD `-0.6283`
- `market_context_high->commodity_24h` score `1.8241` n `82` status `ready` deltaP `33.2401` edge `0.3008` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.7046` n `83` status `ready` deltaP `19.737` edge `0.0301` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.3335` n `43` status `ready` deltaP `13.5174` edge `0.0678` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.2504` n `43` status `ready` deltaP `5.7339` edge `0.1057` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0276` n `83` status `ready` deltaP `13.5705` edge `0.033` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.8073` n `83` status `ready` deltaP `12.4865` edge `0.0613` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

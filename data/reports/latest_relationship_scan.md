# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T07:07:32.428292+00:00`
- Price records: `672`
- Market context records: `8172`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8754.025` n `41` status `ready` deltaP `37.1528` edge `729.2544` maxDD `0.0`
- `market_context_high->equity_24h` score `18.8591` n `58` status `ready` deltaP `44.193` edge `1.368` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.2171` n `59` status `ready` deltaP `38.0193` edge `0.5381` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `9.1328` n `44` status `ready` deltaP `35.1303` edge `0.5474` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.079` n `58` status `ready` deltaP `42.1875` edge `0.392` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.5935` n `44` status `ready` deltaP `21.5355` edge `0.3831` maxDD `-2.1767`
- `market_context_high->index_4h` score `4.0473` n `59` status `ready` deltaP `36.8179` edge `0.0961` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.476` n `59` status `ready` deltaP `20.0371` edge `0.1764` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.376` n `50` status `ready` deltaP `25.1557` edge `0.1445` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.9962` n `44` status `ready` deltaP `25.4158` edge `0.0993` maxDD `-0.191`
- `news_risk_high->metal_4h` score `1.9042` n `44` status `ready` deltaP `17.7106` edge `0.0874` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.8271` n `50` status `ready` deltaP `11.4431` edge `0.1157` maxDD `-1.1783`
- `market_context_high->index_24h` score `1.7863` n `58` status `ready` deltaP `16.2955` edge `0.1874` maxDD `-1.3621`
- `market_context_high->index_1h` score `1.746` n `59` status `ready` deltaP `20.0903` edge `0.0254` maxDD `-0.1069`
- `news_risk_high->crypto_alt_1h` score `1.6125` n `50` status `ready` deltaP `12.1916` edge `0.0965` maxDD `-1.1388`
- `market_context_high->metal_4h` score `1.5433` n `59` status `ready` deltaP `20.1375` edge `0.0566` maxDD `-0.979`
- `news_risk_high->crypto_alt_4h` score `1.2623` n `44` status `ready` deltaP `13.8165` edge `0.2089` maxDD `-5.8012`
- `market_context_high->fx_24h` score `0.8619` n `58` status `ready` deltaP `19.2828` edge `0.0523` maxDD `-0.6283`
- `market_context_high->commodity_24h` score `0.8353` n `58` status `ready` deltaP `26.4787` edge `0.2191` maxDD `-15.7497`
- `news_risk_high->index_1h` score `0.6224` n `50` status `ready` deltaP `8.5988` edge `0.0234` maxDD `-0.3089`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

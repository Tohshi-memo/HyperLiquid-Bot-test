# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T08:31:56.878986+00:00`
- Price records: `672`
- Market context records: `2124`
- Flow alert records: `8011`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9149`

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

- `market_context_high->crypto_alt_4h` score `13.3085` n `158` status `ready` deltaP `37.226` edge `0.9545` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9418` n `158` status `ready` deltaP `41.5271` edge `0.7713` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.0605` n `158` status `ready` deltaP `24.203` edge `0.4186` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.1504` n `158` status `ready` deltaP `27.082` edge `0.3581` maxDD `-5.0894`
- `market_context_high->metal_4h` score `3.2065` n `158` status `ready` deltaP `22.0129` edge `0.2592` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.1393` n `158` status `ready` deltaP `22.6748` edge `0.1788` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `3.139` n `158` status `ready` deltaP `17.4354` edge `0.1975` maxDD `-2.1721`
- `market_context_high->index_24h` score `2.9961` n `157` status `ready` deltaP `12.6474` edge `0.2882` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.8764` n `158` status `ready` deltaP `14.7408` edge `0.2278` maxDD `-4.9097`
- `news_risk_high->unknown_1h` score `2.6841` n `33` status `ready` deltaP `29.8721` edge `0.0548` maxDD `-1.7548`
- `market_context_high->equity_24h` score `2.0358` n `157` status `ready` deltaP `24.0738` edge `0.499` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.5254` n `157` status `ready` deltaP `24.6083` edge `0.4951` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.23` n `157` status `ready` deltaP `20.4262` edge `0.8801` maxDD `-62.3533`
- `news_risk_high->commodity_1h` score `0.8054` n `33` status `ready` deltaP `7.8752` edge `0.0826` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7483` n `158` status `ready` deltaP `9.5695` edge `0.0774` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.5104` n `158` status `ready` deltaP `8.3434` edge `0.0539` maxDD `-2.3594`
- `market_context_high->unknown_1h` score `0.0765` n `158` status `ready` deltaP `5.0159` edge `0.0449` maxDD `-3.0902`
- `market_context_high->metal_24h` score `0.0246` n `157` status `ready` deltaP `10.5415` edge `0.323` maxDD `-23.2095`
- `market_context_high->index_1h` score `-0.0352` n `158` status `ready` deltaP `3.8865` edge `0.0302` maxDD `-1.3898`
- `news_risk_high->fx_1h` score `-0.0691` n `33` status `ready` deltaP `2.114` edge `0.0058` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

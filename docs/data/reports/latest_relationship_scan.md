# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T21:06:03.425357+00:00`
- Price records: `672`
- Market context records: `7918`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14745`

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

- `market_context_high->equity_24h` score `16.3243` n `85` status `ready` deltaP `26.7218` edge `1.3164` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.221` n `85` status `ready` deltaP `39.688` edge `0.4205` maxDD `0.0`
- `market_context_high->equity_4h` score `6.6302` n `94` status `ready` deltaP `25.4994` edge `0.4718` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `2.9216` n `85` status `ready` deltaP `24.8693` edge `0.2316` maxDD `-6.6476`
- `market_context_high->index_4h` score `2.7267` n `94` status `ready` deltaP `28.2322` edge `0.075` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.6519` n `94` status `ready` deltaP `24.0042` edge `0.1232` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.6549` n `94` status `ready` deltaP `12.8042` edge `0.1343` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.4151` n `85` status `ready` deltaP `28.2128` edge `0.0386` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.379` n `94` status `ready` deltaP `10.0253` edge `0.1598` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.2358` n `85` status `ready` deltaP `10.194` edge `0.1575` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.0694` n `94` status `ready` deltaP `11.2383` edge `0.186` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.9798` n `94` status `ready` deltaP `11.8518` edge `0.0435` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.9105` n `94` status `ready` deltaP `14.4431` edge `0.0226` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.5879` n `94` status `ready` deltaP `8.4947` edge `0.0302` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.2878` n `94` status `ready` deltaP `5.902` edge `0.0408` maxDD `-1.4603`
- `market_context_high->fx_4h` score `-0.2897` n `94` status `ready` deltaP `4.7596` edge `0.0059` maxDD `-0.9813`
- `market_context_high->fx_1h` score `-0.2906` n `94` status `ready` deltaP `1.6517` edge `0.0015` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.4485` n `94` status `ready` deltaP `0.3386` edge `-0.0029` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.5179` n `94` status `ready` deltaP `2.7002` edge `0.0153` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.8672` n `94` status `ready` deltaP `8.5266` edge `-0.1701` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

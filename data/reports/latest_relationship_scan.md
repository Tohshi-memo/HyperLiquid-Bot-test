# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T18:52:28.484884+00:00`
- Price records: `672`
- Market context records: `7908`
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

- `market_context_high->equity_24h` score `15.6876` n `93` status `ready` deltaP `28.9483` edge `1.2485` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.2954` n `93` status `ready` deltaP `36.0802` edge `0.3804` maxDD `-0.0389`
- `market_context_high->equity_4h` score `5.9793` n `99` status `ready` deltaP `21.3233` edge `0.4454` maxDD `-5.1426`
- `market_context_high->index_4h` score `2.3137` n `99` status `ready` deltaP `23.8949` edge `0.0695` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.1149` n `99` status `ready` deltaP `18.4775` edge `0.1153` maxDD `-0.979`
- `market_context_high->commodity_24h` score `2.0514` n `93` status `ready` deltaP `20.8949` edge `0.19` maxDD `-7.0012`
- `market_context_high->index_24h` score `1.4918` n `93` status `ready` deltaP `7.1013` edge `0.144` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.4471` n `99` status `ready` deltaP `11.1019` edge `0.1583` maxDD `-3.9374`
- `market_context_high->equity_1h` score `1.4224` n `102` status `ready` deltaP `11.4732` edge `0.1238` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.1652` n `93` status `ready` deltaP `31.9277` edge `0.0453` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `1.1639` n `99` status `ready` deltaP `13.0651` edge `0.1817` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0279` n `102` status `ready` deltaP `12.6776` edge `0.042` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.7495` n `102` status `ready` deltaP `12.7451` edge `0.0205` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.4412` n `102` status `ready` deltaP `7.08` edge `0.0274` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.2189` n `102` status `ready` deltaP `3.9891` edge `0.0349` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1686` n `102` status `ready` deltaP `2.1021` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.1779` n `99` status `ready` deltaP `6.8343` edge `0.0064` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.2023` n `99` status `ready` deltaP `4.8884` edge `0.0159` maxDD `-2.2874`
- `market_context_high->commodity_1h` score `-0.3856` n `102` status `ready` deltaP `1.0687` edge `0.0003` maxDD `-1.5486`
- `market_context_high->unknown_1h` score `-2.1718` n `102` status `ready` deltaP `6.4136` edge `-0.1814` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

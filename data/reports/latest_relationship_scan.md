# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T01:37:32.333418+00:00`
- Price records: `672`
- Market context records: `7938`
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

- `market_context_high->equity_24h` score `16.5738` n `82` status `ready` deltaP `25.7749` edge `1.3435` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.2588` n `82` status `ready` deltaP `37.9549` edge `0.4352` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7477` n `91` status `ready` deltaP `24.8681` edge `0.4858` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.5621` n `82` status `ready` deltaP `27.7058` edge `0.2654` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.838` n `91` status `ready` deltaP `25.5511` edge `0.1284` maxDD `-0.979`
- `market_context_high->index_4h` score `2.7353` n `91` status `ready` deltaP `28.069` edge `0.0768` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7445` n `91` status `ready` deltaP `13.2792` edge `0.1386` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.4055` n `82` status `ready` deltaP `28.2732` edge `0.0374` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.379` n `91` status `ready` deltaP `9.8298` edge `0.1611` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.2504` n `82` status `ready` deltaP `10.2643` edge `0.1589` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.1994` n `91` status `ready` deltaP `11.7228` edge `0.1936` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.0204` n `91` status `ready` deltaP `15.6816` edge `0.0235` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6659` n `91` status `ready` deltaP `9.2897` edge `0.0314` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5852` n `91` status `ready` deltaP `10.8887` edge `0.0433` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.2374` n `91` status `ready` deltaP `4.8431` edge `0.0414` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3871` n `91` status `ready` deltaP `1.2936` edge `-0.0014` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.3876` n `91` status `ready` deltaP `0.4537` edge `0.0014` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4734` n `91` status `ready` deltaP `4.3821` edge `0.0061` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.5042` n `91` status `ready` deltaP `2.7372` edge `0.0162` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.7761` n `91` status `ready` deltaP `8.9903` edge `-0.1656` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

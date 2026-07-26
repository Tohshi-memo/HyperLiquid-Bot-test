# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T02:22:27.625053+00:00`
- Price records: `672`
- Market context records: `7941`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11838`

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

- `market_context_high->equity_24h` score `16.5966` n `82` status `ready` deltaP `25.7749` edge `1.3454` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.2588` n `82` status `ready` deltaP `37.9549` edge `0.4352` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7477` n `91` status `ready` deltaP `24.8681` edge `0.4858` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.5897` n `82` status `ready` deltaP `27.7058` edge `0.2677` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.8392` n `91` status `ready` deltaP `25.5511` edge `0.1285` maxDD `-0.979`
- `market_context_high->index_4h` score `2.7084` n `91` status `ready` deltaP `27.7632` edge `0.0766` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7433` n `91` status `ready` deltaP `13.2792` edge `0.1385` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.452` n `82` status `ready` deltaP `28.794` edge `0.0378` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.3754` n `91` status `ready` deltaP `9.8298` edge `0.1608` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.2504` n `82` status `ready` deltaP `10.2643` edge `0.1589` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.1982` n `91` status `ready` deltaP `11.7228` edge `0.1935` maxDD `-6.7444`
- `market_context_high->index_1h` score `0.9952` n `91` status `ready` deltaP `15.3813` edge `0.0234` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6659` n `91` status `ready` deltaP `9.2897` edge `0.0314` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5821` n `91` status `ready` deltaP `10.8887` edge `0.0429` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.2078` n `91` status `ready` deltaP `4.394` edge `0.0406` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3973` n `91` status `ready` deltaP `1.1435` edge `-0.0017` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.3984` n `91` status `ready` deltaP `0.3036` edge `0.0015` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4612` n `91` status `ready` deltaP `4.535` edge `0.0061` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.5188` n `91` status `ready` deltaP `2.5843` edge `0.016` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.7869` n `91` status `ready` deltaP `8.9903` edge `-0.1665` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

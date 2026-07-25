# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T21:22:25.319098+00:00`
- Price records: `672`
- Market context records: `7919`
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

- `market_context_high->equity_24h` score `16.4053` n `84` status `ready` deltaP `26.4137` edge `1.3252` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.2846` n `84` status `ready` deltaP `39.688` edge `0.4258` maxDD `0.0`
- `market_context_high->equity_4h` score `6.6653` n `93` status `ready` deltaP `25.2935` edge `0.4761` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.0698` n `84` status `ready` deltaP `25.7936` edge `0.2375` maxDD `-6.6248`
- `market_context_high->metal_4h` score `2.7236` n `93` status `ready` deltaP `24.6755` edge `0.1247` maxDD `-0.979`
- `market_context_high->index_4h` score `2.7202` n `93` status `ready` deltaP `28.0606` edge `0.0756` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7176` n `93` status `ready` deltaP `13.3634` edge `0.1358` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `1.3535` n `93` status `ready` deltaP `9.7659` edge `0.1594` maxDD `-3.9374`
- `market_context_high->fx_24h` score `1.3492` n `84` status `ready` deltaP `27.5545` edge `0.0375` maxDD `-3.0343`
- `market_context_high->index_24h` score `1.2743` n `84` status `ready` deltaP `10.6647` edge `0.1593` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.0541` n `93` status `ready` deltaP `11.0019` edge `0.1863` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.9661` n `93` status `ready` deltaP `11.5897` edge `0.0441` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.9579` n `93` status `ready` deltaP `14.9908` edge `0.0229` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6422` n `93` status `ready` deltaP `9.1124` edge `0.0306` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.2739` n `93` status `ready` deltaP `5.5598` edge `0.0413` maxDD `-1.4603`
- `market_context_high->fx_4h` score `-0.3122` n `93` status `ready` deltaP `4.3406` edge `0.0058` maxDD `-0.9813`
- `market_context_high->fx_1h` score `-0.3228` n `93` status `ready` deltaP `1.2642` edge `0.0014` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.4762` n `93` status `ready` deltaP `-0.1647` edge `-0.0031` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.5402` n `93` status `ready` deltaP `2.407` edge `0.0154` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.8911` n `93` status `ready` deltaP `8.0919` edge `-0.1692` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

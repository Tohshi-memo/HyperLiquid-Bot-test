# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T08:22:32.287315+00:00`
- Price records: `672`
- Market context records: `7967`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11769`

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

- `market_context_high->equity_24h` score `16.3596` n `82` status `ready` deltaP `24.7332` edge `1.3326` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.1129` n `82` status `ready` deltaP `36.2218` edge `0.4346` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7935` n `91` status `ready` deltaP `25.4106` edge `0.486` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.8702` n `82` status `ready` deltaP `28.2266` edge `0.2876` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.7021` n `91` status `ready` deltaP `27.699` edge `0.0765` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.6419` n `91` status `ready` deltaP `23.2646` edge `0.1273` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.7877` n `96` status `ready` deltaP `14.5551` edge `0.1337` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.172` n `82` status `ready` deltaP `25.669` edge `0.0353` maxDD `-3.0343`
- `market_context_high->index_24h` score `1.1552` n `82` status `ready` deltaP `9.049` edge `0.1548` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.0698` n `91` status `ready` deltaP `8.3055` edge `0.1455` maxDD `-3.9374`
- `market_context_high->index_1h` score `1.012` n `96` status `ready` deltaP `15.7563` edge `0.0223` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.9792` n `91` status `ready` deltaP `10.3508` edge `0.1844` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.6397` n `96` status `ready` deltaP `9.2315` edge `0.0296` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4637` n `96` status `ready` deltaP `9.2253` edge `0.039` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `0.1172` n `96` status `ready` deltaP `2.8318` edge `0.0394` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1335` n `96` status `ready` deltaP `2.7027` edge `0.0016` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.296` n `96` status `ready` deltaP `2.8059` edge `0.0002` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.3671` n `91` status `ready` deltaP `4.196` edge `0.0179` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.4951` n `91` status `ready` deltaP `4.2915` edge `0.0049` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.6267` n `96` status `ready` deltaP `9.3875` edge `-0.1558` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

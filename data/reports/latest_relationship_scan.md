# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T16:37:24.819992+00:00`
- Price records: `672`
- Market context records: `7897`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14713`

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

- `market_context_high->equity_24h` score `14.8022` n `102` status `ready` deltaP `29.8203` edge `1.1689` maxDD `-6.0681`
- `market_context_high->metal_24h` score `5.615` n `102` status `ready` deltaP `27.6362` edge `0.3383` maxDD `-0.3703`
- `market_context_high->equity_4h` score `5.4875` n `104` status `ready` deltaP `18.4457` edge `0.4236` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `1.8614` n `102` status `ready` deltaP `21.6095` edge `0.1694` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `1.5657` n `104` status `ready` deltaP `12.8987` edge `0.1562` maxDD `-3.9374`
- `market_context_high->index_4h` score `1.4618` n `104` status `ready` deltaP `18.4457` edge `0.064` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.4232` n `110` status `ready` deltaP `12.5935` edge `0.1164` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `1.386` n `104` status `ready` deltaP `14.7162` edge `0.1892` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.3424` n `102` status `ready` deltaP `34.8244` edge `0.0487` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.3018` n `110` status `ready` deltaP `14.5563` edge `0.0523` maxDD `-1.6021`
- `market_context_high->metal_4h` score `1.2529` n `104` status `ready` deltaP `12.6524` edge `0.1073` maxDD `-0.979`
- `market_context_high->index_24h` score `0.6007` n `102` status `ready` deltaP `3.2577` edge `0.1287` maxDD `-1.3621`
- `market_context_high->index_1h` score `0.5707` n `110` status `ready` deltaP `10.7508` edge `0.0189` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.5187` n `104` status `ready` deltaP `9.3566` edge `0.0402` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.492` n `110` status `ready` deltaP `6.3527` edge `0.0419` maxDD `-1.4603`
- `market_context_high->metal_1h` score `0.2318` n `110` status `ready` deltaP `4.8231` edge `0.025` maxDD `-0.6936`
- `market_context_high->fx_1h` score `-0.2729` n `110` status `ready` deltaP `0.4341` edge `-0.0002` maxDD `-0.3474`
- `market_context_high->commodity_1h` score `-0.3624` n `110` status `ready` deltaP `3.5189` edge `0.0032` maxDD `-1.5486`
- `market_context_high->fx_4h` score `-0.3656` n `104` status `ready` deltaP `3.6462` edge `0.004` maxDD `-1.0148`
- `market_context_high->crypto_alt_24h` score `-1.9423` n `102` status `ready` deltaP `9.3316` edge `0.2183` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

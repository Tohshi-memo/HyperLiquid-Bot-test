# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T05:22:32.342443+00:00`
- Price records: `672`
- Market context records: `7954`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11845`

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

- `market_context_high->equity_24h` score `16.5287` n `82` status `ready` deltaP `25.6013` edge `1.3409` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.2069` n `82` status `ready` deltaP `37.2617` edge `0.4355` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7321` n `91` status `ready` deltaP `24.8681` edge `0.4845` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.6989` n `82` status `ready` deltaP `27.7058` edge `0.2768` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.8015` n `91` status `ready` deltaP `25.0938` edge `0.1284` maxDD `-0.979`
- `market_context_high->index_4h` score `2.6523` n `91` status `ready` deltaP `27.1516` edge `0.076` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7457` n `91` status `ready` deltaP `13.2792` edge `0.1387` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3578` n `82` status `ready` deltaP `27.7523` edge `0.0369` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.2268` n `91` status `ready` deltaP `9.0676` edge `0.1535` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.2175` n `82` status `ready` deltaP `9.917` edge `0.157` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.0544` n `91` status `ready` deltaP `10.9606` edge `0.1866` maxDD `-6.7444`
- `market_context_high->index_1h` score `0.9699` n `91` status `ready` deltaP `15.081` edge `0.0233` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.642` n `91` status `ready` deltaP `8.9903` edge `0.0314` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5206` n `91` status `ready` deltaP `9.9905` edge `0.041` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.1424` n `91` status `ready` deltaP `3.4958` edge `0.0382` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3793` n `91` status `ready` deltaP `1.4438` edge `-0.0014` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.4153` n `91` status `ready` deltaP `0.1534` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4538` n `91` status `ready` deltaP `4.6879` edge `0.0057` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.4931` n `91` status `ready` deltaP `2.8901` edge `0.0161` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.661` n `91` status `ready` deltaP `9.8885` edge `-0.162` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

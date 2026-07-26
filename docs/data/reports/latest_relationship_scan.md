# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T04:52:32.535751+00:00`
- Price records: `672`
- Market context records: `7952`
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

- `market_context_high->equity_24h` score `16.5347` n `82` status `ready` deltaP `25.6013` edge `1.3414` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.2033` n `82` status `ready` deltaP `37.2617` edge `0.4352` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7309` n `91` status `ready` deltaP `24.8681` edge `0.4844` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.6797` n `82` status `ready` deltaP `27.7058` edge `0.2752` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.827` n `91` status `ready` deltaP `25.3987` edge `0.1285` maxDD `-0.979`
- `market_context_high->index_4h` score `2.6657` n `91` status `ready` deltaP `27.3045` edge `0.0761` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.718` n `91` status `ready` deltaP `12.9789` edge `0.1384` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3892` n `82` status `ready` deltaP `28.0996` edge `0.0372` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.2436` n `91` status `ready` deltaP `9.0676` edge `0.1549` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.2198` n `82` status `ready` deltaP `9.917` edge `0.1573` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.0688` n `91` status `ready` deltaP `10.9606` edge `0.1878` maxDD `-6.7444`
- `market_context_high->index_1h` score `0.9711` n `91` status `ready` deltaP `15.081` edge `0.0234` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6671` n `91` status `ready` deltaP `9.2897` edge `0.0315` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5237` n `91` status `ready` deltaP `9.9905` edge `0.0414` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.1525` n `91` status `ready` deltaP `3.6455` edge `0.0385` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3793` n `91` status `ready` deltaP `1.4438` edge `-0.0014` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.402` n `91` status `ready` deltaP `0.3036` edge `0.0012` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4526` n `91` status `ready` deltaP `4.6879` edge `0.0058` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.52` n `91` status `ready` deltaP `2.5843` edge `0.0159` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.715` n `91` status `ready` deltaP `9.5891` edge `-0.1645` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

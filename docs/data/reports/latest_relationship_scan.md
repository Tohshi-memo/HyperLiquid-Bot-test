# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T06:22:28.884516+00:00`
- Price records: `672`
- Market context records: `7958`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->equity_24h` score `16.5203` n `82` status `ready` deltaP `25.6013` edge `1.3402` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.2105` n `82` status `ready` deltaP `37.2617` edge `0.4358` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7429` n `91` status `ready` deltaP `24.8681` edge `0.4854` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.7385` n `82` status `ready` deltaP `27.7058` edge `0.2801` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.7503` n `91` status `ready` deltaP `24.4841` edge `0.1282` maxDD `-0.979`
- `market_context_high->index_4h` score `2.6657` n `91` status `ready` deltaP `27.3045` edge `0.0761` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7042` n `92` status `ready` deltaP `13.001` edge `0.1371` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2963` n `82` status `ready` deltaP `27.0579` edge `0.0364` maxDD `-3.0343`
- `market_context_high->index_24h` score `1.2053` n `82` status `ready` deltaP `9.7434` edge `0.1566` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.1894` n `91` status `ready` deltaP `8.9152` edge `0.1514` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.057` n `91` status `ready` deltaP `11.113` edge `0.1858` maxDD `-6.7444`
- `market_context_high->index_1h` score `0.9213` n `92` status `ready` deltaP `14.5025` edge `0.0231` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6105` n `92` status `ready` deltaP `8.6566` edge `0.031` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4669` n `92` status `ready` deltaP `9.4832` edge `0.0375` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.0946` n `92` status `ready` deltaP `2.9224` edge `0.0359` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2321` n `92` status `ready` deltaP `0.865` edge `0.0012` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.3447` n `92` status `ready` deltaP `1.9454` edge `-0.0003` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.4492` n `91` status `ready` deltaP `3.3488` edge `0.0167` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.4574` n `91` status `ready` deltaP `4.6879` edge `0.0054` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.5425` n `92` status `ready` deltaP `9.7045` edge `-0.1509` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

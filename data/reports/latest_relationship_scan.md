# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T05:52:30.262196+00:00`
- Price records: `672`
- Market context records: `7956`
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

- `market_context_high->equity_24h` score `16.5191` n `82` status `ready` deltaP `25.6013` edge `1.3401` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.2081` n `82` status `ready` deltaP `37.2617` edge `0.4356` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7369` n `91` status `ready` deltaP `24.8681` edge `0.4849` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.7193` n `82` status `ready` deltaP `27.7058` edge `0.2785` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.7759` n `91` status `ready` deltaP `24.789` edge `0.1283` maxDD `-0.979`
- `market_context_high->index_4h` score `2.6523` n `91` status `ready` deltaP `27.1516` edge `0.076` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7733` n `91` status `ready` deltaP `13.5795` edge `0.139` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3265` n `82` status `ready` deltaP `27.4051` edge `0.0366` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.2136` n `91` status `ready` deltaP `9.0676` edge `0.1524` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.2053` n `82` status `ready` deltaP `9.7434` edge `0.1566` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.046` n `91` status `ready` deltaP `10.9606` edge `0.1859` maxDD `-6.7444`
- `market_context_high->index_1h` score `0.9711` n `91` status `ready` deltaP `15.081` edge `0.0234` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6671` n `91` status `ready` deltaP `9.2897` edge `0.0315` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5245` n `91` status `ready` deltaP `9.9905` edge `0.0415` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.1424` n `91` status `ready` deltaP `3.4958` edge `0.0382` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3793` n `91` status `ready` deltaP `1.4438` edge `-0.0014` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.4153` n `91` status `ready` deltaP `0.1534` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4562` n `91` status `ready` deltaP `4.6879` edge `0.0055` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.4651` n `91` status `ready` deltaP `3.1959` edge `0.0164` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.5543` n `91` status `ready` deltaP `10.1879` edge `-0.1551` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T04:22:25.408084+00:00`
- Price records: `672`
- Market context records: `7949`
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

- `market_context_high->equity_24h` score `16.5443` n `82` status `ready` deltaP `25.6013` edge `1.3422` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.1997` n `82` status `ready` deltaP `37.2617` edge `0.4349` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7357` n `91` status `ready` deltaP `24.8681` edge `0.4848` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.6605` n `82` status `ready` deltaP `27.7058` edge `0.2736` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.8404` n `91` status `ready` deltaP `25.5511` edge `0.1286` maxDD `-0.979`
- `market_context_high->index_4h` score `2.6926` n `91` status `ready` deltaP `27.6103` edge `0.0763` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7156` n `91` status `ready` deltaP `12.9789` edge `0.1382` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.4206` n `82` status `ready` deltaP `28.4468` edge `0.0375` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.2702` n `91` status `ready` deltaP `9.2201` edge `0.1561` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.2328` n `82` status `ready` deltaP `10.0907` edge `0.1578` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.0966` n `91` status `ready` deltaP `11.113` edge `0.1891` maxDD `-6.7444`
- `market_context_high->index_1h` score `0.9964` n `91` status `ready` deltaP `15.3813` edge `0.0235` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6791` n `91` status `ready` deltaP `9.4394` edge `0.0315` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5448` n `91` status `ready` deltaP `10.2899` edge `0.0421` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.165` n `91` status `ready` deltaP `3.7952` edge `0.0391` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3879` n `91` status `ready` deltaP `1.2936` edge `-0.0015` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.3996` n `91` status `ready` deltaP `0.3036` edge `0.0014` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4502` n `91` status `ready` deltaP `4.6879` edge `0.006` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.5346` n `91` status `ready` deltaP `2.4314` edge `0.0157` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.7269` n `91` status `ready` deltaP `9.4394` edge `-0.1645` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

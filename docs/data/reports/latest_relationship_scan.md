# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T04:07:24.062296+00:00`
- Price records: `672`
- Market context records: `7948`
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

- `market_context_high->equity_24h` score `16.5455` n `82` status `ready` deltaP `25.6013` edge `1.3423` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.1985` n `82` status `ready` deltaP `37.2617` edge `0.4348` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7369` n `91` status `ready` deltaP `24.8681` edge `0.4849` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.6521` n `82` status `ready` deltaP `27.7058` edge `0.2729` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.8404` n `91` status `ready` deltaP `25.5511` edge `0.1286` maxDD `-0.979`
- `market_context_high->index_4h` score `2.6926` n `91` status `ready` deltaP `27.6103` edge `0.0763` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7288` n `91` status `ready` deltaP `13.1291` edge `0.1383` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.4357` n `82` status `ready` deltaP `28.6204` edge `0.0376` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.292` n `91` status `ready` deltaP `9.3725` edge `0.1569` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.2328` n `82` status `ready` deltaP `10.0907` edge `0.1578` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.1172` n `91` status `ready` deltaP `11.2654` edge `0.1898` maxDD `-6.7444`
- `market_context_high->index_1h` score `0.9964` n `91` status `ready` deltaP `15.3813` edge `0.0235` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6791` n `91` status `ready` deltaP `9.4394` edge `0.0315` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5557` n `91` status `ready` deltaP `10.4396` edge `0.0425` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.1751` n `91` status `ready` deltaP `3.9449` edge `0.0394` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3965` n `91` status `ready` deltaP `1.1435` edge `-0.0016` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.3996` n `91` status `ready` deltaP `0.3036` edge `0.0014` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.449` n `91` status `ready` deltaP `4.6879` edge `0.0061` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.5493` n `91` status `ready` deltaP `2.2785` edge `0.0155` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.7245` n `91` status `ready` deltaP `9.4394` edge `-0.1643` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

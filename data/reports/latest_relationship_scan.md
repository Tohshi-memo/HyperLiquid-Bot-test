# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T18:37:27.671469+00:00`
- Price records: `672`
- Market context records: `8012`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11822`

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

- `market_context_high->equity_24h` score `15.9287` n `89` status `ready` deltaP `25.5409` edge `1.2913` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.8044` n `89` status `ready` deltaP `35.8752` edge `0.4112` maxDD `0.0`
- `market_context_high->equity_4h` score `6.1898` n `102` status `ready` deltaP `24.2098` edge `0.4437` maxDD `-5.1426`
- `market_context_high->metal_4h` score `2.5811` n `102` status `ready` deltaP `23.704` edge `0.1193` maxDD `-0.979`
- `market_context_high->commodity_24h` score `2.562` n `89` status `ready` deltaP `22.2538` edge `0.2056` maxDD `-6.2367`
- `market_context_high->index_4h` score `2.4097` n `102` status `ready` deltaP `25.1544` edge `0.0691` maxDD `-0.8791`
- `market_context_high->index_24h` score `2.0184` n `89` status `ready` deltaP `12.0636` edge `0.1548` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6696` n `102` status `ready` deltaP `14.0685` edge `0.1271` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3646` n `89` status `ready` deltaP `26.0413` edge `0.0369` maxDD `-2.7436`
- `market_context_high->index_1h` score `0.8558` n `102` status `ready` deltaP `13.9849` edge `0.0211` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6857` n `102` status `ready` deltaP `9.8962` edge `0.029` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.5756` n `102` status `ready` deltaP `9.2354` edge `0.1582` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.5531` n `102` status `ready` deltaP `10.7931` edge `0.04` maxDD `-1.6171`
- `market_context_high->crypto_alt_4h` score `0.5266` n `102` status `ready` deltaP `5.6854` edge `0.1177` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.0005` n `102` status `ready` deltaP `1.5036` edge `0.0333` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2559` n `102` status `ready` deltaP `0.422` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.3627` n `102` status `ready` deltaP `6.0658` edge `0.0041` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5389` n `102` status `ready` deltaP `-0.3561` edge `-0.0044` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.1735` n `102` status `ready` deltaP `0.6491` edge `-0.0046` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.9549` n `102` status `ready` deltaP `6.7705` edge `-0.1657` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

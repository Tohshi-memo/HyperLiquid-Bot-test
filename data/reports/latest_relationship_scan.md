# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T11:37:23.933051+00:00`
- Price records: `672`
- Market context records: `7980`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11790`

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

- `market_context_high->equity_24h` score `16.1061` n `84` status `ready` deltaP `24.5039` edge `1.313` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.0072` n `84` status `ready` deltaP `35.8752` edge `0.4281` maxDD `0.0`
- `market_context_high->equity_4h` score `6.5218` n `96` status `ready` deltaP `25.5248` edge `0.4626` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.4595` n `84` status `ready` deltaP `26.5129` edge `0.2648` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.6609` n `96` status `ready` deltaP `27.6797` edge `0.0732` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5489` n `96` status `ready` deltaP `22.9421` edge `0.1217` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.701` n `104` status `ready` deltaP `14.596` edge `0.1262` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.1774` n `84` status `ready` deltaP `9.7471` edge `0.153` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.1459` n `84` status `ready` deltaP `25.2976` edge `0.0356` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.0687` n `96` status `ready` deltaP `9.1463` edge `0.1398` maxDD `-3.9374`
- `market_context_high->index_1h` score `0.931` n `104` status `ready` deltaP `14.9839` edge `0.0207` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.855` n `96` status `ready` deltaP `9.9085` edge `0.177` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.7536` n `104` status `ready` deltaP `10.79` edge `0.0287` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5623` n `104` status `ready` deltaP `10.9397` edge `0.0402` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0512` n `104` status `ready` deltaP `0.5988` edge `0.0327` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2922` n `104` status `ready` deltaP `-0.2609` edge `0.001` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.5367` n `104` status `ready` deltaP `-0.3129` edge `-0.0044` maxDD `-1.9855`
- `market_context_high->fx_4h` score `-0.6105` n `96` status `ready` deltaP `3.0136` edge `0.0038` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.9483` n `96` status `ready` deltaP `2.2312` edge `0.0093` maxDD `-3.589`
- `market_context_high->unknown_1h` score `-1.9574` n `104` status `ready` deltaP `6.7538` edge `-0.1658` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

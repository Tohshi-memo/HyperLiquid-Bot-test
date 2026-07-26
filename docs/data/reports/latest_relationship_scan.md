# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T13:22:29.609767+00:00`
- Price records: `672`
- Market context records: `7988`
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

- `market_context_high->equity_24h` score `16.0199` n `87` status `ready` deltaP `25.407` edge `1.2998` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.9054` n `87` status `ready` deltaP `35.9375` edge `0.4192` maxDD `0.0`
- `market_context_high->equity_4h` score `6.3443` n `102` status `ready` deltaP `25.6456` edge `0.447` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `2.784` n `87` status `ready` deltaP `23.8445` edge `0.2263` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.6334` n `102` status `ready` deltaP `27.6512` edge `0.0711` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.6097` n `102` status `ready` deltaP `24.0764` edge `0.1192` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.6931` n `104` status `ready` deltaP `14.5267` edge `0.126` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.2637` n `87` status `ready` deltaP `11.2249` edge `0.1542` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.2301` n `87` status `ready` deltaP `26.1853` edge `0.0367` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.9253` n `104` status `ready` deltaP `14.9125` edge `0.0207` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.8543` n `102` status `ready` deltaP `10.8292` edge `0.1708` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.8475` n `102` status `ready` deltaP `8.1062` edge `0.1283` maxDD `-3.9374`
- `market_context_high->metal_1h` score `0.7164` n `104` status `ready` deltaP `10.3409` edge `0.0286` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5599` n `104` status `ready` deltaP `10.9397` edge `0.0399` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0675` n `104` status `ready` deltaP `0.4491` edge `0.0316` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.3041` n `104` status `ready` deltaP `-0.4894` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4609` n `102` status `ready` deltaP `4.8541` edge `0.004` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5412` n `104` status `ready` deltaP `-0.3858` edge `-0.0045` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.2241` n `102` status `ready` deltaP `-0.1733` edge `-0.0056` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.9514` n `104` status `ready` deltaP `6.7538` edge `-0.1653` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T13:37:25.330156+00:00`
- Price records: `672`
- Market context records: `7989`
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

- `market_context_high->equity_24h` score `16.0009` n `88` status `ready` deltaP `25.6944` edge `1.2963` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.8682` n `88` status `ready` deltaP `35.9375` edge `0.4161` maxDD `0.0`
- `market_context_high->equity_4h` score `6.3273` n `102` status `ready` deltaP `25.4931` edge `0.4466` maxDD `-5.1426`
- `market_context_high->index_4h` score `2.62` n `102` status `ready` deltaP `27.4988` edge `0.071` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5951` n `102` status `ready` deltaP `23.924` edge `0.119` maxDD `-0.979`
- `market_context_high->commodity_24h` score `2.5721` n `88` status `ready` deltaP `22.9955` edge `0.2143` maxDD `-6.5945`
- `market_context_high->equity_1h` score `1.6931` n `104` status `ready` deltaP `14.5267` edge `0.126` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.2912` n `88` status `ready` deltaP `11.6951` edge `0.1546` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.2701` n `88` status `ready` deltaP `26.6256` edge `0.0371` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.9253` n `104` status `ready` deltaP `14.9125` edge `0.0207` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.8713` n `102` status `ready` deltaP `10.9816` edge `0.1712` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.8645` n `102` status `ready` deltaP `8.2586` edge `0.1287` maxDD `-3.9374`
- `market_context_high->metal_1h` score `0.7045` n `104` status `ready` deltaP `10.1912` edge `0.0286` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5615` n `104` status `ready` deltaP `10.9397` edge `0.0401` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0559` n `104` status `ready` deltaP `0.5988` edge `0.0321` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.3041` n `104` status `ready` deltaP `-0.4894` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4609` n `102` status `ready` deltaP `4.8541` edge `0.004` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5412` n `104` status `ready` deltaP `-0.3858` edge `-0.0045` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.2138` n `102` status `ready` deltaP `-0.0209` edge `-0.0053` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.9514` n `104` status `ready` deltaP `6.7538` edge `-0.1653` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

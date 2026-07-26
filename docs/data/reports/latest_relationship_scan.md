# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T13:07:22.350123+00:00`
- Price records: `672`
- Market context records: `7987`
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

- `market_context_high->equity_24h` score `16.0336` n `86` status `ready` deltaP `25.113` edge `1.3029` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.9426` n `86` status `ready` deltaP `35.9375` edge `0.4223` maxDD `0.0`
- `market_context_high->equity_4h` score `6.3613` n `102` status `ready` deltaP `25.798` edge `0.4474` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.0071` n `86` status `ready` deltaP `24.7133` edge `0.2391` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.6468` n `102` status `ready` deltaP `27.8037` edge `0.0712` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.6109` n `102` status `ready` deltaP `24.0764` edge `0.1193` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.6931` n `104` status `ready` deltaP `14.5267` edge `0.126` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.2339` n `86` status `ready` deltaP `10.7437` edge `0.1536` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.1889` n `86` status `ready` deltaP `25.7307` edge `0.0363` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.9372` n `104` status `ready` deltaP `15.0622` edge `0.0207` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.8397` n `102` status `ready` deltaP `10.6767` edge `0.1706` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.8305` n `102` status `ready` deltaP `7.9537` edge `0.1279` maxDD `-3.9374`
- `market_context_high->metal_1h` score `0.7284` n `104` status `ready` deltaP `10.4906` edge `0.0286` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5599` n `104` status `ready` deltaP `10.9397` edge `0.0399` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0691` n `104` status `ready` deltaP `0.4491` edge `0.0314` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.3127` n `104` status `ready` deltaP `-0.6391` edge `0.0009` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4609` n `102` status `ready` deltaP `4.8541` edge `0.004` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5405` n `104` status `ready` deltaP `-0.3858` edge `-0.0044` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.2352` n `102` status `ready` deltaP `-0.3258` edge `-0.006` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.9526` n `104` status `ready` deltaP `6.7538` edge `-0.1654` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

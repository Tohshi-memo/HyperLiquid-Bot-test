# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T12:22:27.679163+00:00`
- Price records: `672`
- Market context records: `7983`
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

- `market_context_high->equity_24h` score `16.0691` n `84` status `ready` deltaP `24.4161` edge `1.3105` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.0108` n `84` status `ready` deltaP `35.8752` edge `0.4284` maxDD `0.0`
- `market_context_high->equity_4h` score `6.4475` n `99` status `ready` deltaP `25.7206` edge `0.4551` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.4977` n `84` status `ready` deltaP `26.6011` edge `0.2674` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.6645` n `99` status `ready` deltaP `27.8748` edge `0.0722` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5777` n `99` status `ready` deltaP `23.4525` edge `0.1207` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.6943` n `104` status `ready` deltaP `14.5267` edge `0.1261` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.1688` n `84` status `ready` deltaP `9.6559` edge `0.1525` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.1033` n `84` status `ready` deltaP `24.8102` edge `0.0353` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.9872` n `99` status `ready` deltaP `8.9678` edge `0.1342` maxDD `-3.9374`
- `market_context_high->index_1h` score `0.9504` n `104` status `ready` deltaP `15.2119` edge `0.0208` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.9229` n `99` status `ready` deltaP `10.8925` edge `0.1761` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.7416` n `104` status `ready` deltaP `10.6403` edge `0.0287` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5739` n `104` status `ready` deltaP `11.0894` edge `0.0407` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0535` n `104` status `ready` deltaP `0.5988` edge `0.0324` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2886` n `104` status `ready` deltaP `-0.19` edge `0.001` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.5327` n `104` status `ready` deltaP `-0.2361` edge `-0.0044` maxDD `-1.9855`
- `market_context_high->fx_4h` score `-0.5622` n `99` status `ready` deltaP `3.6477` edge `0.0036` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.9497` n `99` status `ready` deltaP `0.7915` edge `0.0006` maxDD `-4.5444`
- `market_context_high->unknown_1h` score `-1.9562` n `104` status `ready` deltaP `6.7538` edge `-0.1657` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

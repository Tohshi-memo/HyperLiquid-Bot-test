# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T12:07:26.381129+00:00`
- Price records: `672`
- Market context records: `7982`
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

- `market_context_high->equity_24h` score `16.0727` n `84` status `ready` deltaP `24.4161` edge `1.3108` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.0108` n `84` status `ready` deltaP `35.8752` edge `0.4284` maxDD `0.0`
- `market_context_high->equity_4h` score `6.476` n `98` status `ready` deltaP `25.6876` edge `0.4577` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.4905` n `84` status `ready` deltaP `26.6011` edge `0.2668` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.672` n `98` status `ready` deltaP `27.8932` edge `0.0727` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5786` n `98` status `ready` deltaP `23.3885` edge `0.1212` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.6955` n `104` status `ready` deltaP `14.5267` edge `0.1262` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.1696` n `84` status `ready` deltaP `9.6559` edge `0.1526` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.1183` n `84` status `ready` deltaP `24.9835` edge `0.0354` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.0707` n `98` status `ready` deltaP `9.6068` edge `0.1369` maxDD `-3.9374`
- `market_context_high->index_1h` score `0.9504` n `104` status `ready` deltaP `15.2119` edge `0.0208` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.8993` n `98` status `ready` deltaP `10.5214` edge `0.1766` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.7416` n `104` status `ready` deltaP `10.6403` edge `0.0287` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5747` n `104` status `ready` deltaP `11.0894` edge `0.0408` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0504` n `104` status `ready` deltaP `0.5988` edge `0.0328` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2808` n `104` status `ready` deltaP `-0.0403` edge `0.001` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.5327` n `104` status `ready` deltaP `-0.2361` edge `-0.0044` maxDD `-1.9855`
- `market_context_high->fx_4h` score `-0.5962` n `98` status `ready` deltaP `3.223` edge `0.0036` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.8443` n `98` status `ready` deltaP `1.1853` edge `0.0034` maxDD `-4.2306`
- `market_context_high->unknown_1h` score `-1.9574` n `104` status `ready` deltaP `6.7538` edge `-0.1658` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

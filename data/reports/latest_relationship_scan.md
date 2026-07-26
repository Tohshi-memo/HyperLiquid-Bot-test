# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T11:52:28.584358+00:00`
- Price records: `672`
- Market context records: `7981`
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

- `market_context_high->equity_24h` score `16.0989` n `84` status `ready` deltaP `24.5039` edge `1.3124` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.0084` n `84` status `ready` deltaP `35.8752` edge `0.4282` maxDD `0.0`
- `market_context_high->equity_4h` score `6.4974` n `97` status `ready` deltaP `25.5654` edge `0.4603` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.4643` n `84` status `ready` deltaP `26.5129` edge `0.2652` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.6697` n `97` status `ready` deltaP `27.8193` edge `0.073` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5634` n `97` status `ready` deltaP `23.1676` edge `0.1214` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.701` n `104` status `ready` deltaP `14.596` edge `0.1262` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.1767` n `84` status `ready` deltaP `9.7471` edge `0.1529` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.132` n `84` status `ready` deltaP `25.124` edge `0.0356` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.0682` n `97` status `ready` deltaP `9.3805` edge `0.1382` maxDD `-3.9374`
- `market_context_high->index_1h` score `0.9442` n `104` status `ready` deltaP `15.1338` edge `0.0208` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.8594` n `97` status `ready` deltaP `10.1427` edge `0.1758` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.7416` n `104` status `ready` deltaP `10.6403` edge `0.0287` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5739` n `104` status `ready` deltaP `11.0894` edge `0.0407` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0496` n `104` status `ready` deltaP `0.5988` edge `0.0329` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2837` n `104` status `ready` deltaP `-0.111` edge `0.0011` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.5367` n `104` status `ready` deltaP `-0.3129` edge `-0.0044` maxDD `-1.9855`
- `market_context_high->fx_4h` score `-0.6371` n `97` status `ready` deltaP `2.726` edge `0.0035` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.7361` n `97` status `ready` deltaP `1.6621` edge `0.0061` maxDD `-3.9246`
- `market_context_high->unknown_1h` score `-1.9442` n `104` status `ready` deltaP `6.9035` edge `-0.1657` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

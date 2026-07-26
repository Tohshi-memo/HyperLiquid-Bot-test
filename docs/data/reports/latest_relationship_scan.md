# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T10:22:32.581452+00:00`
- Price records: `672`
- Market context records: `7975`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11787`

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

- `market_context_high->equity_24h` score `16.2105` n `82` status `ready` deltaP `24.0388` edge `1.3248` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.0912` n `82` status `ready` deltaP `35.8752` edge `0.4351` maxDD `0.0`
- `market_context_high->equity_4h` score `6.58` n `96` status `ready` deltaP `25.9828` edge `0.4644` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.9428` n `82` status `ready` deltaP `28.4002` edge `0.2925` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.7292` n `96` status `ready` deltaP `28.443` edge `0.0738` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5853` n `96` status `ready` deltaP `23.247` edge `0.1227` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.7168` n `102` status `ready` deltaP `14.4939` edge `0.1282` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.1239` n `82` status `ready` deltaP `8.7018` edge `0.1531` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.1087` n `96` status `ready` deltaP `9.4512` edge `0.1411` maxDD `-3.9374`
- `market_context_high->fx_24h` score `1.0989` n `82` status `ready` deltaP `24.801` edge `0.035` maxDD `-3.0343`
- `market_context_high->index_1h` score `1.0759` n `102` status `ready` deltaP `16.6755` edge `0.0215` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.8974` n `96` status `ready` deltaP `10.2134` edge `0.1785` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.7304` n `102` status `ready` deltaP `10.4849` edge `0.0288` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5896` n `102` status `ready` deltaP `11.3156` edge `0.0412` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0827` n `102` status `ready` deltaP `-0.0822` edge `0.0332` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2393` n `102` status `ready` deltaP `0.7419` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.6764` n `96` status `ready` deltaP `2.2503` edge `0.0034` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.7342` n `102` status `ready` deltaP `0.7596` edge `-0.0045` maxDD `-1.9395`
- `market_context_high->commodity_4h` score `-0.9917` n `96` status `ready` deltaP `2.0785` edge `0.0067` maxDD `-3.589`
- `market_context_high->unknown_1h` score `-1.9875` n `102` status `ready` deltaP `6.1671` edge `-0.1644` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

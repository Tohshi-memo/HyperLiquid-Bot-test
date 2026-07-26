# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T09:22:30.524551+00:00`
- Price records: `672`
- Market context records: `7971`
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

- `market_context_high->equity_24h` score `16.2863` n `82` status `ready` deltaP `24.386` edge `1.3288` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.084` n `82` status `ready` deltaP `35.8752` edge `0.4345` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7677` n `92` status `ready` deltaP `25.7783` edge `0.4814` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.9224` n `82` status `ready` deltaP `28.4002` edge `0.2908` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.7427` n `92` status `ready` deltaP `28.3123` edge `0.0758` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5976` n `92` status `ready` deltaP `22.9056` edge `0.126` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.7008` n `99` status `ready` deltaP `13.964` edge `0.1304` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.1569` n `82` status `ready` deltaP `25.4954` edge `0.0352` maxDD `-3.0343`
- `market_context_high->index_24h` score `1.1301` n `82` status `ready` deltaP `8.7018` edge `0.1539` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.0558` n `92` status `ready` deltaP `8.4306` edge `0.1435` maxDD `-3.9374`
- `market_context_high->index_1h` score `1.0143` n `99` status `ready` deltaP `15.875` edge `0.0217` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.9445` n `92` status `ready` deltaP `10.1272` edge `0.183` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.688` n `99` status `ready` deltaP `9.8954` edge `0.0292` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5449` n `99` status `ready` deltaP `10.4564` edge `0.0412` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `0.0211` n `99` status `ready` deltaP `1.4033` edge `0.0366` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1997` n `99` status `ready` deltaP `1.4878` edge `0.0012` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.3619` n `99` status `ready` deltaP `1.7336` edge `-0.0011` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.4209` n `92` status `ready` deltaP `3.8682` edge `0.0169` maxDD `-2.5547`
- `market_context_high->fx_4h` score `-0.5122` n `92` status `ready` deltaP `4.1072` edge `0.0047` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.8052` n `99` status `ready` deltaP `7.8011` edge `-0.1601` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

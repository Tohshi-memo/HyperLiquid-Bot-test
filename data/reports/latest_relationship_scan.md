# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T02:07:24.155588+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11636`

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

- `risk_on_high->crypto_alt_24h` score `20.7876` n `55` status `ready` deltaP `45.3219` edge `1.4782` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `20.7876` n `55` status `ready` deltaP `45.3219` edge `1.4782` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `10.6191` n `92` status `ready` deltaP `31.6609` edge `0.7167` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.6191` n `92` status `ready` deltaP `31.6609` edge `0.7167` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `8.085` n `55` status `ready` deltaP `26.4363` edge `0.6393` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `8.085` n `55` status `ready` deltaP `26.4363` edge `0.6393` maxDD `-9.0103`
- `market_context_high->crypto_alt_24h` score `7.6186` n `108` status `ready` deltaP `23.0324` edge `0.9003` maxDD `-27.517`
- `market_context_high->unknown_4h` score `6.8465` n `149` status `ready` deltaP `21.054` edge `0.4772` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.0756` n `55` status `ready` deltaP `68.0556` edge `0.0526` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.0756` n `55` status `ready` deltaP `68.0556` edge `0.0526` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `5.2304` n `108` status `ready` deltaP `20.544` edge `0.548` maxDD `-17.2607`
- `risk_on_high->metal_24h` score `4.2715` n `55` status `ready` deltaP `40.06` edge `0.1361` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.2715` n `55` status `ready` deltaP `40.06` edge `0.1361` maxDD `-0.7767`
- `market_context_high->metal_24h` score `3.8304` n `108` status `ready` deltaP `30.4977` edge `0.2178` maxDD `-3.1535`
- `risk_on_high->unknown_1h` score `3.7881` n `97` status `ready` deltaP `11.0223` edge `0.2777` maxDD `-1.1741`
- `risk_on_and_context->unknown_1h` score `3.7881` n `97` status `ready` deltaP `11.0223` edge `0.2777` maxDD `-1.1741`
- `market_context_high->unknown_1h` score `2.7349` n `161` status `ready` deltaP `7.9872` edge `0.2197` maxDD `-1.2699`
- `market_context_high->fx_24h` score `1.0059` n `108` status `ready` deltaP `36.5741` edge `0.031` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8717` n `55` status `ready` deltaP `9.6528` edge `0.1462` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8717` n `55` status `ready` deltaP `9.6528` edge `0.1462` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

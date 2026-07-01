# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T13:07:38.561806+00:00`
- Price records: `672`
- Market context records: `5354`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11482`

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

- `market_context_high->unknown_24h` score `14.2246` n `163` status `ready` deltaP `18.9811` edge `1.072` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.3141` n `163` status `ready` deltaP `21.7898` edge `0.7516` maxDD `-29.6555`
- `market_context_high->equity_24h` score `4.4081` n `163` status `ready` deltaP `17.8692` edge `0.8111` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.6143` n `194` status `ready` deltaP `13.3361` edge `0.3582` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.2832` n `194` status `ready` deltaP `10.2071` edge `0.2863` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.675` n `194` status `ready` deltaP `9.7875` edge `0.2382` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.7937` n `163` status `ready` deltaP `24.2331` edge `0.1037` maxDD `-7.413`
- `market_context_high->fx_24h` score `0.1481` n `163` status `ready` deltaP `9.5817` edge `0.038` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.1329` n `199` status `ready` deltaP `6.2701` edge `0.0658` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0871` n `199` status `ready` deltaP `4.8912` edge `0.0105` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `-0.118` n `199` status `ready` deltaP `3.8869` edge `0.0888` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.1645` n `199` status `ready` deltaP `1.1923` edge `0.0745` maxDD `-5.0257`
- `market_context_high->index_4h` score `-0.4149` n `194` status `ready` deltaP `5.6119` edge `0.0253` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.4368` n `199` status `ready` deltaP `-0.8929` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5168` n `199` status `ready` deltaP `0.1444` edge `0.0003` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7008` n `194` status `ready` deltaP `1.5259` edge `0.0029` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.1905` n `194` status `ready` deltaP `8.0604` edge `-0.0347` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.5605` n `199` status `ready` deltaP `-4.2608` edge `-0.0084` maxDD `-3.4592`
- `market_context_high->metal_4h` score `-2.6793` n `194` status `ready` deltaP `-7.9865` edge `-0.0378` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-3.8298` n `194` status `ready` deltaP `-7.1662` edge `-0.043` maxDD `-11.937`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

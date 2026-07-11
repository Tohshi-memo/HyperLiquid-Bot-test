# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T08:57:10.657544+00:00`
- Price records: `672`
- Market context records: `6375`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11120`

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

- `news_risk_high->crypto_alt_24h` score `14.3616` n `32` status `ready` deltaP `38.5417` edge `0.9546` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3196` n `32` status `ready` deltaP `52.4306` edge `0.1771` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3121` n `32` status `ready` deltaP `17.5347` edge `0.5139` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `4.1043` n `32` status `ready` deltaP `35.5903` edge `0.1253` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.9486` n `32` status `ready` deltaP `40.7774` edge `0.0618` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3859` n `32` status `ready` deltaP `28.7425` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5084` n `32` status `ready` deltaP `14.5771` edge `0.1429` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8941` n `32` status `ready` deltaP `11.1714` edge `0.0863` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.476` n `217` status `ready` deltaP `14.8772` edge `0.0415` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2616` n `221` status `ready` deltaP `-6.3877` edge `0.1652` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1611` n `217` status `ready` deltaP `8.904` edge `0.0217` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.298` n `32` status `ready` deltaP `6.381` edge `-0.0329` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.3838` n `221` status `ready` deltaP `3.8631` edge `0.0028` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.4141` n `139` status `ready` deltaP `17.7234` edge `0.0856` maxDD `-11.8809`
- `market_context_high->index_1h` score `-0.6282` n `221` status `ready` deltaP `-1.7232` edge `0.0029` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.6657` n `221` status `ready` deltaP `-0.1037` edge `-0.0014` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7014` n `32` status `ready` deltaP `-2.2455` edge `-0.0252` maxDD `-1.6464`
- `market_context_high->commodity_24h` score `-0.7018` n `139` status `ready` deltaP `-4.8998` edge `0.1291` maxDD `-6.2457`
- `news_risk_high->index_24h` score `-0.7261` n `32` status `ready` deltaP `0.5208` edge `-0.0094` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.887` n `217` status `ready` deltaP `7.015` edge `0.0492` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T23:31:38.177842+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11717`

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

- `market_context_high->unknown_24h` score `132.5462` n `106` status `ready` deltaP `-26.9464` edge `17.4411` maxDD `-7.8016`
- `risk_on_high->unknown_24h` score `33.701` n `32` status `ready` deltaP `-38.0903` edge `4.6496` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.701` n `32` status `ready` deltaP `-38.0903` edge `4.6496` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9406` n `36` status `ready` deltaP `26.3142` edge `0.9409` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6725` n `36` status `ready` deltaP `39.1768` edge `0.3782` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.7651` n `106` status `ready` deltaP `37.8012` edge `0.3175` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.6494` n `32` status `ready` deltaP `39.688` edge `0.2062` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.6494` n `32` status `ready` deltaP `39.688` edge `0.2062` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0071` n `32` status `ready` deltaP `27.3343` edge `0.4471` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.0071` n `32` status `ready` deltaP `27.3343` edge `0.4471` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.7811` n `36` status `ready` deltaP `31.8891` edge `0.1025` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9779` n `32` status `ready` deltaP `21.5701` edge `0.1226` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9779` n `32` status `ready` deltaP `21.5701` edge `0.1226` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.2846` n `106` status `ready` deltaP `20.8036` edge `0.0988` maxDD `-0.7687`
- `news_risk_high->index_4h` score `2.0412` n `36` status `ready` deltaP `23.5772` edge `0.0261` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7981` n `36` status `ready` deltaP `8.8823` edge `0.1225` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3988` n `32` status `ready` deltaP `15.0075` edge `0.0398` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3988` n `32` status `ready` deltaP `15.0075` edge `0.0398` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7652` n `32` status `ready` deltaP `14.8559` edge `0.177` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7652` n `32` status `ready` deltaP `14.8559` edge `0.177` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

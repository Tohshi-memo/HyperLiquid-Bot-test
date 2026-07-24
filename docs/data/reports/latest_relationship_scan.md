# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T01:37:24.804450+00:00`
- Price records: `672`
- Market context records: `7729`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.7635` n `132` status `ready` deltaP `19.396` edge `0.3185` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `1.0897` n `133` status `ready` deltaP `13.4573` edge `0.0452` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.9775` n `133` status `ready` deltaP `14.4989` edge `0.1566` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.6999` n `133` status `ready` deltaP `8.9618` edge `0.1103` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.5918` n `133` status `ready` deltaP `8.4964` edge `0.0786` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.4633` n `133` status `ready` deltaP `1.6636` edge `0.2396` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3962` n `133` status `ready` deltaP `9.0949` edge `0.0154` maxDD `-0.7743`
- `market_context_high->fx_24h` score `0.17` n `132` status `ready` deltaP `15.4287` edge `0.0277` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `0.1688` n `133` status `ready` deltaP `4.1286` edge `0.0298` maxDD `-1.4603`
- `market_context_high->metal_24h` score `-0.1075` n `133` status `ready` deltaP `4.9381` edge `0.1672` maxDD `-2.3927`
- `market_context_high->commodity_1h` score `-0.1544` n `133` status `ready` deltaP `3.8452` edge `0.0074` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.2361` n `133` status `ready` deltaP `3.7168` edge `0.0149` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.2623` n `133` status `ready` deltaP `10.5585` edge `0.0418` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4903` n `133` status `ready` deltaP `-0.2269` edge `-0.0006` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7752` n `133` status `ready` deltaP `2.3153` edge `0.0203` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.5171` n `133` status `ready` deltaP `0.6808` edge `0.0745` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5743` n `133` status `ready` deltaP `-5.385` edge `-0.0031` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7309` n `132` status `ready` deltaP `5.6858` edge `-0.0238` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1864` n `133` status `ready` deltaP `-1.2741` edge `-0.1147` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5739` n `132` status `ready` deltaP `-18.4537` edge `0.0033` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

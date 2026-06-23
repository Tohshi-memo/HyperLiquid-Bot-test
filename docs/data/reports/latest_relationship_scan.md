# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T19:22:26.862614+00:00`
- Price records: `672`
- Market context records: `4546`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10045`

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

- `market_context_high->unknown_1h` score `57.4733` n `168` status `ready` deltaP `7.2427` edge `4.7912` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `29.4879` n `168` status `ready` deltaP `7.3824` edge `2.5647` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.4378` n `168` status `ready` deltaP `7.4115` edge `0.0027` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-0.6367` n `168` status `ready` deltaP `0.7663` edge `-0.0027` maxDD `-1.1038`
- `market_context_high->commodity_1h` score `-0.6651` n `168` status `ready` deltaP `-0.8626` edge `0.0124` maxDD `-3.0206`
- `market_context_high->index_4h` score `-0.936` n `168` status `ready` deltaP `0.9364` edge `-0.0098` maxDD `-5.9823`
- `market_context_high->index_1h` score `-1.0465` n `168` status `ready` deltaP `-3.2863` edge `-0.0114` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.079` n `168` status `ready` deltaP `-2.2526` edge `0.0238` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.0961` n `168` status `ready` deltaP `2.8165` edge `0.0668` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-2.0614` n `168` status `ready` deltaP `2.1269` edge `0.0248` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-2.7069` n `166` status `ready` deltaP `2.6795` edge `-0.1511` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.5232` n `168` status `ready` deltaP `-4.7512` edge `-0.0801` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-5.4175` n `166` status `ready` deltaP `-12.8744` edge `-0.0144` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5533` n `168` status `ready` deltaP `-4.0277` edge `-0.1072` maxDD `-22.2982`
- `market_context_high->index_24h` score `-5.6838` n `166` status `ready` deltaP `-9.1512` edge `-0.1302` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.4662` n `168` status `ready` deltaP `-5.2146` edge `-0.1288` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-7.9153` n `166` status `ready` deltaP `5.2606` edge `0.0173` maxDD `-44.2915`
- `market_context_high->equity_24h` score `-13.3706` n `166` status `ready` deltaP `-0.9936` edge `-0.2396` maxDD `-102.1031`
- `market_context_high->crypto_alt_4h` score `-13.4005` n `168` status `ready` deltaP `-2.5479` edge `-0.234` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-15.5322` n `168` status `ready` deltaP `-7.4187` edge `-0.3185` maxDD `-67.7779`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

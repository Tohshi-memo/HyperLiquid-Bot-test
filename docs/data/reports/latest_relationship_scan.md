# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T06:22:26.473534+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12673`

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

- `market_context_high->unknown_24h` score `19218.0305` n `54` status `ready` deltaP `13.3102` edge `1601.419` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `377.2419` n `82` status `ready` deltaP `-4.8014` edge `31.511` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.7249` n `82` status `ready` deltaP `31.8851` edge `1.3133` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.6788` n `82` status `ready` deltaP `37.589` edge `1.3697` maxDD `-9.098`
- `market_context_high->equity_24h` score `11.0006` n `54` status `ready` deltaP `49.6528` edge `0.5857` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.7551` n `54` status `ready` deltaP `19.3287` edge `0.7668` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.8023` n `82` status `ready` deltaP `19.165` edge `0.6171` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.3068` n `82` status `ready` deltaP `44.3894` edge `0.2473` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.6682` n `82` status `ready` deltaP `24.9196` edge `0.2683` maxDD `-0.6334`
- `market_context_high->index_24h` score `4.3187` n `54` status `ready` deltaP `45.4283` edge `0.0921` maxDD `-0.1382`
- `market_context_high->commodity_24h` score `4.305` n `54` status `ready` deltaP `42.1875` edge `0.0775` maxDD `0.0`
- `market_context_high->metal_24h` score `0.7873` n `54` status `ready` deltaP `11.0533` edge `0.1147` maxDD `-1.9958`
- `risk_on_high->crypto_alt_4h` score `0.3503` n `61` status `ready` deltaP `11.3805` edge `0.1365` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.3503` n `61` status `ready` deltaP `11.3805` edge `0.1365` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.2869` n `82` status `ready` deltaP `10.5183` edge `0.0295` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.1208` n `65` status `ready` deltaP `4.8526` edge `0.0033` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1208` n `65` status `ready` deltaP `4.8526` edge `0.0033` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.1358` n `65` status `ready` deltaP `3.0147` edge `0.0016` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.1358` n `65` status `ready` deltaP `3.0147` edge `0.0016` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.1947` n `126` status `ready` deltaP `2.5449` edge `-0.0016` maxDD `-0.5274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

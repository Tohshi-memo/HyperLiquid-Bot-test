# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T07:22:27.424764+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11190`

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

- `news_risk_high->unknown_1h` score `443.5733` n `82` status `ready` deltaP `-5.999` edge `37.0466` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.0489` n `82` status `ready` deltaP `40.6854` edge `1.4483` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.7743` n `82` status `ready` deltaP `36.127` edge `1.3874` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.9882` n `82` status `ready` deltaP `35.7191` edge `0.9389` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2373` n `82` status `ready` deltaP `59.4911` edge `0.3075` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.8246` n `80` status `ready` deltaP `39.8276` edge `0.3032` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2006` n `41` status `ready` deltaP `39.8276` edge `0.2512` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2006` n `41` status `ready` deltaP `39.8276` edge `0.2512` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.6828` n `82` status `ready` deltaP `34.2431` edge `0.2907` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.271` n `41` status `ready` deltaP `58.7679` edge `0.0517` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.271` n `41` status `ready` deltaP `58.7679` edge `0.0517` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.7025` n `80` status `ready` deltaP `53.7069` edge `0.0554` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9587` n `52` status `ready` deltaP `26.5947` edge `0.0209` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9587` n `52` status `ready` deltaP `26.5947` edge `0.0209` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.759` n `137` status `ready` deltaP `22.0046` edge `0.0417` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7586` n `137` status `ready` deltaP `12.812` edge `0.0155` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6576` n `82` status `ready` deltaP `16.311` edge `0.0384` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3254` n `137` status `ready` deltaP `11.9881` edge `0.0094` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2432` n `52` status `ready` deltaP `7.1972` edge `0.0075` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2432` n `52` status `ready` deltaP `7.1972` edge `0.0075` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

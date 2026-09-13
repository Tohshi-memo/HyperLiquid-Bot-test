# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T20:37:26.253559+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12744`

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

- `market_context_high->unknown_24h` score `17680.7088` n `56` status `ready` deltaP `10.2093` edge `1473.3445` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `8931.1181` n `35` status `ready` deltaP `10.5665` edge `744.1959` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `8931.1181` n `35` status `ready` deltaP `10.5665` edge `744.1959` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `429.2919` n `82` status `ready` deltaP `-5.2505` edge `35.8515` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.7003` n `82` status `ready` deltaP `36.2027` edge `1.3658` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3316` n `82` status `ready` deltaP `38.0236` edge `1.4212` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.7151` n `82` status `ready` deltaP `28.6501` edge `0.7966` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.2926` n `82` status `ready` deltaP `52.4222` edge `0.2759` maxDD `-0.0797`
- `risk_on_high->commodity_24h` score `4.8134` n `35` status `ready` deltaP `39.8276` edge `0.1356` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8134` n `35` status `ready` deltaP `39.8276` edge `0.1356` maxDD `0.0`
- `news_risk_high->metal_24h` score `4.8041` n `82` status `ready` deltaP `26.8293` edge `0.2669` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.6466` n `56` status `ready` deltaP `39.8276` edge `0.1217` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `3.6471` n `56` status `ready` deltaP `5.0616` edge `0.4363` maxDD `-9.6226`
- `risk_on_high->crypto_alt_24h` score `3.4707` n `35` status `ready` deltaP `1.8473` edge `0.4105` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `3.4707` n `35` status `ready` deltaP `1.8473` edge `0.4105` maxDD `-7.0204`
- `risk_on_high->fx_24h` score `1.9766` n `35` status `ready` deltaP `42.9064` edge `0.0192` maxDD `-1.1462`
- `risk_on_and_context->fx_24h` score `1.9766` n `35` status `ready` deltaP `42.9064` edge `0.0192` maxDD `-1.1462`
- `risk_on_high->commodity_4h` score `1.2243` n `59` status `ready` deltaP `18.3082` edge `0.0153` maxDD `-0.1596`
- `risk_on_and_context->commodity_4h` score `1.2243` n `59` status `ready` deltaP `18.3082` edge `0.0153` maxDD `-0.1596`
- `market_context_high->commodity_4h` score `0.9283` n `131` status `ready` deltaP `15.6558` edge `0.0148` maxDD `-0.345`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T20:07:26.269636+00:00`
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

- `market_context_high->unknown_24h` score `17679.4848` n `56` status `ready` deltaP `10.2093` edge `1473.2425` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `8332.0431` n `36` status `ready` deltaP `10.8046` edge `694.2714` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `8332.0431` n `36` status `ready` deltaP `10.8046` edge `694.2714` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `429.4275` n `82` status `ready` deltaP `-5.1008` edge `35.8618` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6799` n `82` status `ready` deltaP `36.2027` edge `1.3641` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3376` n `82` status `ready` deltaP `38.0236` edge `1.4217` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.6203` n `82` status `ready` deltaP `28.3053` edge `0.791` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.2518` n `82` status `ready` deltaP `52.0773` edge `0.2748` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.8005` n `82` status `ready` deltaP `26.8293` edge `0.2666` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.7858` n `36` status `ready` deltaP `39.8276` edge `0.1333` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7858` n `36` status `ready` deltaP `39.8276` edge `0.1333` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.5902` n `56` status `ready` deltaP `39.8276` edge `0.117` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `3.7446` n `36` status `ready` deltaP `3.2759` edge `0.4238` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `3.7446` n `36` status `ready` deltaP `3.2759` edge `0.4238` maxDD `-7.0204`
- `market_context_high->crypto_alt_24h` score `2.4931` n `56` status `ready` deltaP `5.0616` edge `0.452` maxDD `-9.6226`
- `risk_on_high->fx_24h` score `1.8232` n `36` status `ready` deltaP `41.1877` edge `0.0168` maxDD `-1.2776`
- `risk_on_and_context->fx_24h` score `1.8232` n `36` status `ready` deltaP `41.1877` edge `0.0168` maxDD `-1.2776`
- `risk_on_high->commodity_4h` score `1.0926` n `59` status `ready` deltaP `16.9181` edge `0.0139` maxDD `-0.1844`
- `risk_on_and_context->commodity_4h` score `1.0926` n `59` status `ready` deltaP `16.9181` edge `0.0139` maxDD `-0.1844`
- `market_context_high->commodity_4h` score `0.8174` n `131` status `ready` deltaP `14.434` edge `0.0137` maxDD `-0.345`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

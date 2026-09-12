# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T22:07:31.098575+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12613`

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

- `market_context_high->unknown_24h` score `13234.3586` n `67` status `ready` deltaP `12.4663` edge `1102.7853` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `382.2148` n `82` status `ready` deltaP `-5.6996` edge `31.9314` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.1812` n `78` status `ready` deltaP `38.7687` edge `1.4037` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `17.7461` n `78` status `ready` deltaP `32.2249` edge `1.3128` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `12.1962` n `67` status `ready` deltaP `26.293` edge `0.9238` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.8667` n `67` status `ready` deltaP `43.9236` edge `0.5294` maxDD `0.0`
- `news_risk_high->equity_24h` score `6.8718` n `78` status `ready` deltaP `17.0005` edge `0.6071` maxDD `-5.4898`
- `news_risk_high->index_24h` score `6.4714` n `78` status `ready` deltaP `45.2323` edge `0.2554` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.3792` n `78` status `ready` deltaP `31.3301` edge `0.2847` maxDD `-0.6239`
- `market_context_high->commodity_24h` score `3.3151` n `67` status `ready` deltaP `36.0438` edge `0.0494` maxDD `-0.0748`
- `market_context_high->index_24h` score `3.2204` n `67` status `ready` deltaP `34.3827` edge `0.0785` maxDD `-0.1483`
- `risk_on_high->crypto_alt_4h` score `0.9848` n `47` status `ready` deltaP `12.3119` edge `0.1751` maxDD `-5.4742`
- `risk_on_and_context->crypto_alt_4h` score `0.9848` n `47` status `ready` deltaP `12.3119` edge `0.1751` maxDD `-5.4742`
- `news_risk_high->index_4h` score `0.0747` n `82` status `ready` deltaP `6.7073` edge `0.0277` maxDD `-0.6935`
- `risk_on_high->index_1h` score `0.0557` n `54` status `ready` deltaP `6.3595` edge `0.0001` maxDD `-0.162`
- `risk_on_and_context->index_1h` score `0.0557` n `54` status `ready` deltaP `6.3595` edge `0.0001` maxDD `-0.162`
- `market_context_high->equity_4h` score `0.028` n `94` status `ready` deltaP `11.3908` edge `0.034` maxDD `-3.1742`
- `risk_on_high->metal_1h` score `0.0147` n `54` status `ready` deltaP `5.1453` edge `0.0006` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.0147` n `54` status `ready` deltaP `5.1453` edge `0.0006` maxDD `-0.3081`
- `risk_on_high->equity_1h` score `-0.209` n `54` status `ready` deltaP `7.5571` edge `0.001` maxDD `-1.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

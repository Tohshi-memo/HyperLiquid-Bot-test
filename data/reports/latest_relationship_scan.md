# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T04:22:30.806148+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9746`

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

- `risk_on_high->crypto_alt_4h` score `5.9702` n `52` status `ready` deltaP `20.6379` edge `0.4047` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.9702` n `52` status `ready` deltaP `20.6379` edge `0.4047` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.3266` n `47` status `ready` deltaP `30.087` edge `0.2433` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3266` n `47` status `ready` deltaP `30.087` edge `0.2433` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `5.1128` n `105` status `ready` deltaP `16.1324` edge `0.4634` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `5.0047` n `52` status `ready` deltaP `36.1046` edge `0.4862` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.0047` n `52` status `ready` deltaP `36.1046` edge `0.4862` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `4.939` n `105` status `ready` deltaP `20.0973` edge `0.4335` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.9127` n `117` status `ready` deltaP `13.5665` edge `0.1757` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5462` n `117` status `ready` deltaP `8.057` edge `0.1557` maxDD `-3.7781`
- `market_context_high->unknown_4h` score `0.8955` n `105` status `ready` deltaP `-4.1463` edge `0.1669` maxDD `-1.8373`
- `risk_on_high->crypto_major_1h` score `-0.1513` n `54` status `ready` deltaP `3.4986` edge `0.0295` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1513` n `54` status `ready` deltaP `3.4986` edge `0.0295` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3071` n `117` status `ready` deltaP `1.5477` edge `0.0021` maxDD `-0.3742`
- `market_context_high->metal_4h` score `-0.465` n `105` status `ready` deltaP `8.2476` edge `0.0108` maxDD `-1.6961`
- `risk_on_high->crypto_alt_1h` score `-0.49` n `54` status `ready` deltaP `3.3101` edge `0.0177` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.49` n `54` status `ready` deltaP `3.3101` edge `0.0177` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.5099` n `117` status `ready` deltaP `5.9177` edge `0.005` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.5321` n `117` status `ready` deltaP `1.2243` edge `-0.0016` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.5458` n `54` status `ready` deltaP `0.5046` edge `-0.0002` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

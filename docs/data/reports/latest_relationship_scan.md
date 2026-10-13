# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T12:07:29.314100+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9804`

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

- `market_context_high->crypto_alt_4h` score `8.1882` n `117` status `ready` deltaP `21.1851` edge `0.686` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `7.2254` n `117` status `ready` deltaP `25.0834` edge `0.5908` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.7771` n `54` status `ready` deltaP `23.4643` edge `0.4531` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.7771` n `54` status `ready` deltaP `23.4643` edge `0.4531` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.8418` n `48` status `ready` deltaP `31.6522` edge `0.2758` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8418` n `48` status `ready` deltaP `31.6522` edge `0.2758` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.2363` n `54` status `ready` deltaP `38.1888` edge `0.502` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.2363` n `54` status `ready` deltaP `38.1888` edge `0.502` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `3.183` n `117` status `ready` deltaP `-3.467` edge `0.353` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.2388` n `117` status `ready` deltaP `15.6623` edge `0.1889` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.6542` n `117` status `ready` deltaP `8.5061` edge `0.1617` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0632` n `117` status `ready` deltaP `12.2408` edge `0.0282` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.0812` n `54` status `ready` deltaP `3.9477` edge `0.0355` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.0812` n `54` status `ready` deltaP `3.9477` edge `0.0355` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2651` n `117` status `ready` deltaP `1.9982` edge `0.0026` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.278` n `54` status `ready` deltaP `5.4059` edge `0.0309` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.278` n `54` status `ready` deltaP `5.4059` edge `0.0309` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.4416` n `117` status `ready` deltaP `6.6662` edge `0.0057` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.4962` n `117` status `ready` deltaP `1.8249` edge `-0.001` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.5014` n `54` status `ready` deltaP `1.2531` edge `0.0005` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

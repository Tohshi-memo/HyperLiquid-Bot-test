# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T12:52:27.063656+00:00`
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

- `market_context_high->crypto_alt_4h` score `8.305` n `117` status `ready` deltaP `21.49` edge `0.6937` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `7.3086` n `117` status `ready` deltaP `25.3883` edge `0.5957` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.8939` n `54` status `ready` deltaP `23.7692` edge `0.4608` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.8939` n `54` status `ready` deltaP `23.7692` edge `0.4608` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.9572` n `48` status `ready` deltaP `32.0` edge `0.2831` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9572` n `48` status `ready` deltaP `32.0` edge `0.2831` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.2904` n `54` status `ready` deltaP `38.4937` edge `0.5069` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.2904` n `54` status `ready` deltaP `38.4937` edge `0.5069` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `3.3474` n `117` status `ready` deltaP `-3.467` edge `0.3667` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.2028` n `117` status `ready` deltaP `15.3629` edge `0.1879` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.6482` n `117` status `ready` deltaP `8.3564` edge `0.1622` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0692` n `117` status `ready` deltaP `12.2408` edge `0.0287` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.0851` n `54` status `ready` deltaP `3.798` edge `0.036` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.0851` n `54` status `ready` deltaP `3.798` edge `0.036` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2771` n `117` status `ready` deltaP `1.848` edge `0.0026` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.3014` n `54` status `ready` deltaP `5.1065` edge `0.0299` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.3014` n `54` status `ready` deltaP `5.1065` edge `0.0299` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.4261` n `117` status `ready` deltaP `6.8159` edge `0.006` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.4876` n `117` status `ready` deltaP `1.975` edge `-0.0009` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.4913` n `54` status `ready` deltaP `1.4028` edge `0.0008` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

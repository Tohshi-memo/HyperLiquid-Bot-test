# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T13:22:29.809303+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9777`

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

- `market_context_high->crypto_alt_4h` score `8.3254` n `117` status `ready` deltaP `21.49` edge `0.6954` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `7.3122` n `117` status `ready` deltaP `25.3883` edge `0.596` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.9143` n `54` status `ready` deltaP `23.7692` edge `0.4625` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.9143` n `54` status `ready` deltaP `23.7692` edge `0.4625` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `6.0124` n `48` status `ready` deltaP `32.0` edge `0.2877` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0124` n `48` status `ready` deltaP `32.0` edge `0.2877` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.2927` n `54` status `ready` deltaP `38.4937` edge `0.5072` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.2927` n `54` status `ready` deltaP `38.4937` edge `0.5072` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `3.5394` n `117` status `ready` deltaP `-3.467` edge `0.3827` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.1489` n `117` status `ready` deltaP `15.0635` edge `0.1854` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.6074` n `117` status `ready` deltaP `8.057` edge `0.1608` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.074` n `117` status `ready` deltaP `12.2408` edge `0.0291` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1116` n `54` status `ready` deltaP `3.4986` edge `0.0346` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1116` n `54` status `ready` deltaP `3.4986` edge `0.0346` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3035` n `117` status `ready` deltaP `1.5477` edge `0.0024` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.3365` n `54` status `ready` deltaP `4.8071` edge `0.0274` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.3365` n `54` status `ready` deltaP `4.8071` edge `0.0274` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.4273` n `117` status `ready` deltaP `6.8159` edge `0.0059` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.4876` n `117` status `ready` deltaP `1.975` edge `-0.0009` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.4921` n `54` status `ready` deltaP `1.4028` edge `0.0007` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

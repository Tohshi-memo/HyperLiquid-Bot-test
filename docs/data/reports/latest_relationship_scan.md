# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T22:07:27.284710+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9421`

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

- `market_context_high->crypto_alt_4h` score `7.3397` n `117` status `ready` deltaP `19.5083` edge `0.626` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `6.9367` n `54` status `ready` deltaP `35.3043` edge `0.3427` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.9367` n `54` status `ready` deltaP `35.3043` edge `0.3427` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.321` n `117` status `ready` deltaP `21.5773` edge `0.5388` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.9349` n `54` status `ready` deltaP `21.7875` edge `0.394` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.9349` n `54` status `ready` deltaP `21.7875` edge `0.394` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6484` n `54` status `ready` deltaP `34.6827` edge `0.45` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6484` n `54` status `ready` deltaP `34.6827` edge `0.45` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7592` n `117` status `ready` deltaP `13.5665` edge `0.1626` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1807` n `117` status `ready` deltaP `5.2127` edge `0.1442` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.465` n `117` status `ready` deltaP `14.8322` edge `0.0444` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2763` n `117` status `ready` deltaP `8.3129` edge `0.0085` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.2939` n `117` status `ready` deltaP `1.6979` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.3889` n `54` status `ready` deltaP `0.6543` edge `0.018` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3889` n `54` status `ready` deltaP `0.6543` edge `0.018` maxDD `-3.7781`
- `risk_on_high->metal_1h` score `-0.394` n `54` status `ready` deltaP `2.8998` edge `0.0033` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.394` n `54` status `ready` deltaP `2.8998` edge `0.0033` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.4787` n `54` status `ready` deltaP `2.439` edge `0.0269` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.4787` n `54` status `ready` deltaP `2.439` edge `0.0269` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.5274` n `117` status `ready` deltaP `1.0741` edge `0.0` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

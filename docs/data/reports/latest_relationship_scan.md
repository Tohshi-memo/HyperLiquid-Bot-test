# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T05:37:31.675262+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9744`

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

- `market_context_high->crypto_alt_4h` score `6.5327` n `110` status `ready` deltaP `17.561` edge `0.5722` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.1047` n `110` status `ready` deltaP `21.3941` edge `0.522` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.729` n `52` status `ready` deltaP `20.6379` edge `0.3846` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.729` n `52` status `ready` deltaP `20.6379` edge `0.3846` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.3278` n `48` status `ready` deltaP `30.087` edge `0.2434` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3278` n `48` status `ready` deltaP `30.087` edge `0.2434` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.8352` n `52` status `ready` deltaP `35.7997` edge `0.4665` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.8352` n `52` status `ready` deltaP `35.7997` edge `0.4665` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `2.9442` n `110` status `ready` deltaP `-3.5421` edge `0.3336` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.8791` n `117` status `ready` deltaP `13.5665` edge `0.1729` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5211` n `117` status `ready` deltaP `7.9073` edge `0.1546` maxDD `-3.7781`
- `risk_on_high->crypto_major_1h` score `-0.1677` n `54` status `ready` deltaP `3.3489` edge `0.0284` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1677` n `54` status `ready` deltaP `3.3489` edge `0.0284` maxDD `-3.7781`
- `market_context_high->metal_4h` score `-0.2338` n `110` status `ready` deltaP `9.8476` edge `0.0194` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.3191` n `117` status `ready` deltaP `1.3976` edge `0.0021` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.5118` n `54` status `ready` deltaP `3.3101` edge `0.0149` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5118` n `54` status `ready` deltaP `3.3101` edge `0.0149` maxDD `-5.8734`
- `market_context_high->index_1h` score `-0.5336` n `117` status `ready` deltaP `1.2243` edge `-0.0018` maxDD `-1.3154`
- `market_context_high->metal_1h` score `-0.5794` n `117` status `ready` deltaP `5.1692` edge `0.0042` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.591` n `54` status `ready` deltaP `-0.2439` edge `-0.001` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

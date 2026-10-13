# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T06:22:25.463260+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9714`

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

- `market_context_high->crypto_alt_4h` score `7.0356` n `113` status `ready` deltaP `18.3575` edge `0.6088` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.4845` n `113` status `ready` deltaP `22.2871` edge `0.5477` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.6318` n `52` status `ready` deltaP `20.6379` edge `0.3765` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.6318` n `52` status `ready` deltaP `20.6379` edge `0.3765` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.3302` n `48` status `ready` deltaP `30.087` edge `0.2436` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3302` n `48` status `ready` deltaP `30.087` edge `0.2436` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.7861` n `52` status `ready` deltaP `35.7997` edge `0.4602` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.7861` n `52` status `ready` deltaP `35.7997` edge `0.4602` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `3.0538` n `113` status `ready` deltaP `-3.4926` edge `0.3424` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.8563` n `117` status `ready` deltaP `13.5665` edge `0.171` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.4575` n `117` status `ready` deltaP `7.4582` edge `0.1523` maxDD `-3.7781`
- `market_context_high->metal_4h` score `-0.0937` n `113` status `ready` deltaP `10.9095` edge `0.024` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.209` n `54` status `ready` deltaP `2.8998` edge `0.0261` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.209` n `54` status `ready` deltaP `2.8998` edge `0.0261` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3576` n `117` status `ready` deltaP `0.9471` edge `0.0019` maxDD `-0.3742`
- `market_context_high->index_1h` score `-0.525` n `117` status `ready` deltaP `1.3744` edge `-0.0017` maxDD `-1.3154`
- `risk_on_high->crypto_alt_1h` score `-0.5266` n `54` status `ready` deltaP `3.3101` edge `0.013` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5266` n `54` status `ready` deltaP `3.3101` edge `0.013` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.5674` n `117` status `ready` deltaP `5.3189` edge `0.0042` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5832` n `54` status `ready` deltaP `-0.0942` edge `-0.001` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

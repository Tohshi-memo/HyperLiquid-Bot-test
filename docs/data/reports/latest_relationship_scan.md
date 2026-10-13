# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T02:07:32.978372+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9338`

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

- `risk_on_high->crypto_alt_4h` score `5.3169` n `48` status `ready` deltaP `20.7826` edge `0.3493` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.3169` n `48` status `ready` deltaP `20.7826` edge `0.3493` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `4.9774` n `38` status `ready` deltaP `30.087` edge `0.2142` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9774` n `38` status `ready` deltaP `30.087` edge `0.2142` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.6151` n `100` status `ready` deltaP `15.8659` edge `0.4237` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.2521` n `48` status `ready` deltaP `35.4167` edge `0.3943` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2521` n `48` status `ready` deltaP `35.4167` edge `0.3943` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `4.1512` n `100` status `ready` deltaP `19.25` edge `0.3735` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.4134` n `108` status `ready` deltaP `11.9151` edge `0.1451` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `0.9435` n `108` status `ready` deltaP `5.4724` edge `0.1227` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2577` n `108` status `ready` deltaP `0.7007` edge `0.0003` maxDD `-0.3742`
- `market_context_high->index_1h` score `-0.3315` n `108` status `ready` deltaP `1.6517` edge `-0.0021` maxDD `-1.1132`
- `market_context_high->metal_4h` score `-0.3408` n `100` status `ready` deltaP `8.6098` edge `0.0095` maxDD `-1.624`
- `market_context_high->unknown_4h` score `-0.3541` n `100` status `ready` deltaP `-4.8415` edge `0.0674` maxDD `-1.8373`
- `risk_on_high->crypto_major_1h` score `-0.4159` n `52` status `ready` deltaP `2.6946` edge `0.0196` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4159` n `52` status `ready` deltaP `2.6946` edge `0.0196` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.5144` n `108` status `ready` deltaP `3.1049` edge `0.0003` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.5905` n `52` status `ready` deltaP `-1.0799` edge `-0.004` maxDD `-0.3742`
- `risk_on_and_context->fx_1h` score `-0.5905` n `52` status `ready` deltaP `-1.0799` edge `-0.004` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.625` n `52` status `ready` deltaP `-0.5988` edge `-0.003` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

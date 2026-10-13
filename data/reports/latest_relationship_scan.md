# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T01:36:18.366415+00:00`
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

- `risk_on_high->crypto_alt_4h` score `5.2881` n `48` status `ready` deltaP `20.7826` edge `0.3469` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.2881` n `48` status `ready` deltaP `20.7826` edge `0.3469` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `4.8226` n `36` status `ready` deltaP `30.087` edge `0.2013` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8226` n `36` status `ready` deltaP `30.087` edge `0.2013` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.5863` n `100` status `ready` deltaP `15.8659` edge `0.4213` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.2443` n `48` status `ready` deltaP `35.4167` edge `0.3933` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2443` n `48` status `ready` deltaP `35.4167` edge `0.3933` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `4.1392` n `100` status `ready` deltaP `19.25` edge `0.3725` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `0.6897` n `106` status `ready` deltaP `11.5157` edge `0.1184` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `0.3906` n `106` status `ready` deltaP `4.8808` edge `0.0981` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.1897` n `106` status `ready` deltaP `2.5951` edge `-0.0007` maxDD `-0.94`
- `market_context_high->unknown_4h` score `-0.2629` n `100` status `ready` deltaP `-4.8415` edge `0.075` maxDD `-1.8373`
- `market_context_high->fx_1h` score `-0.3063` n `106` status `ready` deltaP `-0.1728` edge `-0.0001` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.3128` n `52` status `ready` deltaP `2.994` edge `0.0262` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3128` n `52` status `ready` deltaP `2.994` edge `0.0262` maxDD `-3.7781`
- `market_context_high->metal_4h` score `-0.3384` n `100` status `ready` deltaP `8.6098` edge `0.0097` maxDD `-1.624`
- `market_context_high->metal_1h` score `-0.4623` n `106` status `ready` deltaP `3.3245` edge `0.0009` maxDD `-0.9204`
- `risk_on_high->fx_1h` score `-0.5893` n `52` status `ready` deltaP `-1.0799` edge `-0.0039` maxDD `-0.3742`
- `risk_on_and_context->fx_1h` score `-0.5893` n `52` status `ready` deltaP `-1.0799` edge `-0.0039` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.5962` n `52` status `ready` deltaP `3.0977` edge `0.0055` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

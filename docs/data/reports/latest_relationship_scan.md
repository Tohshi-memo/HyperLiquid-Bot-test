# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T02:52:27.774955+00:00`
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

- `risk_on_high->crypto_alt_4h` score `5.3553` n `48` status `ready` deltaP `20.7826` edge `0.3525` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.3553` n `48` status `ready` deltaP `20.7826` edge `0.3525` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.1562` n `41` status `ready` deltaP `30.087` edge `0.2291` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.1562` n `41` status `ready` deltaP `30.087` edge `0.2291` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.6535` n `100` status `ready` deltaP `15.8659` edge `0.4269` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.2467` n `48` status `ready` deltaP `35.4167` edge `0.3936` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2467` n `48` status `ready` deltaP `35.4167` edge `0.3936` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `4.1428` n `100` status `ready` deltaP `19.25` edge `0.3728` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.5296` n `111` status `ready` deltaP `12.467` edge `0.1511` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.1957` n `111` status `ready` deltaP `6.2996` edge `0.1382` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2528` n `111` status `ready` deltaP `0.7508` edge `0.0006` maxDD `-0.3742`
- `market_context_high->metal_4h` score `-0.3444` n `100` status `ready` deltaP `8.6098` edge `0.0092` maxDD `-1.624`
- `market_context_high->metal_1h` score `-0.4508` n `111` status `ready` deltaP `4.0568` edge `0.0021` maxDD `-0.9556`
- `market_context_high->unknown_4h` score `-0.5115` n `100` status `ready` deltaP `-4.9939` edge `0.0553` maxDD `-1.8373`
- `risk_on_high->crypto_major_1h` score `-0.5119` n `52` status `ready` deltaP `2.2455` edge `0.0146` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.5119` n `52` status `ready` deltaP `2.2455` edge `0.0146` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.5214` n `111` status `ready` deltaP `0.3003` edge `-0.0031` maxDD `-1.2601`
- `risk_on_high->fx_1h` score `-0.6169` n `52` status `ready` deltaP `-1.3802` edge `-0.0042` maxDD `-0.3742`
- `risk_on_and_context->fx_1h` score `-0.6169` n `52` status `ready` deltaP `-1.3802` edge `-0.0042` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.6453` n `52` status `ready` deltaP `-0.8982` edge `-0.0036` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

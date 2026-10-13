# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T17:22:30.426140+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9582`

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

- `market_context_high->crypto_alt_4h` score `7.8827` n `117` status `ready` deltaP `19.6608` edge `0.6707` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.8439` n `117` status `ready` deltaP `23.2541` edge `0.5712` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.4715` n `54` status `ready` deltaP `21.94` edge `0.4378` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.4715` n `54` status `ready` deltaP `21.94` edge `0.4378` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `6.2917` n `48` status `ready` deltaP `32.0557` edge `0.3106` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2917` n `48` status `ready` deltaP `32.0557` edge `0.3106` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.9883` n `54` status `ready` deltaP `36.3595` edge `0.4824` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.9883` n `54` status `ready` deltaP `36.3595` edge `0.4824` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.5402` n `117` status `ready` deltaP `-3.467` edge `0.4661` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.0733` n `117` status `ready` deltaP `14.9138` edge `0.1801` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5355` n `117` status `ready` deltaP `7.9073` edge `0.1558` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3638` n `117` status `ready` deltaP `14.5273` edge `0.038` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1583` n `54` status `ready` deltaP `3.3489` edge `0.0296` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1583` n `54` status `ready` deltaP `3.3489` edge `0.0296` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2927` n `117` status `ready` deltaP `1.6979` edge `0.0023` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.3482` n `117` status `ready` deltaP `7.5644` edge `0.0075` maxDD `-0.9556`
- `risk_on_high->crypto_alt_1h` score `-0.3856` n `54` status `ready` deltaP `4.6574` edge `0.0221` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.3856` n `54` status `ready` deltaP `4.6574` edge `0.0221` maxDD `-5.8734`
- `risk_on_high->metal_1h` score `-0.4407` n `54` status `ready` deltaP `2.1513` edge `0.0023` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4407` n `54` status `ready` deltaP `2.1513` edge `0.0023` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

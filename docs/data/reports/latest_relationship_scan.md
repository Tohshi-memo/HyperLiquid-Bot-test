# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T15:07:31.857832+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9576`

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

- `market_context_high->crypto_alt_4h` score `8.1902` n `117` status `ready` deltaP `20.8803` edge `0.6882` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `7.1397` n `117` status `ready` deltaP `24.6261` edge `0.5867` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.7791` n `54` status `ready` deltaP `23.1595` edge `0.4553` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.7791` n `54` status `ready` deltaP `23.1595` edge `0.4553` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `6.1633` n `48` status `ready` deltaP `32.0557` edge `0.2999` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1633` n `48` status `ready` deltaP `32.0557` edge `0.2999` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.1806` n `54` status `ready` deltaP `37.7315` edge `0.4979` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.1806` n `54` status `ready` deltaP `37.7315` edge `0.4979` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.113` n `117` status `ready` deltaP `-3.467` edge `0.4305` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.1069` n `117` status `ready` deltaP `14.9138` edge `0.1829` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5727` n `117` status `ready` deltaP `7.9073` edge `0.1589` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1856` n `117` status `ready` deltaP `13.1554` edge `0.0323` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1342` n `54` status `ready` deltaP `3.3489` edge `0.0327` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1342` n `54` status `ready` deltaP `3.3489` edge `0.0327` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3299` n `117` status `ready` deltaP `1.2474` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.3638` n `54` status `ready` deltaP `4.6574` edge `0.0249` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.3638` n `54` status `ready` deltaP `4.6574` edge `0.0249` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.4129` n `117` status `ready` deltaP `6.9656` edge `0.0061` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4828` n `54` status `ready` deltaP `1.5525` edge `0.0009` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4828` n `54` status `ready` deltaP `1.5525` edge `0.0009` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

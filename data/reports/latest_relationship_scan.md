# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T09:07:32.259743+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9717`

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

- `risk_on_high->commodity_24h` score `7.9363` n `54` status `ready` deltaP `41.2892` edge `0.3861` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9363` n `54` status `ready` deltaP `41.2892` edge `0.3861` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.7399` n `120` status `ready` deltaP `18.7805` edge `0.6642` maxDD `-9.2196`
- `risk_on_high->crypto_alt_4h` score `6.8351` n `54` status `ready` deltaP `22.8546` edge `0.4619` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.8351` n `54` status `ready` deltaP `22.8546` edge `0.4619` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.1172` n `120` status `ready` deltaP `20.0204` edge `0.5322` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.7375` n `54` status `ready` deltaP `34.8352` edge `0.4604` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.7375` n `54` status `ready` deltaP `34.8352` edge `0.4604` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7931` n `123` status `ready` deltaP `13.3294` edge `0.167` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0813` n `123` status `ready` deltaP `5.0497` edge `0.137` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0732` n `120` status `ready` deltaP `10.9857` edge `0.0374` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3406` n `54` status `ready` deltaP `0.804` edge `0.0232` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3406` n `54` status `ready` deltaP `0.804` edge `0.0232` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3551` n `54` status `ready` deltaP `4.6574` edge `0.0257` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3551` n `54` status `ready` deltaP `4.6574` edge `0.0257` maxDD `-5.8485`
- `market_context_high->fx_1h` score `-0.3569` n `123` status `ready` deltaP `-0.8204` edge `-0.0019` maxDD `-0.4047`
- `market_context_high->commodity_24h` score `-0.4312` n `116` status `ready` deltaP `12.8409` edge `0.1476` maxDD `-12.0788`
- `market_context_high->metal_1h` score `-0.4448` n `123` status `ready` deltaP `6.6112` edge `0.0058` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4726` n `54` status `ready` deltaP `1.5525` edge `0.0022` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4726` n `54` status `ready` deltaP `1.5525` edge `0.0022` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

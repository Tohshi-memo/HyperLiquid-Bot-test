# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T16:37:36.174433+00:00`
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

- `market_context_high->crypto_alt_4h` score `7.9574` n `117` status `ready` deltaP `19.9656` edge `0.6749` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.9225` n `117` status `ready` deltaP `23.7115` edge `0.5747` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.5463` n `54` status `ready` deltaP `22.2448` edge `0.442` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.5463` n `54` status `ready` deltaP `22.2448` edge `0.442` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `6.2713` n `48` status `ready` deltaP `32.0557` edge `0.3089` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2713` n `48` status `ready` deltaP `32.0557` edge `0.3089` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.0394` n `54` status `ready` deltaP `36.8169` edge `0.4859` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.0394` n `54` status `ready` deltaP `36.8169` edge `0.4859` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.2714` n `117` status `ready` deltaP `-3.467` edge `0.4437` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.1201` n `117` status `ready` deltaP `15.0635` edge `0.183` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.563` n `117` status `ready` deltaP `8.057` edge `0.1571` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3128` n `117` status `ready` deltaP `14.07` edge `0.0368` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1404` n `54` status `ready` deltaP `3.4986` edge `0.0309` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1404` n `54` status `ready` deltaP `3.4986` edge `0.0309` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3167` n `117` status `ready` deltaP `1.3976` edge `0.0023` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.335` n `117` status `ready` deltaP `7.7141` edge `0.0076` maxDD `-0.9556`
- `risk_on_high->crypto_alt_1h` score `-0.3552` n `54` status `ready` deltaP `4.8071` edge `0.025` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.3552` n `54` status `ready` deltaP `4.8071` edge `0.025` maxDD `-5.8734`
- `risk_on_high->metal_1h` score `-0.4321` n `54` status `ready` deltaP `2.301` edge `0.0024` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4321` n `54` status `ready` deltaP `2.301` edge `0.0024` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
